import MySQLdb
from influxdb import InfluxDBClient
import traceback
import numpy as np
import os
import json
from Fog.Filter.Filter import Filter
import time



datapoint_folder    = "/media/hamhochoi/Beo/OneDrive for Business 1/OneDrive - student.hust.edu.vn/OD/20182/DATN/data/datapoint"
metric_folder       = "/media/hamhochoi/Beo/OneDrive for Business 1/OneDrive - student.hust.edu.vn/OD/20182/DATN/data/metric"
source_folder       = "/media/hamhochoi/Beo/OneDrive for Business 1/OneDrive - student.hust.edu.vn/OD/20182/DATN/data/source"
platform_folder     = "/media/hamhochoi/Beo/OneDrive for Business 1/OneDrive - student.hust.edu.vn/OD/20182/DATN/data/platform"
smartcontext_folder = "/media/hamhochoi/Beo/OneDrive for Business 1/OneDrive - student.hust.edu.vn/OD/20182/DATN/data/smartcontext"
filter_ = Filter(broker_fog="broker.hivemq.com")



###########################################################
# BASE API

def api_get_datapoint_id_from_datapoint_attribute(datapoint_attribute, datapoint_value):
    datapoints = api_get_all_datapoint()
    datapoint_ids = []

    for datapoint in datapoints:
        if (datapoint[datapoint_attribute] == datapoint_value):
            datapoint_id = datapoint["DatapointId"]
            datapoint_ids.append(datapoint_id)

    return datapoint_ids


def api_get_metric_id_from_metric_attribute(metric_attribute, metric_value):
    metrics = api_get_all_metric()
    metric_ids = []

    for metric in metrics:
        if (metric[metric_attribute] == metric_value):
            metric_id = metric["MetricId"]
            metric_ids.append(metric_id)

    return metric_ids


def api_get_source_id_from_source_attribute(source_attribute, source_value):
    sources = api_get_all_source()
    source_ids = []

    for source in sources:
        if (source[source_attribute] == source_value):
            source_id = source["SourceId"]
            source_ids.append(source_id)

    return source_ids


def api_get_platform_id_from_platform_attribute(platform_attribute, platform_value):
    platforms = api_get_all_platform()
    platform_ids = []

    for platform in platforms:
        if (platform[platform_attribute] == platform_value):
            platform_id = platform["PlatformId"]
            platform_ids.append(platform_id)

    return platform_ids


def api_get_smartcontext_id_from_smartcontext_attribute(smartcontext_attribute, smartcontext_value):
    smartcontexts = api_get_all_smartcontext()
    smartcontext_ids = []

    for smartcontext in smartcontexts:
        if (smartcontext[smartcontext_attribute] == smartcontext_value):
            smartcontext_id = smartcontext["SmartContextId"]
            smartcontext_ids.append(smartcontext_id)

    return smartcontext_ids


###################################################
# GET DATAPOINT

def api_get_all_datapoint():
    filter_.api_get_state()
    time.sleep(2)

    datapoints = []

    datapoint_paths = [os.path.join(datapoint_folder, datapoint_id) for datapoint_id in os.listdir(datapoint_folder)]
    for datapoint_path in datapoint_paths:
        f_datapoint = open(datapoint_path, 'r')
        datapoint = json.load(f_datapoint)
        datapoints.append(datapoint)
        # datapoints.append(json.dumps(datapoint))

    return datapoints


def api_get_datapoint_from_datapoint_attr(datapoint_attr, datapoint_value):
    datapoints = api_get_all_datapoint()
    return_datapoints = []

    for datapoint in datapoints:
        if (str(datapoint[datapoint_attr]) == str(datapoint_value)):
            return_datapoints.append(datapoint)

    return return_datapoints


def api_get_datapoint_from_metric(metric_attr, metric_value):
    metrics = api_get_metric_from_metric_attr(metric_attr, metric_value)
    datapoints = []
    # print (metrics)

    for metric in metrics:
        datapoint_id = metric["HasDatapoint"][0]
        datapoint_attr = "DatapointId"
        datapoint = api_get_datapoint_from_datapoint_attr(datapoint_attr, datapoint_id)
        datapoints.extend(datapoint)

    return datapoints


def api_get_datapoint_from_source(source_attr, source_value):
    list_datapoints = []

    metrics = api_get_metric_from_source(source_attr, source_value)

    for metric in metrics:
        metric = metric
        metric_id = metric["MetricId"]
        datapoints = api_get_datapoint_from_metric(metric_attr="MetricId", metric_value=metric_id)
        if (datapoints != []):
            list_datapoints.extend(datapoints)

    return list_datapoints


