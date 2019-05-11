import unittest
from language.api import *
import json


class TestAPI(unittest.TestCase):


    # def test_api_get_metric_from_source(self):
    #     source_id = 'source_id_1'
    #     results = api_get_metric_from_source(source_id)

    #     self.assertEqual(str(results[0]), "('metric_id_1', 'source_id_1', 'Temperature', 'Gauge', '*C', 'sensor', 'active', 'metric_local_id')")


    def test_api_get_all_datapoint(self):
        results = api_get_all_datapoint()
        expected_results = [(u'int', 32, u'2018-03-28T08:01:00Z'), (u'int', 27, u'2019-04-28T08:01:00Z')]
        self.assertEqual(results, expected_results)


    def test_api_get_datapoint_from_measurement(self):
        measurement = "metric_id_1"
        result = api_get_datapoint_from_measurement(measurement)
        expected_results = [(u'int', 32, u'2018-03-28T08:01:00Z')]
        self.assertEqual(result, expected_results)


    """
    TODO
    """


if __name__ == "__main__":
    unittest.main()
