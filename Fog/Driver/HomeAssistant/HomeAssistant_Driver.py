import json
import requests
import hashlib
import time
from Fog.Driver.Driver_Base import Driver
import sys


class HomeAssistant(Driver):
    def __init__(self, config_path, time_push_config, time_push_state):

        # logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG, datefmt='%m-%d-%Y %H:%M:%S')
        Driver.__init__(self, config_path, time_push_config, time_push_state)

    def get_states(self):
        # self.logger.debug('Get state of all things')
        url = 'http://' + self.host + ':' + self.port + '/api/states'
        message = {
            "header": {},
            "body": {}
        }
        response = self.connect_platform(url)
        states = []

        for metric in response:
            thing_local_type = metric['entity_id'].split(".")[0]
            if thing_local_type != 'group' and thing_local_type != 'automation' and thing_local_type != 'updater':
                metric_local_id = metric['entity_id']
                detect_value = self.detect_data_type(metric['state'])
                value_detected = detect_value[1]
                data_type_detected = detect_value[0]
                item_name = metric['attributes']['friendly_name']
                
                states.append({
                    "MetricId": metric_local_id,
                    "MetricLocalId": metric_local_id,
                    "MetricName" : item_name,
                    "MetricStatus" : "active",
                    "CanSetState" : "false",
                    "MetricType" : "gauge",
                    "Unit" : "",
                    "MetricDomain" : "sensor",
                    "DataPoint": {
                        "DataType": data_type_detected,
                        "value": value_detected
                }
            })

        return states


    def connect_platform(self, url):
        while True:
            try:
                # url = 'http://' + host_homeAssistant + ':' + port_homeAssistant + '/api/states'
                response = requests.get(url).json()
                return response
            except:
                self.logger.error("Error connect to Platform")
                time.sleep(2)
                continue

    def set_state(self, metric_local_id, metric_name, metric_domain, new_value):
        # if metric_domain == 'switch':
        try:
            if new_value == "on":
                url = 'http://' + self.host + ':' + self.port + '/api/services/light/turn_on'
                data = {"entity_id": metric_local_id}
                response = requests.post(url, json.dumps(data))
            else:
                url = 'http://' + self.host + ':' + self.port + '/api/services/light/turn_off'
                data = {"entity_id": metric_local_id}
                response = requests.post(url, json.dumps(data))
        # else:
        except:
            self.logger.error("Don't support {} set new_value: {}".format(metric_name, new_value))


if __name__ == '__main__':
    CONFIG_PATH = "/media/hamhochoi/Beo/OneDrive for Business 1/OneDrive - student.hust.edu.vn/OD/20182/DATN/Fog/Driver/HomeAssistant/config/configuration.ini"
    # TIME_PUSH_CONFIG = sys.argv[1]
    # TIME_PUSH_STATE = int(sys.argv[2])
    TIME_PUSH_CONFIG = 15
    TIME_PUSH_STATE = 5
    home_assistant = HomeAssistant(CONFIG_PATH, TIME_PUSH_CONFIG, TIME_PUSH_STATE)
    home_assistant.run()

    