def api_get_datapoint_from_thing(thing_attr, thing_value):
    list_datapoints = []
    sources = api_get_source_from_thing(thing_attr, thing_value)

    for source in sources:
        source_id = source[0]
        datapoints = api_get_datapoint_from_source(source_attr="SourceId", source_value=source_id)
        list_datapoints.extend(datapoints)
    
    # print (list_datapoints)
    return list_datapoints


def api_get_datapoint_from_platform(platform_attr, platform_value):
    list_datapoints = []
    sources = api_get_source_from_platform(platform_attr, platform_value)

    for source in sources:
        source_id = source["SourceId"]
        datapoints = api_get_datapoint_from_source(source_attr="SourceId", source_value=source_id)
        list_datapoints.extend(datapoints)
    
    # print (list_datapoints)
    return list_datapoints


def api_get_datapoint_from_smartcontext(smartcontext_attr, smartcontext_value):
    list_datapoints = []
    platforms = api_get_platform_from_smartcontext(smartcontext_attr, smartcontext_value)

    for platform in platforms:
        platform_id = platform["PlatformId"]
        datapoints = api_get_datapoint_from_platform(platform_attr="PlatformId", platform_value=platform_id)
        list_datapoints.extend(datapoints)

    return list_datapoints


#############
# GET METRIC

def api_get_all_metric():
    metrics = []

    metric_paths = [os.path.join(metric_folder, metric_id) for metric_id in os.listdir(metric_folder)]
    for metric_path in metric_paths:
        f_metric = open(metric_path, 'r')
        metric = json.load(f_metric)
        metrics.append(metric)

    return metrics


def api_get_metric_from_datapoint(datapoint_attr, datapoint_value):
    datapoint_ids = api_get_datapoint_id_from_datapoint_attribute(datapoint_attr, datapoint_value)
    metrics = []

    for datapoint_id in datapoint_ids:
        metric_attr = "HasDatapoint"
        metric = api_get_metric_from_metric_attr(metric_attr, datapoint_id)
        if (metric != []):
            metrics.extend(metric)

    return metrics


def api_get_metric_from_metric_attr(metric_attr, metric_value):
    metrics = api_get_all_metric()
    return_metrics = []

    for metric in metrics:
        if (metric[metric_attr] == metric_value):
            return_metrics.append(metric)

    return return_metrics



def api_get_metric_from_thing(thing_attr, thing_value):
    list_metrics = []
    sources = api_get_source_from_thing(thing_attr, thing_value)
    # print (sources)

    for source in sources:
        source_id = source[0]
        # print (source_id)
        metrics = api_get_metric_from_source(source_attr="SourceId", source_value=source_id)
        list_metrics.extend(metrics)

    # print (list_metrics)
    return list(set(list_metrics))


def api_get_metric_from_source(source_attr, source_value):
    sources = api_get_source_from_source_attr(source_attr, source_value)
    metrics = []

    for source in sources:
        metric_ids = source["HasMetric"]
        for metric_id in metric_ids:
            metric_attr = "MetricId"
            metric = api_get_metric_from_metric_attr(metric_attr, metric_id)
            metrics.extend(metric)

    return metrics


def api_get_metric_from_platform(platform_attr, platform_value):
    list_metrics = []
    sources = api_get_source_from_platform(platform_attr, platform_value)
    
    for source in sources:
        source_id = source["SourceId"]
        metrics = api_get_metric_from_source(source_attr="SourceId", source_value=source_id)
        list_metrics.extend(metrics)

    # print (list_metrics)
    # return list(set(list_metrics))
    return list_metrics

def api_get_metric_from_smartcontext(smartcontext_attr, smartcontext_value):
    list_metrics = []
    smartcontexts = api_get_smartcontext_from_smartcontext_attr(smartcontext_attr, smartcontext_value)

    for smartcontext in smartcontexts:
        smartcontext_id = smartcontext["SmartContextId"]
        platforms = api_get_platform_from_smartcontext(smartcontext_attr="SmartContextId", smartcontext_value=smartcontext_id)
        for platform in platforms:
            platform_id = platform["PlatformId"]
            metrics = api_get_metric_from_platform(platform_attr="PlatformId", platform_value=platform_id)
            list_metrics.extend(metrics)

    return list_metrics


####################################################
# GET SOURCE


