import unittest
from language.api import *
import json


class TestAPI(unittest.TestCase):
    def test_api_get_datapoint_from_metric(self):
        metric_id = "metric_id_1"
        result = api_get_datapoint_from_metric(metric_id)

        self.assertEqual(str(result[0]), "{u'DataType': u'int', u'value': 32, u'time': u'2018-03-28T08:01:00Z'}")


    def test_api_get_metric_from_source(self):
        source_id = 'source_id_1'
        results = api_get_metric_from_source(source_id)

        self.assertEqual(str(results[0]), "('metric_id_1', 'source_id_1', 'Temperature', 'Gauge', '*C', 'sensor', 'active', 'metric_local_id')")





if __name__ == "__main__":
    unittest.main()
