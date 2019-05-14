####################################################################################
######## This part for the docs of this program ####################################
'''
.
. 	thing_global_id = platform_id + thing_local_id
. 	item_global_id  = platform_id + thing_local_id + item_local_id
. 	A item without things seemly as a thing
.
'''

import paho.mqtt.client as mqtt
import json
from requests import get
import hashlib
from openhab import openHAB
import urllib
import numpy as np

import hashlib
import time
from Fog.Driver.Driver_Base import Driver
# from Driver_Base import Driver


class OpenHAB(Driver):
    def __init__(self, config_path, time_push_config, time_push_state):
        Driver.__init__(self, config_path, time_push_config, time_push_state)

        base_url = "http://" + self.host + ":" + self.port + "/rest"
        self.openhab = openHAB(base_url)

    def get_things_from_openhab(self):
        while True:
            try:
                thing_url = "http://" + self.host + ":" + self.port + "/rest/things"
                things = get(thing_url).json()
                return things
            except:
                self.logger.error("Error connect to Platform")
                time.sleep(2)

    def get_item_from_openhab(self, item_name):
        while True:
            try:
                item = self.openhab.get_item(item_name)
                return item
            except:
                self.logger.error("Error connect to Platform")
                time.sleep(2)

    def get_items_from_openhab(self):
        while True:
            try:
                items = self.openhab.fetch_all_items()
                return items
            except:
                self.logger.error("Error connect to Platform")
                time.sleep(2)

    def get_item_raw_from_openhab(self, item_to_thing):
        while True:
            try:
                item = self.openhab.get_item_raw(item_to_thing)
                return item
            except:
                self.logger.error("Error connect to Platform")
                time.sleep(2)

    def get_states(self):
        things = self.get_things_from_openhab()
        # print("STATES: {}".format(things))
        states = []
        item_of_thing_list = []

        # Get all items in openHAB
        items = self.get_items_from_openhab()  # dict of openHAB items
        items_list = list(items)

        # Get all things and items of things in openHAB
        for thing in things:
            thing_type = thing["thingTypeUID"]
            thing_name = thing["label"]
            thing_local_id = thing["UID"]
            thing_global_id = self.platform_id + "-" + thing_local_id
            thing_location = thing["location"]
            linked_items = thing["channels"]
            items_state = []

            for linked_item in linked_items:
                item_type = linked_item["itemType"]
                item_name = linked_item["linkedItems"][0]
                item_of_thing_list.append(item_name)  # Get all item of things.
                item_local_id = item_name
                item_url = "http://" + self.host + ":" + self.port + "/rest/items?recursive=false"
                item = self.get_item_from_openhab(item_name)

                metric_local_id = linked_item["itemType"]
                detect_value = self.detect_data_type(item['state'])
                value_detected = detect_value[1]
                data_type_detected = detect_value[0]

                states.append({
                    "MetricLocalId": metric_local_id,
                    "DataPoint": {
                        "DataType": data_type_detected,
                        "Value": value_detected
                    }
                })

        # Get items not belong thing
        item_of_thing_list = np.asarray(item_of_thing_list)

        if (item_of_thing_list != []):
            remain_item_list = list(set(items_list) - set(item_of_thing_list))
        else:
            remain_item_list = list(set(items_list))

        # Those items above be converted to things
        for item_to_thing in remain_item_list:
            item = self.get_item_raw_from_openhab(item_to_thing)
            # print("STATES ITEM: {}".format(item))
            item_type = item['type']
            item_name = item['name']
            item_local_id = item_name
            thing_name = item_name
            metric_local_id = item_local_id
            detect_value = self.detect_data_type(item['state'])
            value_detected = detect_value[1]
            data_type_detected = detect_value[0]

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


    def set_state(self, metric_local_id, metric_name, metric_domain, new_value):
        # print("SET STATE {} to {}".format(metric_local_id, new_value))
        try:
            item = self.openhab.get_item(metric_local_id)
            if isinstance(new_value, str):
                item.command(new_value.upper())
        except:
            self.logger.error("Don't support {} set new_value: {}".format(metric_name, new_value))




if __name__ == '__main__':
    CONFIG_PATH = "/media/hamhochoi/Beo/OneDrive for Business 1/OneDrive - student.hust.edu.vn/OD/20182/DATN/Fog/Driver/OpenHab/config/openhab.ini"
    TIME_PUSH_STATE = 5
    TIME_PUSH_CONFIG = 20
    openHAB = OpenHAB(CONFIG_PATH, TIME_PUSH_CONFIG, TIME_PUSH_STATE)
    openHAB.run()