def api_get_all_source():
    sources = []

    source_paths = [os.path.join(source_folder, source_id) for source_id in os.listdir(source_folder)]
    for source_path in source_paths:
        f_source = open(source_path, 'r')
        source = json.load(f_source)
        sources.append(source)

    return sources


def api_get_source_from_datapoint(datapoint_attr, datapoint_value):
    list_source = []
    metrics = api_get_metric_from_datapoint(datapoint_attr, datapoint_value)
    
    for metric in metrics:
        metric_id = metric['MetricId']
        result = api_get_source_from_metric(metric_attr="MetricId", metric_value=metric_id)
        list_source.extend(result)

    return list_source


def api_get_source_from_metric(metric_attr, metric_value):
    metrics = api_get_metric_from_metric_attr(metric_attr, metric_value)
    sources = api_get_all_source()
    return_sources = []

    for metric in metrics:
        metric_id = metric["MetricId"]
        for source in sources:
            if (metric_id in source["HasMetric"]):
                return_sources.append(source)

    return return_sources


def api_get_source_from_source_attr(source_attr, source_value):
    sources = api_get_all_source()
    return_sources = []

    for source in sources:
        if (source[source_attr] == source_value):
            return_sources.append(source)

    return return_sources


def api_get_source_from_platform(platform_attr, platform_value):
    platforms = api_get_platform_from_platform_attr(platform_attr, platform_value)
    sources = []

    for platform in platforms:
        source_ids = platform["HasSource"]
        for source_id in source_ids:
            source_attr = "SourceId"
            source = api_get_source_from_source_attr(source_attr, source_id)
            sources.extend(source)

    return sources


def api_get_source_from_smartcontext(smartcontext_attr, smartcontext_value):
    list_sources = []
    smartcontexts = api_get_smartcontext_from_smartcontext_attr(smartcontext_attr, smartcontext_value)
    
    for smartcontext in smartcontexts:
        smartcontext_id = smartcontext["SmartContextId"]
        platforms = api_get_platform_from_smartcontext(smartcontext_attr, smartcontext_value)
        for platform in platforms:
            platform_id = platform["PlatformId"]
            sources = api_get_source_from_platform(platform_attr="PlatformId", platform_value=platform_id)
            list_sources.extend(sources)

    return list_sources


#####################################################
# GET PLATFORM

def api_get_all_platform():
    platforms = []

    platform_paths = [os.path.join(platform_folder, platform_id) for platform_id in os.listdir(platform_folder)]
    for platform_path in platform_paths:
        f_platform = open(platform_path, 'r')
        platform = json.load(f_platform)
        platforms.append(platform)

    return platforms


def api_get_platform_from_datapoint(datapoint_attr, datapoint_value):
    metrics = api_get_metric_from_datapoint(datapoint_attr, datapoint_value)
    list_platform = []

    for metric in metrics:
        metric_id = metric['MetricId']
        result = api_get_platform_from_metric(metric_attr="MetricId", metric_value=metric_id)
        list_platform.extend(result)

    return list_platform


def api_get_platform_from_metric(metric_attr, metric_value):
    list_platforms = []
    sources = api_get_source_from_metric(metric_attr, metric_value)
    # print (sources)

    for source in sources:
        source_id = source["SourceId"]
        platforms = api_get_platform_from_source(source_attr="SourceId", source_value=source_id)
        list_platforms.extend(platforms)

    return list_platforms


def api_get_platform_from_thing(thing_attr, thing_value):
    list_platforms = []

    sources = api_get_source_from_thing(thing_attr, thing_value)
    for source in sources:
        source_id = source[0]
        platforms = api_get_platform_from_source(source_attr="SourceId", source_value=source_id)
        list_platforms.extend(platforms)

    return list(set(list_platforms))


def api_get_platform_from_source(source_attr, source_value):
    sources = api_get_source_from_source_attr(source_attr, source_value)
    platforms = api_get_all_platform()
    return_platforms = []

    for source in sources:
        source_id = source["SourceId"]
        for platform in platforms:
            if (source_id in platform["HasSource"]):
                return_platforms.append(platform)
    
    return list({v["PlatformId"]:v for v in return_platforms}.values())


def api_get_platform_from_platform_attr(platform_attr, platform_value):
    platforms = api_get_all_platform()
    return_platforms = []

    for platform in platforms:
        if (platform[platform_attr] == platform_value):
            return_platforms.append(platform)

    return return_platforms


