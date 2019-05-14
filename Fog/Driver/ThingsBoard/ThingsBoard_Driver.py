import http.client
import json
import hashlib

from kombu.utils.scheduling import priority_cycle

from Fog.Driver.Driver_Base import Driver
import time
import urllib


class ThingsBoard(Driver):
    def __init__(self, config_path, time_push_config, time_push_state):
        Driver.__init__(self, config_path, time_push_config, time_push_state)

    def get_authorization(self):
        conn = http.client.HTTPConnection(self.host + ':' + self.port)
        headers = {
            'Accept': "application/json",
            'Content-Type': "application/json"
        }

        body = '{"username":"tenant@thingsboard.org", "password":"tenant"}'

        conn.request("POST", "/api/auth/login", body=body, headers=headers)
        response_data = conn.getresponse().read()
        response_json = json.loads(response_data.decode("utf-8"))

        return response_json

    def connect(self):
        while True:
            try:
                conn = http.client.HTTPConnection(self.host + ':' + self.port)
                authorization = self.get_authorization()
                headers = {
                    'Accept': "application/json",
                    'X-Authorization': "Bearer " + authorization["token"],
                }
                return [conn, headers]
            except:
                self.logger.error("Error connect to Platform")
                time.sleep(2)
                continue

    def get_customer_id(self):
        result = self.connect()
        conn = result[0]
        headers = result[1]

        conn.request("GET", "/api/customers?limit=11", headers=headers)
        data = conn.getresponse().read()
        json_data = json.loads(data.decode("utf-8"))
        return json_data['data'][0]['id']['id']

    def get_list_device_on_customes(self):
        # print("get list")
        result = self.connect()
        conn = result[0]
        headers = result[1]
        customer_id = self.get_customer_id()

        conn.request("GET", "/api/customer/" + customer_id + "/devices?limit=111", headers=headers)
        data = conn.getresponse().read()
        json_data = json.loads(data.decode("utf-8"))
        device_list = json_data['data']

        return device_list

    def get_access_token_device(self, thing_local_id):
        # print("Get Access token device: ")
        result = self.connect()
        conn = result[0]
        headers = result[1]

        conn.request("GET", "/api/device/" + thing_local_id + "/credentials", headers=headers)
        data = conn.getresponse().read()
        json_data = json.loads(data.decode("utf-8"))

        return json_data['credentialsId']

    def get_telemetry_keys(self, thing_local_id):
        telemetries = []

        result = self.connect()
        conn = result[0]
        headers = result[1]

        url = "/api/plugins/telemetry/DEVICE/" + thing_local_id + "/keys/timeseries"
        conn.request("GET", url, headers=headers)
        data = conn.getresponse().read()
        json_data = json.loads(data.decode("utf-8"))

        for i, telemetry in enumerate(json_data):
            telemetries.append(telemetry)

        return [json_data, ",".join(sorted(telemetries))]

    def get_dashboard_id_on_customes_id(self, customers_id):
        result = self.connect()
        conn = result[0]
        headers = result[1]
        print("customer_id: {}".format(customers_id))
        conn.request("GET", "/api/customer/" + customers_id + "/dashboards?ascOrder=false&limit=111", headers=headers)
        data = conn.getresponse().read()
        json_data = json.loads(data.decode("utf-8"))
        print ("haha : {}".format(json_data['data']))
        return json_data['data'][0]['id']['id']

    def get_label_on_dashboard_id(self):
        result = self.connect()
        conn = result[0]
        headers = result[1]
        customer_id = self.get_customer_id()

        dashboard_id = self.get_dashboard_id_on_customes_id(customer_id)
        conn.request("GET", "/api/dashboard/" + dashboard_id, headers=headers)
        data = conn.getresponse().read()
        json_data = json.loads(data.decode("utf-8"))
        key = list(json_data["configuration"]["widgets"].keys())[0]
        #print("JSON_DASHBOARD: {}".format(json_data))
        return json_data["configuration"]["widgets"][key]["config"]["settings"]["gpioList"]

    def get_states(self):
        # print("get states")
        states = []
        device_list = self.get_list_device_on_customes()
        # print (device_list)

        result = self.connect()
        conn = result[0]
        headers = result[1]

        for device in device_list:
            result_telemetry_keys = self.get_telemetry_keys(device["id"]["id"])
            # print(result_telemetry_keys)
            keys_telemetry_list = result_telemetry_keys[0]
            telemetries = result_telemetry_keys[1]

            url = "/api/plugins/telemetry/DEVICE/" + device["id"]["id"] + "/values/timeseries?keys=" + telemetries
            url = url.replace(" ", "%20")
            #print("url: {}".format(url))
            conn.request("GET", url, headers=headers)
            response_data = conn.getresponse().read()
            # print(response_data)
            response_json = json.loads(response_data.decode("utf-8"))
            #print(response_json)

            for telemetry in keys_telemetry_list:
                item_state = response_json[telemetry][0]["value"]
                item_name = telemetry

                metric_local_id = device["id"]["id"] + '-' + item_name
                detect_value = self.detect_data_type(item_state)
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

                # if metric_local_id in self.now_metric_domain:
                #     mapped = self.mapping_data_value(self.now_metric_domain[metric_local_id], value_detected, data_type_detected)

                #     #print("self.now_metric_domain[metric_local_id]: {}, value_detected: {}, data_type_detected {}, mapped: {}".format(self.now_metric_domain[metric_local_id], value_detected, data_type_detected, mapped))
                #     data_type_mapped = mapped[1]
                #     value_mapped = mapped[0]
                #     states.append({
                #         "MetricLocalId": metric_local_id,
                #         "DataPoint": {
                #             "DataType": data_type_mapped,
                #             "Value": value_mapped
                #         }
                    # })
        # print (states)
        return states

    def set_state(self, metric_local_id, metric_name, metric_domain, new_value):
        result = self.connect()
        conn = result[0]
        headers = result[1]

        # if metric_domain == "switch":
        try:
            pin = metric_local_id.rsplit('-', 1)[1]
            device_id = metric_local_id.rsplit('-', 1)[0]
            # print("TACH : {}".format(metric_local_id.rsplit('-', 1)))
            # print("pin: {} device_id: {}".format(pin, device_id))
            if new_value == "on":
                body = '{"method":"setGpioStatus","params":{"pin":' + pin + ',"enabled":true}}'
                conn.request("POST", "/api/plugins/rpc/twoway/" + device_id, body=body, headers=headers)
            elif new_value == "off":
                body = '{"method":"setGpioStatus","params":{"pin":' + pin + ',"enabled":false}}'
                conn.request("POST", "/api/plugins/rpc/twoway/" + device_id, body=body, headers=headers)
            else:
                self.logger.error("Don't support type of new_value: {}".format(new_value))
        # else:
        except:
            self.logger.error("Don't support {} set new_value: {}".format(metric_name, new_value))


if __name__ == '__main__':
    CONFIG_PATH = "/media/hamhochoi/Beo/OneDrive for Business 1/OneDrive - student.hust.edu.vn/OD/20182/DATN/Fog/Driver/ThingsBoard/config/thingsboard.ini"
    TIME_PUSH_STATE = 5
    TIME_PUSH_CONFIG = 10
    things_board = ThingsBoard(CONFIG_PATH, TIME_PUSH_STATE, TIME_PUSH_CONFIG)
    things_board.run()