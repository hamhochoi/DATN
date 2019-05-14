import json
import paho.mqtt.client as mqtt
import sys
import copy
import logging
import json
import os
import datetime



class Filter:
    def __init__(self, broker_fog):
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
        self.logger.setLevel(logging.INFO)
        # -----> end configure logging <-----

        self.client = mqtt.Client()
        self.client.connect(broker_fog)
        self.now_state = {}         # {global_id : value_state}
        self.datapoint_folder = "/media/hamhochoi/Beo/OneDrive for Business 1/OneDrive - student.hust.edu.vn/OD/20182/DATN/data/datapoint"
        self.metric_folder = "/media/hamhochoi/Beo/OneDrive for Business 1/OneDrive - student.hust.edu.vn/OD/20182/DATN/data/metric"




    def on_connect(self, client, userdata, flags, rc):
        self.logger.info("Connected to Mosquitto")
        filter_topic_sub = 'driver/response/filter/api_get_states'
        self.client.subscribe(filter_topic_sub)


    def filter_message(self, client, userdata, msg):
        self.logger.info("Filter message before send to Collector")
        # filter_topic_pub = 'filter/response/forwarder/api_get_states'
        message = json.loads(msg.payload.decode('utf-8'))
        self.logger.debug("Meassage before: {}".format(message))
        # self.client.publish(filter_topic_pub, json.dumps(message))

        received_state = message['body']['states']
        filter_states = copy.deepcopy(received_state)
        # print (filter_states)


        # Update files
        for filter_state in filter_states:
            metric_id = filter_state['MetricId']
            
            # Update datapoint file
            datapoint_id = metric_id + "_datapoint"
            datapoint_file_path = os.path.join(self.datapoint_folder, datapoint_id+".json")

            datapoint = filter_state['DataPoint']
            time = datetime.datetime.now()
            datapoint['time'] = str(time)
            datapoint['DatapointId'] = datapoint_id
            f = open(datapoint_file_path, 'w')
            json_file = json.dump(datapoint, f)
            f.close()
            
            # update metric file
            metric_file_path = os.path.join(self.metric_folder, metric_id+".json")
            if ("DataPoint" in filter_state):
                del filter_state["DataPoint"]
                # print (filter_state)
            filter_state['HasDatapoint'] = [str(datapoint_id)]
            f = open(metric_file_path, 'w')
            json_file = json.dump(filter_state, f)
            f.close()


    def api_get_state(self):
        self.client.publish("/request/api_get_states", "")


    def api_set_state(self, topic, message):
        self.client.publish(topic, message)


    def run(self):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.filter_message
        self.client.loop_forever()


if __name__ == '__main__':
    MODE_CODE = 'Develop'
    #MODE_CODE = 'Deploy'

    if MODE_CODE == 'Develop':
        BROKER_FOG = 'broker.hivemq.com'
    else:
        BROKER_FOG = sys.argv[1]

    filter_fog = Filter(BROKER_FOG)
    filter_fog.run()