def api_get_platform_from_smartcontext(smartcontext_attr, smartcontext_value):
    smartcontexts = api_get_smartcontext_from_smartcontext_attr(smartcontext_attr, smartcontext_value)
    platforms = []

    for smartcontext in smartcontexts:
        # add platform in smartcontext
        if (smartcontext["HasPlatform"] != []):
            platform_ids = smartcontext["HasPlatform"]
            for platform_id in platform_ids:
                platform_attr = "PlatformId"
                platform = api_get_platform_from_platform_attr(platform_attr, platform_id)
                platforms.extend(platform)

        # add platform in sub_smartcontext
        smartcontext_id = smartcontext["SmartContextId"]
        sub_smartcontexts = api_get_sub_smartcontext_from_parent_smartcontext(smartcontext_id)
        for sub_smartcontext in sub_smartcontexts:
            platform_ids = sub_smartcontext["HasPlatform"]
            for platform_id in platform_ids:
                platform_attr = "PlatformId"
                platform = api_get_platform_from_platform_attr(platform_attr, platform_id)
                platforms.extend(platform)

    return platforms


#################################################
# GET SMARTCONTEXT

def api_get_all_smartcontext():
    smartcontexts = []

    smartcontext_paths = [os.path.join(smartcontext_folder, smartcontext_id) for smartcontext_id in os.listdir(smartcontext_folder)]
    for smartcontext_path in smartcontext_paths:
        f_smartcontext = open(smartcontext_path, 'r')
        smartcontext = json.load(f_smartcontext)
        smartcontexts.append(smartcontext)

    return smartcontexts


def api_get_smartcontext_from_datapoint(datapoint_attr, datapoint_value):
    list_smartcontext = []
    
    datapoint_ids = api_get_datapoint_id_from_datapoint_attribute(datapoint_attr, datapoint_value)
    for datapoint_id in datapoint_ids:
        datapoint_attr = "DatapointId"
        metrics = api_get_metric_from_datapoint(datapoint_attr, datapoint_id)

        for metric in metrics:
            metric_id = metric["MetricId"]
            results = api_get_smartcontext_from_metric(metric_attr="MetricId", metric_value=metric_id)
            list_smartcontext.extend(results)

    return list({v["SmartContextId"]:v for v in list_smartcontext}.values())


def api_get_smartcontext_from_metric(metric_attr, metric_value):
    list_smartcontexts = []
    platforms = api_get_platform_from_metric(metric_attr, metric_value)
    
    for platform in platforms:
        platform_id = platform["PlatformId"]
        smartcontexts = api_get_smartcontext_from_platform(platform_attr="PlatformId", platform_value=platform_id)
        list_smartcontexts.extend(smartcontexts)

    return list({v["SmartContextId"]:v for v in list_smartcontexts}.values())


def api_get_smartcontext_from_source(source_attr, source_value):
    list_smartcontexts = []
    platforms = api_get_platform_from_source(source_attr, source_value)
    # print len(platforms)

    for platform in platforms:
        platform_id = platform["PlatformId"]
        # add smartcontext
        smartcontexts = api_get_smartcontext_from_platform(platform_attr="PlatformId", platform_value=platform_id)
        list_smartcontexts.extend(smartcontexts)

    return list({v["SmartContextId"]:v for v in list_smartcontexts}.values())


def api_get_smartcontext_from_platform(platform_attr, platform_value):
    platforms = api_get_platform_from_platform_attr(platform_attr, platform_value)
    smartcontexts = api_get_all_smartcontext()
    return_smartcontexts = []

    for platform in platforms:
        platform_id = platform["PlatformId"]
        for smartcontext in smartcontexts:
            if (platform_id in smartcontext["HasPlatform"]):
                # add smartcontetx
                return_smartcontexts.append(smartcontext)
                # add parent smartcontext
                parent_smartcontext_ids = smartcontext["ParentSmartContextId"]
                
                for parent_smartcontext_id in parent_smartcontext_ids:
                    parent_smartcontext_attr = "SmartContextId"
                    parent_smartcontext = api_get_smartcontext_from_smartcontext_attr(parent_smartcontext_attr,
                                                                                      parent_smartcontext_id)
                    return_smartcontexts.extend(parent_smartcontext)


    return return_smartcontexts


def api_get_smartcontext_from_smartcontext_attr(smartcontext_attr, smartcontext_value):
    smartcontexts = api_get_all_smartcontext()
    return_smartcontexts = []

    for smartcontext in smartcontexts:
        if (smartcontext[smartcontext_attr] == smartcontext_value):
            return_smartcontexts.append(smartcontext)

    return return_smartcontexts


