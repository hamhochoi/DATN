import unittest
from language.api import *
import json


class TestAPI(unittest.TestCase):

    def test_api_get_all_datapoint(self):
        results = api_get_all_datapoint()
        expected_results = [{'time': '15:00:00-12-05-2019', 'DatapointId': 'humidity_homeassistant_datapoint', 'value': '64.0', 'DataType': 'float'}, {'time': '15:00:00-12-05-2019', 'DatapointId': 'humidity_openhab_datapoint', 'value': '63.0', 'DataType': 'float'}, {'time': '15:00:00-12-05-2019', 'DatapointId': 'humidity_thingsboard_datapoint', 'value': '65.0', 'DataType': 'float'}, {'time': '15:00:00-12-05-2019', 'DatapointId': 'light_homeassistant_datapoint', 'value': '0', 'DataType': 'int'}, {'time': '15:00:00-12-05-2019', 'DatapointId': 'light_openhab_datapoint', 'value': '0', 'DataType': 'int'}, {'time': '15:00:00-12-05-2019', 'DatapointId': 'light_thingsboard_datapoint', 'value': '0', 'DataType': 'int'}, {'time': '15:00:00-12-05-2019', 'DatapointId': 'motion_homeassistant_datapoint', 'value': '0', 'DataType': 'int'}, {'time': '15:00:00-12-05-2019', 'DatapointId': 'motion_openhab_datapoint', 'value': '0', 'DataType': 'int'}, {'time': '15:00:00-12-05-2019', 'DatapointId': 'motion_thingsboard_datapoint', 'value': '0', 'DataType': 'int'}, {'time': '15:00:00-12-05-2019', 'DatapointId': 'temperature_homeassistant_datapoint', 'value': '26.0', 'DataType': 'float'}, {'time': '15:00:00-12-05-2019', 'DatapointId': 'temperature_openhab_datapoint', 'value': '25.0', 'DataType': 'float'}, {'time': '15:00:00-12-05-2019', 'DatapointId': 'temperature_thingsboard_datapoint', 'value': '27.0', 'DataType': 'float'}]
        self.assertEqual(results, expected_results)


    def test_api_get_all_metric(self):
        results = api_get_all_metric()
        expected_results = [{'MetricId': 'humidity_homeassistant', 'MetricDomain': 'sensor', 'Unit': '', 'HasDatapoint': 'humidity_homeassistant_datapoint', 'MetricLocalId': 'humidity_metric_id', 'CanSetState': 'false', 'MetricType': 'gauge', 'MetricStatus': 'active', 'MetricName': 'humidity_phong_may_chu'}, {'MetricId': 'humidity_openhab', 'MetricDomain': 'sensor', 'Unit': '', 'HasDatapoint': 'humidity_openhab_datapoint', 'MetricLocalId': 'humidity_metric_id', 'CanSetState': 'false', 'MetricType': 'gauge', 'MetricStatus': 'active', 'MetricName': 'humidity_phong_sinh_vien'}, {'MetricId': 'humidity_thingsboard', 'MetricDomain': 'sensor', 'Unit': '', 'HasDatapoint': 'humidity_thingsboard_datapoint', 'MetricLocalId': 'humidity_metric_id', 'CanSetState': 'false', 'MetricType': 'gauge', 'MetricStatus': 'active', 'MetricName': 'humidity_phong_can_bo'}, {'MetricId': 'light_homeassistant', 'MetricDomain': 'sensor', 'Unit': '', 'HasDatapoint': 'light_homeassistant_datapoint', 'MetricLocalId': 'light_metric_id', 'CanSetState': 'false', 'MetricType': 'gauge', 'MetricStatus': 'active', 'MetricName': 'light_phong_may_chu'}, {'MetricId': 'light_openhab', 'MetricDomain': 'sensor', 'Unit': '', 'HasDatapoint': 'light_openhab_datapoint', 'MetricLocalId': 'light_metric_id', 'CanSetState': 'false', 'MetricType': 'gauge', 'MetricStatus': 'active', 'MetricName': 'light_phong_sinh_vien'}, {'MetricId': 'light_thingsboard', 'MetricDomain': 'sensor', 'Unit': '', 'HasDatapoint': 'light_thingsboard_datapoint', 'MetricLocalId': 'light_metric_id', 'CanSetState': 'false', 'MetricType': 'gauge', 'MetricStatus': 'active', 'MetricName': 'light_phong_can_bo'}, {'MetricId': 'motion_homeassistant', 'MetricDomain': 'sensor', 'Unit': '', 'HasDatapoint': 'motion_homeassistant_datapoint', 'MetricLocalId': 'motion_metric_id', 'CanSetState': 'false', 'MetricType': 'gauge', 'MetricStatus': 'active', 'MetricName': 'motion_phong_may_chu'}, {'MetricId': 'motion_openhab', 'MetricDomain': 'sensor', 'Unit': '', 'HasDatapoint': 'motion_openhab_datapoint', 'MetricLocalId': 'motion_metric_id', 'CanSetState': 'false', 'MetricType': 'gauge', 'MetricStatus': 'active', 'MetricName': 'motion_phong_sinh_vien'}, {'MetricId': 'motion_thingsboard', 'MetricDomain': 'sensor', 'Unit': '', 'HasDatapoint': 'motion_thingsboard_datapoint', 'MetricLocalId': 'motion_metric_id', 'CanSetState': 'false', 'MetricType': 'gauge', 'MetricStatus': 'active', 'MetricName': 'motion_phong_can_bo'}, {'MetricId': 'temperature_homeassistant', 'MetricDomain': 'sensor', 'Unit': '', 'HasDatapoint': 'temperature_homeassistant_datapoint', 'MetricLocalId': 'temperature_metric_id', 'CanSetState': 'false', 'MetricType': 'gauge', 'MetricStatus': 'active', 'MetricName': 'temperature_phong_may_chu'}, {'MetricId': 'temperature_openhab', 'MetricDomain': 'sensor', 'Unit': '', 'HasDatapoint': 'temperature_openhab_datapoint', 'MetricLocalId': 'temperature_metric_id', 'CanSetState': 'false', 'MetricType': 'gauge', 'MetricStatus': 'active', 'MetricName': 'temperature_phong_sinh_vien'}, {'MetricId': 'temperature_thingsboard', 'MetricDomain': 'sensor', 'Unit': '', 'HasDatapoint': 'temperature_thingsboard_datapoint', 'MetricLocalId': 'temperature_metric_id', 'CanSetState': 'false', 'MetricType': 'gauge', 'MetricStatus': 'active', 'MetricName': 'temperature_phong_can_bo'}]
        self.assertEqual(results, expected_results)


    def test_api_get_all_source(self):
        results = api_get_all_source()
        expected_results = [{'SourceStatus': 'active', 'Description': '', 'HasMetric': ['motion_homeassistant'], 'SourceId': 'motion_homeassistant', 'EndPoint': 'http://192.168.0.199:8123/source', 'Label': 'sensor', 'SourceType': 'thing', 'LocalId': 'motion_id'}, {'SourceStatus': 'active', 'Description': '', 'HasMetric': ['motion_openhab'], 'SourceId': 'motion_openhab', 'EndPoint': 'http://192.168.0.197:8080/source', 'Label': 'sensor', 'SourceType': 'thing', 'LocalId': 'motion_id'}, {'SourceStatus': 'active', 'Description': '', 'HasMetric': ['motion_thingsboard'], 'SourceId': 'motion_thingsboard', 'EndPoint': 'http://192.168.0.198:8080/source', 'Label': 'sensor', 'SourceType': 'thing', 'LocalId': 'motion_id'}, {'SourceStatus': 'active', 'Description': '', 'HasMetric': ['temperature_homeassistant', 'humidity_homeassistant', 'light_homeassistant'], 'SourceId': 'temperature-humidity-light_homeassistant', 'EndPoint': 'http://192.168.0.199:8123/source', 'Label': 'sensor', 'SourceType': 'thing', 'LocalId': 'temperature-humidity-light_id'}, {'SourceStatus': 'active', 'Description': '', 'HasMetric': ['temperature_openhab', 'humidity_openhab', 'light_openhab'], 'SourceId': 'temperature-humidity-light_openhab', 'EndPoint': 'http://192.168.0.197:8080/source', 'Label': 'sensor', 'SourceType': 'thing', 'LocalId': 'temperature-humidity-light_id'}, {'SourceStatus': 'active', 'Description': '', 'HasMetric': ['temperature_thingsboard', 'humidity_thingsboard', 'light_thingsboard'], 'SourceId': 'temperature-humidity-light_thingsboard', 'EndPoint': 'http://192.168.0.198:8080/source', 'Label': 'sensor', 'SourceType': 'thing', 'LocalId': 'temperature-humidity-light_id'}]
        self.assertEqual(results, expected_results)


    def test_api_get_all_platform(self):
        results = api_get_all_platform()
        expected_results = [{'PlatformStatus': 'active', 'PlatformPort': '8123', 'PlatformHost': 'http://192.168.0.199', 'PlatformType': '', 'HasSource': ['temperature-humidity-light_homeassistant', 'motion_homeassistant'], 'PlatformId': 'homeassistant_id', 'PlatformName': 'homeassistant'}, {'PlatformStatus': 'active', 'PlatformPort': '8080', 'PlatformHost': 'http://192.168.0.197', 'PlatformType': '', 'HasSource': ['temperature-humidity-light_openhab', 'motion_openhab'], 'PlatformId': 'openhab_id', 'PlatformName': 'openhab'}, {'PlatformStatus': 'active', 'PlatformPort': '8080', 'PlatformHost': 'http://192.168.0.198', 'PlatformType': '', 'HasSource': ['temperature-humidity-light_thingsboard', 'motion_thingsboard'], 'PlatformId': 'thingsboard_id', 'PlatformName': 'thingsboard'}]
        self.assertEqual(results, expected_results)


    def test_api_get_all_smartcontext(self):
        results = api_get_all_smartcontext()
        expected_results = [{'SmartContextName': 'HPCC', 'SubSmartContextId': ['phong_sinh_vien_id', 'phong_can_bo_id', 'phong_may_chu_id'], 'ParentSmartContextId': [], 'SmartContextId': 'HPCC_id', 'HasPlatform': []}, {'SmartContextName': 'phong_can_bo', 'SubSmartContextId': [], 'ParentSmartContextId': ['HPCC_id'], 'SmartContextId': 'phong_can_bo_id', 'HasPlatform': ['thingsboard_id']}, {'SmartContextName': 'phong_may_chu', 'SubSmartContextId': [], 'ParentSmartContextId': ['HPCC_id'], 'SmartContextId': 'phong_may_chu_id', 'HasPlatform': ['homeassistant_id']}, {'SmartContextName': 'phong_sinh_vien', 'SubSmartContextId': [], 'ParentSmartContextId': ['HPCC_id'], 'SmartContextId': 'phong_sinh_vien_id', 'HasPlatform': ['openhab_id']}]
        self.assertEqual(results, expected_results)


    def test_api_get_datapoint_from_datapoint_attr(self):
        results = api_get_datapoint_from_datapoint_attr('value', '25.0')
        expected_results = [{'time': '15:00:00-12-05-2019', 'value': '25.0', 'DatapointId': 'temperature_openhab_datapoint', 'DataType': 'float'}]
        self.assertEqual(results, expected_results)


    def test_api_get_metric_from_metric_attr(self):
        results = api_get_metric_from_metric_attr("MetricId", 'humidity_homeassistant')
        expected_results = [{'MetricType': 'gauge', 'CanSetState': 'false', 'HasDatapoint': 'humidity_homeassistant_datapoint', 'MetricStatus': 'active', 'Unit': '', 'MetricName': 'humidity_phong_may_chu', 'MetricDomain': 'sensor', 'MetricId': 'humidity_homeassistant', 'MetricLocalId': 'humidity_metric_id'}]
        self.assertEqual(results, expected_results)


    def test_api_get_source_from_source_attr(self):
        results = api_get_source_from_source_attr("SourceId", 'motion_openhab')
        expected_results = [{'HasMetric': ['motion_openhab'], 'LocalId': 'motion_id', 'EndPoint': 'http://192.168.0.197:8080/source', 'Description': '', 'SourceId': 'motion_openhab', 'SourceType': 'thing', 'Label': 'sensor', 'SourceStatus': 'active'}]
        self.assertEqual(results, expected_results)


    def test_api_get_smartcontext_from_smartcontext_attr(self):
        results = api_get_smartcontext_from_smartcontext_attr('SmartContextName', 'phong_sinh_vien')
        expected_results = [{'HasPlatform': ['openhab_id'], 'SmartContextName': 'phong_sinh_vien', 'SmartContextId': 'phong_sinh_vien_id', 'ParentSmartContextId': ['HPCC_id'], 'SubSmartContextId': []}]
        self.assertEqual(results, expected_results)


    def test_api_get_datapoint_id_from_datapoint_attribute(self):
        results = api_get_datapoint_id_from_datapoint_attribute('DatapointId', 'humidity_homeassistant_datapoint')
        expected_results = ['humidity_homeassistant_datapoint']
        self.assertEqual(results, expected_results)


    def test_api_get_metric_id_from_metric_attribute(self):
        results = api_get_metric_id_from_metric_attribute('MetricName', 'temperature_phong_may_chu')
        expected_results = ['temperature_homeassistant']
        self.assertEqual(results, expected_results)


    def test_api_get_source_id_from_source_attribute(self):
        results = api_get_source_id_from_source_attribute('SourceStatus', 'active')
        expected_results = ['motion_homeassistant', 'motion_openhab', 'motion_thingsboard', 'temperature-humidity-light_homeassistant', 'temperature-humidity-light_openhab', 'temperature-humidity-light_thingsboard']
        self.assertEqual(results, expected_results)


    def test_api_get_platform_id_from_platform_attribute(self):
        results = api_get_platform_id_from_platform_attribute('PlatformPort', '8080')
        expected_results = ['openhab_id', 'thingsboard_id']
        self.assertEqual(results, expected_results)


    def test_api_get_smartcontext_id_from_smartcontext_attribute(self):
        results = api_get_smartcontext_id_from_smartcontext_attribute('SmartContextName', 'HPCC')
        expected_results = ['HPCC_id']
        self.assertEqual(results, expected_results)

    
    def test_api_get_datapoint_from_metric(self):
        results = api_get_datapoint_from_metric("MetricId", 'humidity_thingsboard')
        expected_results = [{'value': '65.0', 'time': '15:00:00-12-05-2019', 'DatapointId': 'humidity_thingsboard_datapoint', 'DataType': 'float'}]
        self.assertEqual(results, expected_results)


    def test_api_get_metric_from_datapoint(self):
        results = api_get_metric_from_datapoint('DataType', 'float')
        expected_results = [{'Unit': '', 'MetricStatus': 'active', 'CanSetState': 'false', 'MetricDomain': 'sensor', 'HasDatapoint': 'humidity_homeassistant_datapoint', 'MetricId': 'humidity_homeassistant', 'MetricName': 'humidity_phong_may_chu', 'MetricLocalId': 'humidity_metric_id', 'MetricType': 'gauge'}, {'Unit': '', 'MetricStatus': 'active', 'CanSetState': 'false', 'MetricDomain': 'sensor', 'HasDatapoint': 'humidity_openhab_datapoint', 'MetricId': 'humidity_openhab', 'MetricName': 'humidity_phong_sinh_vien', 'MetricLocalId': 'humidity_metric_id', 'MetricType': 'gauge'}, {'Unit': '', 'MetricStatus': 'active', 'CanSetState': 'false', 'MetricDomain': 'sensor', 'HasDatapoint': 'humidity_thingsboard_datapoint', 'MetricId': 'humidity_thingsboard', 'MetricName': 'humidity_phong_can_bo', 'MetricLocalId': 'humidity_metric_id', 'MetricType': 'gauge'}, {'Unit': '', 'MetricStatus': 'active', 'CanSetState': 'false', 'MetricDomain': 'sensor', 'HasDatapoint': 'temperature_homeassistant_datapoint', 'MetricId': 'temperature_homeassistant', 'MetricName': 'temperature_phong_may_chu', 'MetricLocalId': 'temperature_metric_id', 'MetricType': 'gauge'}, {'Unit': '', 'MetricStatus': 'active', 'CanSetState': 'false', 'MetricDomain': 'sensor', 'HasDatapoint': 'temperature_openhab_datapoint', 'MetricId': 'temperature_openhab', 'MetricName': 'temperature_phong_sinh_vien', 'MetricLocalId': 'temperature_metric_id', 'MetricType': 'gauge'}, {'Unit': '', 'MetricStatus': 'active', 'CanSetState': 'false', 'MetricDomain': 'sensor', 'HasDatapoint': 'temperature_thingsboard_datapoint', 'MetricId': 'temperature_thingsboard', 'MetricName': 'temperature_phong_can_bo', 'MetricLocalId': 'temperature_metric_id', 'MetricType': 'gauge'}]
        self.assertEqual(results, expected_results)


    def test_api_get_metric_from_source(self):
        results = api_get_metric_from_source('SourceType', 'thing')
        expected_results = [{'MetricStatus': 'active', 'CanSetState': 'false', 'HasDatapoint': 'motion_homeassistant_datapoint', 'MetricId': 'motion_homeassistant', 'MetricDomain': 'sensor', 'MetricType': 'gauge', 'Unit': '', 'MetricLocalId': 'motion_metric_id', 'MetricName': 'motion_phong_may_chu'}, {'MetricStatus': 'active', 'CanSetState': 'false', 'HasDatapoint': 'motion_openhab_datapoint', 'MetricId': 'motion_openhab', 'MetricDomain': 'sensor', 'MetricType': 'gauge', 'Unit': '', 'MetricLocalId': 'motion_metric_id', 'MetricName': 'motion_phong_sinh_vien'}, {'MetricStatus': 'active', 'CanSetState': 'false', 'HasDatapoint': 'motion_thingsboard_datapoint', 'MetricId': 'motion_thingsboard', 'MetricDomain': 'sensor', 'MetricType': 'gauge', 'Unit': '', 'MetricLocalId': 'motion_metric_id', 'MetricName': 'motion_phong_can_bo'}, {'MetricStatus': 'active', 'CanSetState': 'false', 'HasDatapoint': 'temperature_homeassistant_datapoint', 'MetricId': 'temperature_homeassistant', 'MetricDomain': 'sensor', 'MetricType': 'gauge', 'Unit': '', 'MetricLocalId': 'temperature_metric_id', 'MetricName': 'temperature_phong_may_chu'}, {'MetricStatus': 'active', 'CanSetState': 'false', 'HasDatapoint': 'humidity_homeassistant_datapoint', 'MetricId': 'humidity_homeassistant', 'MetricDomain': 'sensor', 'MetricType': 'gauge', 'Unit': '', 'MetricLocalId': 'humidity_metric_id', 'MetricName': 'humidity_phong_may_chu'}, {'MetricStatus': 'active', 'CanSetState': 'false', 'HasDatapoint': 'light_homeassistant_datapoint', 'MetricId': 'light_homeassistant', 'MetricDomain': 'sensor', 'MetricType': 'gauge', 'Unit': '', 'MetricLocalId': 'light_metric_id', 'MetricName': 'light_phong_may_chu'}, {'MetricStatus': 'active', 'CanSetState': 'false', 'HasDatapoint': 'temperature_openhab_datapoint', 'MetricId': 'temperature_openhab', 'MetricDomain': 'sensor', 'MetricType': 'gauge', 'Unit': '', 'MetricLocalId': 'temperature_metric_id', 'MetricName': 'temperature_phong_sinh_vien'}, {'MetricStatus': 'active', 'CanSetState': 'false', 'HasDatapoint': 'humidity_openhab_datapoint', 'MetricId': 'humidity_openhab', 'MetricDomain': 'sensor', 'MetricType': 'gauge', 'Unit': '', 'MetricLocalId': 'humidity_metric_id', 'MetricName': 'humidity_phong_sinh_vien'}, {'MetricStatus': 'active', 'CanSetState': 'false', 'HasDatapoint': 'light_openhab_datapoint', 'MetricId': 'light_openhab', 'MetricDomain': 'sensor', 'MetricType': 'gauge', 'Unit': '', 'MetricLocalId': 'light_metric_id', 'MetricName': 'light_phong_sinh_vien'}, {'MetricStatus': 'active', 'CanSetState': 'false', 'HasDatapoint': 'temperature_thingsboard_datapoint', 'MetricId': 'temperature_thingsboard', 'MetricDomain': 'sensor', 'MetricType': 'gauge', 'Unit': '', 'MetricLocalId': 'temperature_metric_id', 'MetricName': 'temperature_phong_can_bo'}, {'MetricStatus': 'active', 'CanSetState': 'false', 'HasDatapoint': 'humidity_thingsboard_datapoint', 'MetricId': 'humidity_thingsboard', 'MetricDomain': 'sensor', 'MetricType': 'gauge', 'Unit': '', 'MetricLocalId': 'humidity_metric_id', 'MetricName': 'humidity_phong_can_bo'}, {'MetricStatus': 'active', 'CanSetState': 'false', 'HasDatapoint': 'light_thingsboard_datapoint', 'MetricId': 'light_thingsboard', 'MetricDomain': 'sensor', 'MetricType': 'gauge', 'Unit': '', 'MetricLocalId': 'light_metric_id', 'MetricName': 'light_phong_can_bo'}]
        self.assertEqual(results, expected_results)


    def test_api_get_source_from_metric(self):
        results = api_get_source_from_metric("MetricId", 'humidity_homeassistant')
        expected_results = [{'SourceType': 'thing', 'SourceId': 'temperature-humidity-light_homeassistant', 'Description': '', 'EndPoint': 'http://192.168.0.199:8123/source', 'HasMetric': ['temperature_homeassistant', 'humidity_homeassistant', 'light_homeassistant'], 'LocalId': 'temperature-humidity-light_id', 'Label': 'sensor', 'SourceStatus': 'active'}]
        self.assertEqual(results, expected_results)


    def test_api_get_source_from_platform(self):
        results = api_get_source_from_platform('PlatformPort', "8080")
        expected_results = [{'SourceStatus': 'active', 'SourceId': 'temperature-humidity-light_openhab', 'HasMetric': ['temperature_openhab', 'humidity_openhab', 'light_openhab'], 'Label': 'sensor', 'EndPoint': 'http://192.168.0.197:8080/source', 'Description': '', 'SourceType': 'thing', 'LocalId': 'temperature-humidity-light_id'}, {'SourceStatus': 'active', 'SourceId': 'motion_openhab', 'HasMetric': ['motion_openhab'], 'Label': 'sensor', 'EndPoint': 'http://192.168.0.197:8080/source', 'Description': '', 'SourceType': 'thing', 'LocalId': 'motion_id'}, {'SourceStatus': 'active', 'SourceId': 'temperature-humidity-light_thingsboard', 'HasMetric': ['temperature_thingsboard', 'humidity_thingsboard', 'light_thingsboard'], 'Label': 'sensor', 'EndPoint': 'http://192.168.0.198:8080/source', 'Description': '', 'SourceType': 'thing', 'LocalId': 'temperature-humidity-light_id'}, {'SourceStatus': 'active', 'SourceId': 'motion_thingsboard', 'HasMetric': ['motion_thingsboard'], 'Label': 'sensor', 'EndPoint': 'http://192.168.0.198:8080/source', 'Description': '', 'SourceType': 'thing', 'LocalId': 'motion_id'}]
        self.assertEqual(results, expected_results)


    def test_api_get_platform_from_source(self):
        results = api_get_platform_from_source('SourceType', 'thing')
        expected_results = [{u'PlatformPort': u'8123', u'PlatformStatus': u'active', u'PlatformId': u'homeassistant_id', u'HasSource': [u'temperature-humidity-light_homeassistant', u'motion_homeassistant'], u'PlatformHost': u'http://192.168.0.199', u'PlatformName': u'homeassistant', u'PlatformType': u''}, {u'PlatformPort': u'8080', u'PlatformStatus': u'active', u'PlatformId': u'thingsboard_id', u'HasSource': [u'temperature-humidity-light_thingsboard', u'motion_thingsboard'], u'PlatformHost': u'http://192.168.0.198', u'PlatformName': u'thingsboard', u'PlatformType': u''}, {u'PlatformPort': u'8080', u'PlatformStatus': u'active', u'PlatformId': u'openhab_id', u'HasSource': [u'temperature-humidity-light_openhab', u'motion_openhab'], u'PlatformHost': u'http://192.168.0.197', u'PlatformName': u'openhab', u'PlatformType': u''}]
        self.assertEqual(results, expected_results)


    def test_api_get_platform_from_smartcontext(self):
        results = api_get_platform_from_smartcontext('SmartContextName', 'HPCC')
        expected_results = [{u'PlatformPort': u'8080', u'PlatformStatus': u'active', u'PlatformId': u'openhab_id', u'HasSource': [u'temperature-humidity-light_openhab', u'motion_openhab'], u'PlatformHost': u'http://192.168.0.197', u'PlatformName': u'openhab', u'PlatformType': u''}, {u'PlatformPort': u'8080', u'PlatformStatus': u'active', u'PlatformId': u'thingsboard_id', u'HasSource': [u'temperature-humidity-light_thingsboard', u'motion_thingsboard'], u'PlatformHost': u'http://192.168.0.198', u'PlatformName': u'thingsboard', u'PlatformType': u''}, {u'PlatformPort': u'8123', u'PlatformStatus': u'active', u'PlatformId': u'homeassistant_id', u'HasSource': [u'temperature-humidity-light_homeassistant', u'motion_homeassistant'], u'PlatformHost': u'http://192.168.0.199', u'PlatformName': u'homeassistant', u'PlatformType': u''}]
        self.assertEqual(results, expected_results)


    def test_api_get_smartcontext_from_platform(self):
        results = api_get_smartcontext_from_platform('PlatformPort', "8123")
        expected_results = [{u'SubSmartContextId': [], u'SmartContextId': u'phong_may_chu_id', u'HasPlatform': [u'homeassistant_id'], u'ParentSmartContextId': [u'HPCC_id'], u'SmartContextName': u'phong_may_chu'}, {u'SubSmartContextId': [u'phong_sinh_vien_id', u'phong_can_bo_id', u'phong_may_chu_id'], u'SmartContextId': u'HPCC_id', u'HasPlatform': [], u'ParentSmartContextId': [], u'SmartContextName': u'HPCC'}]
        self.assertEqual(results, expected_results)


    def test_api_get_smartcontext_from_platform(self):
        results = api_get_sub_smartcontext_from_parent_smartcontext('HPCC_id')
        expected_results = [{u'SubSmartContextId': [], u'SmartContextId': u'phong_sinh_vien_id', u'HasPlatform': [u'openhab_id'], u'ParentSmartContextId': [u'HPCC_id'], u'SmartContextName': u'phong_sinh_vien'}, {u'SubSmartContextId': [], u'SmartContextId': u'phong_can_bo_id', u'HasPlatform': [u'thingsboard_id'], u'ParentSmartContextId': [u'HPCC_id'], u'SmartContextName': u'phong_can_bo'}, {u'SubSmartContextId': [], u'SmartContextId': u'phong_may_chu_id', u'HasPlatform': [u'homeassistant_id'], u'ParentSmartContextId': [u'HPCC_id'], u'SmartContextName': u'phong_may_chu'}]
        self.assertEqual(results, expected_results)


    def test_api_get_parent_smartcontext_from_sub_smartcontext(self):
        results = api_get_parent_smartcontext_from_sub_smartcontext('phong_sinh_vien_id')
        expected_results = [{u'SubSmartContextId': [u'phong_sinh_vien_id', u'phong_can_bo_id', u'phong_may_chu_id'], u'SmartContextId': u'HPCC_id', u'HasPlatform': [], u'ParentSmartContextId': [], u'SmartContextName': u'HPCC'}]
        self.assertEqual(results, expected_results)


    def test_api_get_datapoint_from_source(self):
        results = api_get_datapoint_from_source('SourceStatus', 'active')
        expected_results = [{u'DataType': u'int', u'DatapointId': u'motion_homeassistant_datapoint', u'value': u'0', u'time': u'15:00:00-12-05-2019'}, {u'DataType': u'int', u'DatapointId': u'motion_openhab_datapoint', u'value': u'0', u'time': u'15:00:00-12-05-2019'}, {u'DataType': u'int', u'DatapointId': u'motion_thingsboard_datapoint', u'value': u'0', u'time': u'15:00:00-12-05-2019'}, {u'DataType': u'float', u'DatapointId': u'temperature_homeassistant_datapoint', u'value': u'26.0', u'time': u'15:00:00-12-05-2019'}, {u'DataType': u'float', u'DatapointId': u'humidity_homeassistant_datapoint', u'value': u'64.0', u'time': u'15:00:00-12-05-2019'}, {u'DataType': u'int', u'DatapointId': u'light_homeassistant_datapoint', u'value': u'0', u'time': u'15:00:00-12-05-2019'}, {u'DataType': u'float', u'DatapointId': u'temperature_openhab_datapoint', u'value': u'25.0', u'time': u'15:00:00-12-05-2019'}, {u'DataType': u'float', u'DatapointId': u'humidity_openhab_datapoint', u'value': u'63.0', u'time': u'15:00:00-12-05-2019'}, {u'DataType': u'int', u'DatapointId': u'light_openhab_datapoint', u'value': u'0', u'time': u'15:00:00-12-05-2019'}, {u'DataType': u'float', u'DatapointId': u'temperature_thingsboard_datapoint', u'value': u'27.0', u'time': u'15:00:00-12-05-2019'}, {u'DataType': u'float', u'DatapointId': u'humidity_thingsboard_datapoint', u'value': u'65.0', u'time': u'15:00:00-12-05-2019'}, {u'DataType': u'int', u'DatapointId': u'light_thingsboard_datapoint', u'value': u'0', u'time': u'15:00:00-12-05-2019'}]
        self.assertEqual(results, expected_results)


    def test_api_get_datapoint_from_platform(self):
        results = api_get_datapoint_from_platform('PlatformPort', "8080")
        expected_results = [{u'DataType': u'float', u'DatapointId': u'temperature_openhab_datapoint', u'value': u'25.0', u'time': u'15:00:00-12-05-2019'}, {u'DataType': u'float', u'DatapointId': u'humidity_openhab_datapoint', u'value': u'63.0', u'time': u'15:00:00-12-05-2019'}, {u'DataType': u'int', u'DatapointId': u'light_openhab_datapoint', u'value': u'0', u'time': u'15:00:00-12-05-2019'}, {u'DataType': u'int', u'DatapointId': u'motion_openhab_datapoint', u'value': u'0', u'time': u'15:00:00-12-05-2019'}, {u'DataType': u'float', u'DatapointId': u'temperature_thingsboard_datapoint', u'value': u'27.0', u'time': u'15:00:00-12-05-2019'}, {u'DataType': u'float', u'DatapointId': u'humidity_thingsboard_datapoint', u'value': u'65.0', u'time': u'15:00:00-12-05-2019'}, {u'DataType': u'int', u'DatapointId': u'light_thingsboard_datapoint', u'value': u'0', u'time': u'15:00:00-12-05-2019'}, {u'DataType': u'int', u'DatapointId': u'motion_thingsboard_datapoint', u'value': u'0', u'time': u'15:00:00-12-05-2019'}]
        self.assertEqual(results, expected_results)


    def test_api_get_datapoint_from_platform(self):
        results = api_get_datapoint_from_smartcontext("SmartContextId", 'phong_can_bo_id')
        expected_results = [{u'DataType': u'float', u'DatapointId': u'temperature_thingsboard_datapoint', u'value': u'27.0', u'time': u'15:00:00-12-05-2019'}, {u'DataType': u'float', u'DatapointId': u'humidity_thingsboard_datapoint', u'value': u'65.0', u'time': u'15:00:00-12-05-2019'}, {u'DataType': u'int', u'DatapointId': u'light_thingsboard_datapoint', u'value': u'0', u'time': u'15:00:00-12-05-2019'}, {u'DataType': u'int', u'DatapointId': u'motion_thingsboard_datapoint', u'value': u'0', u'time': u'15:00:00-12-05-2019'}]
        self.assertEqual(results, expected_results)


    def test_api_get_metric_from_platform(self):
        results = api_get_metric_from_platform('PlatformPort', "8080")
        expected_results = [{u'MetricLocalId': u'temperature_metric_id', u'MetricStatus': u'active', u'MetricId': u'temperature_openhab', u'MetricType': u'gauge', u'HasDatapoint': u'temperature_openhab_datapoint', u'CanSetState': u'false', u'MetricDomain': u'sensor', u'Unit': u'', u'MetricName': u'temperature_phong_sinh_vien'}, {u'MetricLocalId': u'humidity_metric_id', u'MetricStatus': u'active', u'MetricId': u'humidity_openhab', u'MetricType': u'gauge', u'HasDatapoint': u'humidity_openhab_datapoint', u'CanSetState': u'false', u'MetricDomain': u'sensor', u'Unit': u'', u'MetricName': u'humidity_phong_sinh_vien'}, {u'MetricLocalId': u'light_metric_id', u'MetricStatus': u'active', u'MetricId': u'light_openhab', u'MetricType': u'gauge', u'HasDatapoint': u'light_openhab_datapoint', u'CanSetState': u'false', u'MetricDomain': u'sensor', u'Unit': u'', u'MetricName': u'light_phong_sinh_vien'}, {u'MetricLocalId': u'motion_metric_id', u'MetricStatus': u'active', u'MetricId': u'motion_openhab', u'MetricType': u'gauge', u'HasDatapoint': u'motion_openhab_datapoint', u'CanSetState': u'false', u'MetricDomain': u'sensor', u'Unit': u'', u'MetricName': u'motion_phong_sinh_vien'}, {u'MetricLocalId': u'temperature_metric_id', u'MetricStatus': u'active', u'MetricId': u'temperature_thingsboard', u'MetricType': u'gauge', u'HasDatapoint': u'temperature_thingsboard_datapoint', u'CanSetState': u'false', u'MetricDomain': u'sensor', u'Unit': u'', u'MetricName': u'temperature_phong_can_bo'}, {u'MetricLocalId': u'humidity_metric_id', u'MetricStatus': u'active', u'MetricId': u'humidity_thingsboard', u'MetricType': u'gauge', u'HasDatapoint': u'humidity_thingsboard_datapoint', u'CanSetState': u'false', u'MetricDomain': u'sensor', u'Unit': u'', u'MetricName': u'humidity_phong_can_bo'}, {u'MetricLocalId': u'light_metric_id', u'MetricStatus': u'active', u'MetricId': u'light_thingsboard', u'MetricType': u'gauge', u'HasDatapoint': u'light_thingsboard_datapoint', u'CanSetState': u'false', u'MetricDomain': u'sensor', u'Unit': u'', u'MetricName': u'light_phong_can_bo'}, {u'MetricLocalId': u'motion_metric_id', u'MetricStatus': u'active', u'MetricId': u'motion_thingsboard', u'MetricType': u'gauge', u'HasDatapoint': u'motion_thingsboard_datapoint', u'CanSetState': u'false', u'MetricDomain': u'sensor', u'Unit': u'', u'MetricName': u'motion_phong_can_bo'}]
        self.assertEqual(results, expected_results)


    def test_api_get_metric_from_platform(self):
        results = api_get_metric_from_smartcontext("SmartContextId", 'HPCC_id')
        expected_results = [{u'MetricLocalId': u'temperature_metric_id', u'MetricStatus': u'active', u'MetricId': u'temperature_openhab', u'MetricType': u'gauge', u'HasDatapoint': u'temperature_openhab_datapoint', u'CanSetState': u'false', u'MetricDomain': u'sensor', u'Unit': u'', u'MetricName': u'temperature_phong_sinh_vien'}, {u'MetricLocalId': u'humidity_metric_id', u'MetricStatus': u'active', u'MetricId': u'humidity_openhab', u'MetricType': u'gauge', u'HasDatapoint': u'humidity_openhab_datapoint', u'CanSetState': u'false', u'MetricDomain': u'sensor', u'Unit': u'', u'MetricName': u'humidity_phong_sinh_vien'}, {u'MetricLocalId': u'light_metric_id', u'MetricStatus': u'active', u'MetricId': u'light_openhab', u'MetricType': u'gauge', u'HasDatapoint': u'light_openhab_datapoint', u'CanSetState': u'false', u'MetricDomain': u'sensor', u'Unit': u'', u'MetricName': u'light_phong_sinh_vien'}, {u'MetricLocalId': u'motion_metric_id', u'MetricStatus': u'active', u'MetricId': u'motion_openhab', u'MetricType': u'gauge', u'HasDatapoint': u'motion_openhab_datapoint', u'CanSetState': u'false', u'MetricDomain': u'sensor', u'Unit': u'', u'MetricName': u'motion_phong_sinh_vien'}, {u'MetricLocalId': u'temperature_metric_id', u'MetricStatus': u'active', u'MetricId': u'temperature_thingsboard', u'MetricType': u'gauge', u'HasDatapoint': u'temperature_thingsboard_datapoint', u'CanSetState': u'false', u'MetricDomain': u'sensor', u'Unit': u'', u'MetricName': u'temperature_phong_can_bo'}, {u'MetricLocalId': u'humidity_metric_id', u'MetricStatus': u'active', u'MetricId': u'humidity_thingsboard', u'MetricType': u'gauge', u'HasDatapoint': u'humidity_thingsboard_datapoint', u'CanSetState': u'false', u'MetricDomain': u'sensor', u'Unit': u'', u'MetricName': u'humidity_phong_can_bo'}, {u'MetricLocalId': u'light_metric_id', u'MetricStatus': u'active', u'MetricId': u'light_thingsboard', u'MetricType': u'gauge', u'HasDatapoint': u'light_thingsboard_datapoint', u'CanSetState': u'false', u'MetricDomain': u'sensor', u'Unit': u'', u'MetricName': u'light_phong_can_bo'}, {u'MetricLocalId': u'motion_metric_id', u'MetricStatus': u'active', u'MetricId': u'motion_thingsboard', u'MetricType': u'gauge', u'HasDatapoint': u'motion_thingsboard_datapoint', u'CanSetState': u'false', u'MetricDomain': u'sensor', u'Unit': u'', u'MetricName': u'motion_phong_can_bo'}, {u'MetricLocalId': u'temperature_metric_id', u'MetricStatus': u'active', u'MetricId': u'temperature_homeassistant', u'MetricType': u'gauge', u'HasDatapoint': u'temperature_homeassistant_datapoint', u'CanSetState': u'false', u'MetricDomain': u'sensor', u'Unit': u'', u'MetricName': u'temperature_phong_may_chu'}, {u'MetricLocalId': u'humidity_metric_id', u'MetricStatus': u'active', u'MetricId': u'humidity_homeassistant', u'MetricType': u'gauge', u'HasDatapoint': u'humidity_homeassistant_datapoint', u'CanSetState': u'false', u'MetricDomain': u'sensor', u'Unit': u'', u'MetricName': u'humidity_phong_may_chu'}, {u'MetricLocalId': u'light_metric_id', u'MetricStatus': u'active', u'MetricId': u'light_homeassistant', u'MetricType': u'gauge', u'HasDatapoint': u'light_homeassistant_datapoint', u'CanSetState': u'false', u'MetricDomain': u'sensor', u'Unit': u'', u'MetricName': u'light_phong_may_chu'}, {u'MetricLocalId': u'motion_metric_id', u'MetricStatus': u'active', u'MetricId': u'motion_homeassistant', u'MetricType': u'gauge', u'HasDatapoint': u'motion_homeassistant_datapoint', u'CanSetState': u'false', u'MetricDomain': u'sensor', u'Unit': u'', u'MetricName': u'motion_phong_may_chu'}]
        self.assertEqual(results, expected_results)


    def test_api_get_source_from_smartcontext(self):
        results = api_get_source_from_smartcontext('SmartContextName', 'phong_sinh_vien')
        expected_results = [{u'EndPoint': u'http://192.168.0.197:8080/source', u'Description': u'', u'SourceId': u'temperature-humidity-light_openhab', u'LocalId': u'temperature-humidity-light_id', u'HasMetric': [u'temperature_openhab', u'humidity_openhab', u'light_openhab'], u'Label': u'sensor', u'SourceStatus': u'active', u'SourceType': u'thing'}, {u'EndPoint': u'http://192.168.0.197:8080/source', u'Description': u'', u'SourceId': u'motion_openhab', u'LocalId': u'motion_id', u'HasMetric': [u'motion_openhab'], u'Label': u'sensor', u'SourceStatus': u'active', u'SourceType': u'thing'}]
        self.assertEqual(results, expected_results)


    def test_api_get_source_from_datapoint(self):
        results = api_get_source_from_datapoint('value', '64.0')
        expected_results = [{u'EndPoint': u'http://192.168.0.199:8123/source', u'Description': u'', u'SourceId': u'temperature-humidity-light_homeassistant', u'LocalId': u'temperature-humidity-light_id', u'HasMetric': [u'temperature_homeassistant', u'humidity_homeassistant', u'light_homeassistant'], u'Label': u'sensor', u'SourceStatus': u'active', u'SourceType': u'thing'}]
        self.assertEqual(results, expected_results)


    def test_api_get_platform_from_metric(self):
        results = api_get_platform_from_metric("MetricId", 'light_openhab')
        expected_results = [{u'PlatformPort': u'8080', u'PlatformStatus': u'active', u'PlatformId': u'openhab_id', u'HasSource': [u'temperature-humidity-light_openhab', u'motion_openhab'], u'PlatformHost': u'http://192.168.0.197', u'PlatformName': u'openhab', u'PlatformType': u''}]
        self.assertEqual(results, expected_results)


    def test_api_get_smartcontext_from_source(self):
        results = api_get_smartcontext_from_source('SourceStatus', 'active')
        expected_results = [{u'SubSmartContextId': [], u'SmartContextId': u'phong_can_bo_id', u'HasPlatform': [u'thingsboard_id'], u'ParentSmartContextId': [u'HPCC_id'], u'SmartContextName': u'phong_can_bo'}, {u'SubSmartContextId': [], u'SmartContextId': u'phong_may_chu_id', u'HasPlatform': [u'homeassistant_id'], u'ParentSmartContextId': [u'HPCC_id'], u'SmartContextName': u'phong_may_chu'}, {u'SubSmartContextId': [], u'SmartContextId': u'phong_sinh_vien_id', u'HasPlatform': [u'openhab_id'], u'ParentSmartContextId': [u'HPCC_id'], u'SmartContextName': u'phong_sinh_vien'}, {u'SubSmartContextId': [u'phong_sinh_vien_id', u'phong_can_bo_id', u'phong_may_chu_id'], u'SmartContextId': u'HPCC_id', u'HasPlatform': [], u'ParentSmartContextId': [], u'SmartContextName': u'HPCC'}]
        self.assertEqual(results, expected_results)


    def test_api_get_smartcontext_from_metric(self):
        results = api_get_smartcontext_from_metric("MetricId", 'humidity_thingsboard')
        expected_results = [{u'SubSmartContextId': [], u'SmartContextId': u'phong_can_bo_id', u'HasPlatform': [u'thingsboard_id'], u'ParentSmartContextId': [u'HPCC_id'], u'SmartContextName': u'phong_can_bo'}, {u'SubSmartContextId': [u'phong_sinh_vien_id', u'phong_can_bo_id', u'phong_may_chu_id'], u'SmartContextId': u'HPCC_id', u'HasPlatform': [], u'ParentSmartContextId': [], u'SmartContextName': u'HPCC'}]
        self.assertEqual(results, expected_results)


    def test_api_get_smartcontext_from_datapoint(self):
        results = api_get_smartcontext_from_datapoint('DataType', 'int')
        expected_results = [{u'SubSmartContextId': [], u'SmartContextId': u'phong_can_bo_id', u'HasPlatform': [u'thingsboard_id'], u'ParentSmartContextId': [u'HPCC_id'], u'SmartContextName': u'phong_can_bo'}, {u'SubSmartContextId': [], u'SmartContextId': u'phong_may_chu_id', u'HasPlatform': [u'homeassistant_id'], u'ParentSmartContextId': [u'HPCC_id'], u'SmartContextName': u'phong_may_chu'}, {u'SubSmartContextId': [], u'SmartContextId': u'phong_sinh_vien_id', u'HasPlatform': [u'openhab_id'], u'ParentSmartContextId': [u'HPCC_id'], u'SmartContextName': u'phong_sinh_vien'}, {u'SubSmartContextId': [u'phong_sinh_vien_id', u'phong_can_bo_id', u'phong_may_chu_id'], u'SmartContextId': u'HPCC_id', u'HasPlatform': [], u'ParentSmartContextId': [], u'SmartContextName': u'HPCC'}]
        self.assertEqual(results, expected_results)







if __name__ == "__main__":
    unittest.main()
