import paho.mqtt.client as mqtt
import json
import configparser
import threading
import logging
from ast import literal_eval
import os
import copy
import requests
import time

class Driver:

    def __init__(self, config_path, time_push_config, time_push_state):
        # ----->configure logging <-----
        # if not os.path.exists('logging'):
        #     os.makedirs('logging')
        # handler = logging.handlers.RotatingFileHandler('logging/driver.log', maxBytes=200,
        #                               backupCount=1)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(fmt='[%(asctime)s - %(levelname)s - %(name)s] - %(message)s',
                                      datefmt='%m-%d-%Y %H:%M:%S')
        handler.setFormatter(formatter)
        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)
        # -----> end configure logging <-----

        self.now_info = []
        self.now_metric_domain = {}     # 'local_id': 'metric_domain'
        self.list_mapping_id = {}       # 'local_id': 'global_id'
        config = configparser.ConfigParser()
        config.read(config_path)
        self.time_push_config = int(time_push_config)
        self.time_push_state = int(time_push_state)
        self.host = config['PLATFORM']['host']
        self.port = config['PLATFORM']['port']
        self.platform_name = config['PLATFORM']['platform_name']
        self.platform_type = config['PLATFORM']['platform_type']
        # self.platform_id = None
        self.platform_id = config['PLATFORM']['platform_id']

        broker_fog = config['BROKER']['host']
        self.clientMQTT = mqtt.Client()
        self.clientMQTT.connect(broker_fog)
        self.clientMQTT.on_connect = self.on_connect
        self.clientMQTT.on_disconnect = self.on_disconnect

      
        self.clientMQTT.subscribe('/request/api_get_states')
        self.clientMQTT.message_callback_add('/request/api_get_states', self.api_get_states)

        self.clientMQTT.subscribe(str(self.platform_id) + '/request/api_set_state', qos=2)
        self.clientMQTT.message_callback_add(str(self.platform_id) + '/request/api_set_state', self.api_set_state)
       
    def mapping_id(self, info, ids, is_config=True):
        if is_config is True:
            for source in info:
                if source['information']['LocalId'] in ids:
                    source['information']['SourceId'] = ids[source['information']['LocalId']]

                for metric in source['metrics']:
                    if metric['MetricLocalId'] in ids:
                        metric['MetricId'] = ids[metric['MetricLocalId']]
        else:
            for metric in info:
                if metric['MetricLocalId'] in ids:
                    metric['MetricId'] = ids[metric['MetricLocalId']]

    def api_get_states(self, client, userdata, msg):
        self.logger.info("API get states")
        # message = json.loads(msg.payload.decode('utf-8'))
        states = self.get_states()

        message_response = {
            # "header": message['header'],
            "body": {}
        }

        self.mapping_id(states, copy.deepcopy(self.list_mapping_id), is_config=False)
        message_response['body']['states'] = states
        self.clientMQTT.publish('driver/response/filter/api_get_states', json.dumps(message_response))

    # This API is called when driver send configuration change
    # then registry response active_sources to driver for update now_configuration
    # def api_update_now_configuration(self, client, userdata, msg):
    #     message = json.loads(msg.payload.decode('utf-8'))
    #     self.logger.info("API update now configuration")
    #     self.handle_info_from_registry(info_receive_from_registry=message['body']['active_sources'])

    def api_set_state(self, client, userdata, msg):
        message = json.loads(msg.payload.decode('utf-8'))
        body = message['body']
        metric_local_id = body['MetricId']
        # metric_name = body['metric']['MetricName']
        # metric_domain = body['metric']['MetricDomain']
        metric_name = ""
        metric_domain = ""
        new_value = body['new_value']
        self.logger.info("API set state: {} to {}".format(metric_name, new_value))
        self.set_state(metric_local_id, metric_name, metric_domain, new_value)

    def on_disconnect(self, client, userdata, rc):
        if rc != 0:
            self.logger.warning("Disconnected to BROKER_FOG.")
            

    def on_connect(self, client, userdata, flags, rc):
        self.logger.info("Connected to BROKER_FOG.")
        if self.platform_id is not None:
            self.clientMQTT.subscribe('/request/api_get_states')
            self.clientMQTT.message_callback_add('/request/api_get_states', self.api_get_states)

            
            self.clientMQTT.subscribe(str(self.platform_id) + '/request/api_set_state', qos=2)
            self.clientMQTT.message_callback_add(str(self.platform_id) + '/request/api_set_state', self.api_set_state)

    def run(self):
        
        # thread_push_get_state= threading.Thread(target=self.push_get_state)
        # thread_push_get_state.setDaemon(True)
        # thread_push_get_state.start()

        self.clientMQTT.loop_forever()
        # self.push_get_state()

    def push_get_state(self):
        # while 1:
        if 1:
            message = {
                "header":{},
                "body": {}
            }
            states = self.get_states()
            # message['header']['reply_to'] = 'driver.response.collector.api_get_states'
            message['header']['PlatformId'] = self.platform_id
            message['header']['PlatformType'] = self.platform_type
            message['header']['PlatformName'] = self.platform_name
            message['header']['PlatformHost'] = self.host
            message['header']['PlatformPort'] = self.port
            message['header']['PlatformStatus'] = "active"


            # message['header']['mode'] = "PUSH"
            self.mapping_id(states, copy.deepcopy(self.list_mapping_id), is_config=False)
            message['body']['states'] = states
            self.logger.debug("Push state to Filter")
            self.clientMQTT.publish('driver/response/filter/api_get_states', json.dumps(message))
            # time.sleep(self.time_push_state)

    def get_states(self):
        pass

    def set_state(self, metric_local_id, metric_name, metric_domain, new_value):
        pass

    # This function mapping value of data point to unified style
    def mapping_data_value(self, domain_name, value, datatype):
        value_domain = self.metric_domain_file[domain_name]["value"]
        if isinstance(value_domain, list):
            if value in value_domain:
                return [value, datatype]
            elif 'mapping' in self.metric_domain_file[domain_name]:
                if value in self.metric_domain_file[domain_name]['mapping']:
                    value_mapped = self.metric_domain_file[domain_name]['mapping'][value]
                    return [value_mapped, self.detect_data_type(str(value_mapped))[0]]
            else:
                return "ERROR typedata"

        elif value_domain == "number":
            if datatype == "float" or datatype == "int":
                return [value, datatype]
            else:
                return "ERROR typedata"

    @staticmethod
    def detect_data_type(value):

        try:
            number = literal_eval(str(value))
        except:
            return ["string", value]

        if isinstance(number, int) or (isinstance(number, float) and number.is_integer()):
            return ["int", int(number)]
        elif isinstance(number, float):
            return ["float", float(number)]
        else:
            return ["unknown", value]

    def ordered(self, obj):
        if isinstance(obj, dict):
            return sorted((k, self.ordered(v)) for k, v in obj.items())
        if isinstance(obj, list):
            return sorted(self.ordered(x) for x in obj)
        else:
            return obj