def api_get_sub_smartcontext_from_parent_smartcontext(parent_smartcontext_id):
    """ Get all smartcontext that this smartcontext contains
    return : list of smartcontexts, list_smart
    """
    smartcontext_attr = "SmartContextId"
    smartcontext = api_get_smartcontext_from_smartcontext_attr(smartcontext_attr, parent_smartcontext_id)[0]
    sub_smartcontext_ids = smartcontext["SubSmartContextId"]
    sub_smartcontexts = []

    for sub_smartcontext_id in sub_smartcontext_ids:
        sub_smartcontext_attr = "SmartContextId"
        sub_smartcontext = api_get_smartcontext_from_smartcontext_attr(sub_smartcontext_attr, sub_smartcontext_id)[0]
        sub_smartcontexts.append(sub_smartcontext)

        sub_sub_smartcontexts = api_get_sub_smartcontext_from_parent_smartcontext(sub_smartcontext_id)
        sub_smartcontexts.extend(sub_sub_smartcontexts)

    return sub_smartcontexts


def api_get_parent_smartcontext_from_sub_smartcontext(sub_smartcontext_id):
    sub_smartcontext_attr = "SmartContextId"
    smartcontext = api_get_smartcontext_from_smartcontext_attr(sub_smartcontext_attr, sub_smartcontext_id)[0]
    parent_smartcontext_id = smartcontext["ParentSmartContextId"][0]
    parent_smartcontext_attr = "SmartContextId"
    parent_smartcontext = api_get_smartcontext_from_smartcontext_attr(parent_smartcontext_attr, parent_smartcontext_id)

    return parent_smartcontext





if __name__ == "__main__":
    # x = api_get_all_datapoint()
    # x = api_get_all_metric()
    # x = api_get_all_source()
    # x = api_get_all_platform()
    # x = api_get_all_smartcontext()

    x = api_get_datapoint_from_datapoint_attr('value', '55')
    # x = api_get_metric_from_metric_attr("MetricId", 'humidity_homeassistant')
    # x = api_get_source_from_source_attr("SourceId", 'motion_openhab')
    # x = api_get_platform_from_platform_attr("PlatformId", 'openhab_id')
    # x = api_get_smartcontext_from_smartcontext_attr('SmartContextName', 'phong_sinh_vien')

    # x = api_get_datapoint_id_from_datapoint_attribute('DatapointId', 'humidity_homeassistant_datapoint')
    # x = api_get_metric_id_from_metric_attribute('MetricName', 'temperature_phong_may_chu')
    # x = api_get_source_id_from_source_attribute('SourceStatus', 'active')
    # x = api_get_platform_id_from_platform_attribute('PlatformPort', '8080')
    # x = api_get_smartcontext_id_from_smartcontext_attribute('SmartContextName', 'HPCC')

    # x = api_get_datapoint_from_metric("MetricId", 'Humidity')
    # x = api_get_metric_from_datapoint('DataType', 'float')
    # x = api_get_metric_from_source('SourceType', 'thing')
    # x = api_get_source_from_metric("MetricId", 'humidity_homeassistant')
    # x = api_get_source_from_platform('PlatformPort', "8080")
    # x = api_get_platform_from_source('SourceType', 'thing')
    # x = api_get_platform_from_smartcontext('SmartContextName', 'HPCC')
    # x = api_get_smartcontext_from_platform('PlatformPort', "8123")
    # x = api_get_sub_smartcontext_from_parent_smartcontext('HPCC_id')
    # x = api_get_parent_smartcontext_from_sub_smartcontext('phong_sinh_vien_id')

    # x = api_get_datapoint_from_source('SourceStatus', 'active')
    # x = api_get_datapoint_from_platform('PlatformPort', "8080")
    # x = api_get_datapoint_from_smartcontext("SmartContextId", 'phong_can_bo_id')

    # x = api_get_metric_from_platform('PlatformPort', "8080")
    # x = api_get_metric_from_smartcontext("SmartContextId", 'HPCC_id')
    

    # x = api_get_source_from_smartcontext('SmartContextName', 'phong_sinh_vien')
    # x = api_get_source_from_datapoint('value', '64.0')
    

    # x = api_get_platform_from_metric("MetricId", 'light_openhab')

    # x = api_get_smartcontext_from_source('SourceStatus', 'active')
    # x = api_get_smartcontext_from_metric("MetricId", 'humidity_thingsboard')
    # x = api_get_smartcontext_from_datapoint('DataType', 'int')


    print (x)
    print (len(x))