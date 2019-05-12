import unittest
from language.api import *
import json


class TestAPI(unittest.TestCase):
    def test_api_get_all_datapoint(self):
        results = api_get_all_datapoint()
        expected_results = [{'time': '15:00:00-12-05-2019', 'DatapointId': 'humidity_homeassistant_datapoint', 'value': '64.0', 'DataType': 'float'}, {'time': '15:00:00-12-05-2019', 'DatapointId': 'humidity_openhab_datapoint', 'value': '63.0', 'DataType': 'float'}, {'time': '15:00:00-12-05-2019', 'DatapointId': 'humidity_thingsboard_datapoint', 'value': '65.0', 'DataType': 'float'}, {'time': '15:00:00-12-05-2019', 'DatapointId': 'light_homeassistant_datapoint', 'value': '0', 'DataType': 'int'}, {'time': '15:00:00-12-05-2019', 'DatapointId': 'light_openhab_datapoint', 'value': '0', 'DataType': 'int'}, {'time': '15:00:00-12-05-2019', 'DatapointId': 'light_thingsboard_datapoint', 'value': '0', 'DataType': 'int'}, {'time': '15:00:00-12-05-2019', 'DatapointId': 'motion_homeassistant_datapoint', 'value': '0', 'DataType': 'int'}, {'time': '15:00:00-12-05-2019', 'DatapointId': 'motion_openhab_datapoint', 'value': '0', 'DataType': 'int'}, {'time': '15:00:00-12-05-2019', 'DatapointId': 'motion_thingsboard_datapoint', 'value': '0', 'DataType': 'int'}, {'time': '15:00:00-12-05-2019', 'DatapointId': 'temperature_homeassistant_datapoint', 'value': '26.0', 'DataType': 'float'}, {'time': '15:00:00-12-05-2019', 'DatapointId': 'temperature_openhab_datapoint', 'value': '25.0', 'DataType': 'float'}, {'time': '15:00:00-12-05-2019', 'DatapointId': 'temperature_thingsboard_datapoint', 'value': '27.0', 'DataType': 'float'}]
        self.assertEqual(results, expected_results)











if __name__ == "__main__":
    unittest.main()
