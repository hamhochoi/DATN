import MySQLdb
from influxdb import InfluxDBClient
import traceback
import numpy as np


# Influx connection
client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('datn')

# MySQL connection
db = MySQLdb.connect("localhost","root","root","datn" )
cursor = db.cursor()



###########################################################
# BASE API

def api_get_measurement_from_datapoint_attribute(datapoint_attribute, datapoint_value):
    metric_ids = api_get_all_metric_id()
    list_measurement = []

    for metric_id in metric_ids:
        query = 'SELECT * FROM "datn"."autogen".{} '.format(metric_id)
        # print (query)
        results = client.query(query)
        points = results.get_points()

        for point in points:
            if (point[datapoint_attribute] == datapoint_value or \
                str(point[datapoint_attribute]) == str(datapoint_value)
            ):
                list_measurement.append(metric_id)

    return list_measurement


def api_get_metric_id_from_metric_attribute(metric_attribute, metric_value):
    query = 'select MetricId from Metric \
             where {}="{}"'.format(metric_attribute, metric_value)

    # print (query)
    list_result = []
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            list_result.append(result[0])

        return list_result
    except:
        traceback.print_exc()


def api_get_thing_id_from_thing_attribute(thing_attribute, thing_value):
    query = 'select ThingGlobalId from Thing \
             where {}="{}"'.format(thing_attribute, thing_value)
    # print (query)
    list_result = []
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            list_result.append(result[0])

        return list_result
    except:
        traceback.print_exc()


def api_get_source_id_from_source_attribute(source_attribute, source_value):
    query = 'select SourceId from IoTSource \
             where {}="{}"'.format(source_attribute, source_value)
    # print (query)
    list_result = []
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            list_result.append(result[0])

        return list_result
    except:
        traceback.print_exc()


def api_get_platform_id_from_platform_attribute(platform_attribute, platform_value):
    query = 'select PlatformId from Platform \
             where {}="{}"'.format(platform_attribute, platform_value)

    # print (query)
    list_result = []
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            list_result.append(result[0])

        return list_result
    except:
        traceback.print_exc()


def api_get_smartcontext_id_from_smartcontext_attribute(smartcontext_attribute, smartcontext_value):
    query = 'select SmartContextId from SmartContext \
             where {}="{}"'.format(smartcontext_attribute, smartcontext_value)

    # print (query)
    list_result = []
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            list_result.append(result[0])

        return list_result
    except:
        traceback.print_exc()
























###################################################
# GET DATAPOINT

def api_get_all_datapoint():
    list_datapoints = []

    metric_ids = api_get_all_metric_id()
    for metric_id in metric_ids:
        datapoints = api_get_datapoint_from_metric(metric_attr="MetricId", metric_value=metric_id)
        list_datapoints.extend(datapoints)

    return list_datapoints


def api_get_datapoint_from_measurement(measurement):
    return api_get_datapoint_from_metric(metric_attr="MetricId", metric_value=measurement)


def api_get_datapoint_from_datapoint_attr(datapoint_attr, datapoint_value):
    metric_ids = api_get_all_metric_id()
    list_point = []

    for metric_id in metric_ids:        
        query = 'SELECT * FROM "datn"."autogen".{} '.format(metric_id)
        # print (query)
        results = client.query(query)
        points = results.get_points()

        for point in points:
            if (point[datapoint_attr] == datapoint_value or \
                str(point[datapoint_attr]) == str(datapoint_value)
            ):
                list_point.append(tuple(point.values()))
        
    return list_point


def api_get_datapoint_from_metric(metric_attr, metric_value):
    metric_ids = api_get_metric_id_from_metric_attribute(metric_attr, metric_value)
    list_point = []
    # print (metric_ids)

    for metric_id in metric_ids:
        query = 'SELECT * FROM "datn"."autogen".{} '.format(metric_id)
        # print (query)
        results = client.query(query)
        points = results.get_points()

        for point in points:
            list_point.append(tuple(point.values()))

    return list_point


def api_get_datapoint_from_source(source_attr, source_value):
    list_datapoints = []

    metrics = api_get_metric_from_source(source_attr, source_value)
    for metric in metrics:
        metric_id = metric[0]
        datapoints = api_get_datapoint_from_metric(metric_attr="MetricId", metric_value=metric_id)
        # print (datapoints)
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
        source_id = source[0]
        datapoints = api_get_datapoint_from_source(source_attr="SourceId", source_value=source_id)
        list_datapoints.extend(datapoints)
    
    # print (list_datapoints)
    return list_datapoints


def api_get_datapoint_from_smartcontext(smartcontext_attr, smartcontext_value):
    list_datapoints = []
    platforms = api_get_platform_from_smartcontext(smartcontext_attr, smartcontext_value)

    # print (platforms)
    for platform in platforms:
        platform_id = platform[0]
        # print (platform_id)
        datapoints = api_get_datapoint_from_platform(platform_attr="PlatformId", platform_value=platform_id)
        list_datapoints.extend(datapoints)

    # print (list_datapoints)
    return list_datapoints
























#############
# GET METRIC

def api_get_all_metric_id():
    query = 'select MetricId from Metric'
    list_result = []

    try:
        cursor.execute(query)
        results = cursor.fetchall()
        # print (results)
        for result in results:
            list_result.append(result[0])

        return list_result
    except:
        traceback.print_exc()


def api_get_metric_from_datapoint(datapoint_attr, datapoint_value):
    measurements = api_get_measurement_from_datapoint_attribute(datapoint_attr, datapoint_value)
    list_metric = []

    for measurement in measurements:
        query = 'select * from Metric \
                where MetricId="{}"'.format(measurement)
        # print (query)
        
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            # print (results)
            list_metric.extend(results)

        except:
            traceback.print_exc()
    
    return list_metric


def api_get_metric_from_metric_attr(metric_attr, metric_value):
    query = 'select * from Metric \
             where {}="{}"'.format(metric_attr, metric_value)

    # print (query)
    list_result = []

    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            list_result.append(result)

        return list_result
    except:
        traceback.print_exc()


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
    list_metric = []
    source_ids = api_get_source_id_from_source_attribute(source_attr, source_value)

    for source_id in source_ids:
        try:
            query = ' select * from Metric where SourceId = "{}";'.format(source_id)
            cursor.execute(query)
            results = cursor.fetchall()
            # print (results)
            list_metric.extend(results)
        except:
            traceback.print_exc()

    return list(set(list_metric))


def api_get_metric_from_platform(platform_attr, platform_value):
    list_metrics = []

    sources = api_get_source_from_platform(platform_attr, platform_value)
    for source in sources:
        source_id = source[0]
        metrics = api_get_metric_from_source(source_attr="SourceId", source_value=source_id)
        list_metrics.extend(metrics)

    # print (list_metrics)
    return list(set(list_metrics))


def api_get_metric_from_smartcontext(smartcontext_attr, smartcontext_value):
    list_metrics = []
    smartcontexts = api_get_smartcontext_from_smartcontext_attr(smartcontext_attr, smartcontext_value)

    for smartcontext in smartcontexts:
        smartcontext_id = smartcontext[0]
        platforms = api_get_platform_from_smartcontext(smartcontext_attr="SmartContextId", smartcontext_value=smartcontext_id)
        for platform in platforms:
            platform_id = platform[0]
            metrics = api_get_metric_from_platform(platform_attr="PlatformId", platform_value=platform_id)
            list_metrics.extend(metrics)

    # print (list_metrics)
    return list(set(list_metrics))























#######################################################
## GET THING


def api_get_all_thing_id():
    query = 'select ThingGlobalId from Thing'
    list_result = []

    try:
        cursor.execute(query)
        results = cursor.fetchall()
        # print (results)
        for result in results:
            list_result.append(result[0])

        return list_result
    except:
        traceback.print_exc()


def api_get_thing_from_datapoint(datapoint_attr, datapoint_value):
    list_thing = []
    metric_ids = api_get_metric_from_datapoint(datapoint_attr, datapoint_value)
    # print (metric_ids)

    for metric_id in metric_ids:
        metric_id = metric_id[0]
        result = api_get_thing_from_metric(metric_attr="MetricId", metric_value=metric_id)
        list_thing.extend(result)

    return list_thing


def api_get_thing_from_metric(metric_attr, metric_value):
    list_things = []

    sources = api_get_source_from_metric(metric_attr, metric_value)
    for source in sources:
        source_id = source[0]
        things = api_get_thing_from_source(source_attr="SourceId", source_value=source_id)
        list_things.extend(things)

    # print (list_things)
    return list(set(list_things)) 


def api_get_thing_from_thing_attr(thing_attr, thing_value):
    query = 'select * from Thing \
             where {}="{}"'.format(thing_attr, thing_value)
    # print (query)
    list_result = []
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            list_result.append(result)

        return list_result
    except:
        traceback.print_exc()


def api_get_thing_from_source(source_attr, source_value):
    source_ids = api_get_source_id_from_source_attribute(source_attr, source_value)
    list_thing = []

    for source_id in source_ids:
        query = 'select ThingName, ThingGlobalId \
                from Thing, IoTSource\
                where (Thing.ThingGlobalId = IoTSource.SourceId) and \
                    (SourceId = "{}")'.format(source_id)

        try:
            cursor.execute(query)
            results = cursor.fetchall()
            # print (results)
            list_thing.extend(results)
        except:
            traceback.print_exc()

    return list(set(list_thing))


def api_get_thing_from_platform(platform_attr, platform_value):
    list_things = []

    sources = api_get_source_from_platform(platform_attr, platform_value)
    for source in sources:
        source_id = source[0]
        things = api_get_thing_from_source(source_attr="SourceId", source_value=source_id)
        list_things.extend(things)


    # print (list_things)
    return list(set(list_things)) 


def api_get_thing_from_smartcontext(smartcontext_attr, smartcontext_value):
    list_things = []
    smartcontexts = api_get_smartcontext_from_smartcontext_attr(smartcontext_attr, smartcontext_value)

    for smartcontext in smartcontexts:
        smartcontext_id = smartcontext[0]
        platforms = api_get_platform_from_smartcontext(smartcontext_attr="SmartContextId", smartcontext_value=smartcontext_id)
        for platform in platforms:
            platform_id = platform[0]
            things = api_get_thing_from_platform(platform_attr="PlatformId", platform_value=platform_id)
            list_things.extend(things)
    
    return list(set(list_things))























####################################################
# GET SOURCE


def api_get_all_source_id():
    query = 'select SourceId from IoTSource'
    list_result = []

    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            list_result.append(result[0])

        return list_result
    except:
        traceback.print_exc()


def api_get_source_from_datapoint(datapoint_attr, datapoint_value):
    list_source = []
    metric_ids = api_get_metric_from_datapoint(datapoint_attr, datapoint_value)
    for metric_id in metric_ids:
        metric_id = metric_id[0]
        result = api_get_source_from_metric(metric_attr="MetricId", metric_value=metric_id)
        list_source.extend(result)

    return list_source


def api_get_source_from_metric(metric_attr, metric_value):
    metric_ids = api_get_metric_id_from_metric_attribute(metric_attr, metric_value)
    list_source = []

    for metric_id in metric_ids:
        query = 'select IoTSource.SourceId, EndPoint, SourceStatus, \
                        Description, SourceType, Label, \
                        PlatformId, LocalId \
                from Metric, IoTSource \
                where (Metric.SourceId = IoTSource.SourceId) and \
                    (MetricId = "{}")'.format(metric_id)
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            # print (results)
            list_source.extend(results)
        except:
            traceback.print_exc()

    return list(set(list_source))


def api_get_source_from_thing(thing_attr, thing_value):
    thing_ids = api_get_thing_id_from_thing_attribute(thing_attr, thing_value)
    list_source = []

    for thing_id in thing_ids:
        query = 'select SourceId, EndPoint, SourceStatus, \
                        Description, SourceType, Label, \
                        IoTSource.PlatformId, LocalId \
                from Thing, IoTSource\
                where (Thing.ThingGlobalId = IoTSource.SourceId) and \
                    (ThingGlobalId = "{}")'.format(thing_id)

        try:
            cursor.execute(query)
            results = cursor.fetchall()
            # print (results)
            list_source.extend(results)
        except:
            traceback.print_exc()

    return list(set(list_source))


def api_get_source_from_source_attr(source_attr, source_value):
    query = 'select * from IoTSource \
             where {}="{}"'.format(source_attr, source_value)
    # print (query)
    list_result = []
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            list_result.append(result)

        return list_result
    except:
        traceback.print_exc()


def api_get_source_from_platform(platform_attr, platform_value):
    platform_ids = api_get_platform_id_from_platform_attribute(platform_attr, platform_value)
    list_source = []
    
    for platform_id in platform_ids:
        query = 'select SourceId, EndPoint, SourceStatus, \
                        Description, SourceType, Label, \
                        IoTSource.PlatformId, LocalId \
                from Platform, IoTSource\
                where (Platform.PlatformId = IoTSource.PlatformId) and \
                    (Platform.PlatformId = "{}")'.format(platform_id)

        try:
            cursor.execute(query)
            results = cursor.fetchall()
            # print (results)
            list_source.extend(results)
        except:
            traceback.print_exc()

    return list(set(list_source))


def api_get_source_from_smartcontext(smartcontext_attr, smartcontext_value):
    list_sources = []
    smartcontexts = api_get_smartcontext_from_smartcontext_attr(smartcontext_attr, smartcontext_value)
    
    for smartcontext in smartcontexts:
        smartcontext_id = smartcontext[0]
        platforms = api_get_platform_from_smartcontext(smartcontext_attr, smartcontext_value)
        for platform in platforms:
            platform_id = platform[0]
            sources = api_get_source_from_platform(platform_attr="PlatformId", platform_value=platform_id)
            list_sources.extend(sources)

    return list(set(list_sources))






















#####################################################
# GET PLATFORM

def api_get_all_platform_id():
    query = 'select PlatformId from Platform'
    list_result = []

    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            list_result.append(result[0])

        return list_result
    except:
        traceback.print_exc()


def api_get_platform_from_datapoint(datapoint_attr, datapoint_value):
    metric_ids = api_get_metric_from_datapoint(datapoint_attr, datapoint_value)
    list_platform = []

    for metric_id in metric_ids:
        metric_id = metric_id[0]
        result = api_get_platform_from_metric(metric_attr="MetricId", metric_value=metric_id)
        list_platform.extend(result)

    return list_platform


def api_get_platform_from_metric(metric_attr, metric_value):
    list_platforms = []
    sources = api_get_source_from_metric(metric_attr, metric_value)
    # print (sources)

    for source in sources:
        source_id = source[0]
        # print (source_id)
        platforms = api_get_platform_from_source(source_attr="SourceId", source_value=source_id)
        list_platforms.extend(platforms)

    return list(set(list_platforms))


def api_get_platform_from_thing(thing_attr, thing_value):
    list_platforms = []

    sources = api_get_source_from_thing(thing_attr, thing_value)
    for source in sources:
        source_id = source[0]
        platforms = api_get_platform_from_source(source_attr="SourceId", source_value=source_id)
        list_platforms.extend(platforms)

    return list(set(list_platforms))


def api_get_platform_from_source(source_attr, source_value):
    list_platform = []
    source_ids = api_get_source_id_from_source_attribute(source_attr, source_value)

    for source_id in source_ids:
        query = 'select Platform.PlatformId, PlatformName, PlatformType, \
                        PlatformHost, PlatformPort, PlatformStatus, \
                        LastResponse\
                from Platform, IoTSource\
                where (Platform.PlatformId = IoTSource.PlatformId) and \
                    (SourceId = "{}")'.format(source_id)

        try:
            cursor.execute(query)
            results = cursor.fetchall()
            # print (results)
            list_platform.extend(results)
        except:
            traceback.print_exc()

    return list(set(list_platform))


def api_get_platform_from_platform_attr(platform_attr, platform_value):
    query = 'select * from  Platform\
             where {}="{}"'.format(platform_attr, platform_value)

    # print (query)
    list_result = []
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            list_result.append(result)

        return list_result
    except:
        traceback.print_exc()


def api_get_platform_from_smartcontext(smartcontext_attr, smartcontext_value):
    list_platforms = []
    smartcontext_ids = api_get_smartcontext_id_from_smartcontext_attribute(smartcontext_attr, smartcontext_value)

    for smartcontext_id in smartcontext_ids:
        query = 'select Platform.PlatformId, PlatformName, PlatformType, \
                                    PlatformHost, PlatformPort, PlatformStatus, \
                                    LastResponse\
                            from Platform, SmartContext\
                            where (Platform.PlatformId = SmartContext.PlatformId) and \
                                (SmartContextId = "{}")'.format(smartcontext_id)
        try:
            cursor.execute(query)
            platform = cursor.fetchall()
            list_platforms.extend(platform)
        except:
            traceback.print_exc()

        # Add platform from parent of smartcontext_id
        try:
            smartcontexts = api_get_sub_smartcontext_from_parent_smartcontext(smartcontext_id)
            
            for smartcontext in smartcontexts:
                sub_smartcontext_id = smartcontext[0]
                # print (smartcontext_id)

                query = 'select Platform.PlatformId, PlatformName, PlatformType, \
                                    PlatformHost, PlatformPort, PlatformStatus, \
                                    LastResponse\
                            from Platform, SmartContext\
                            where (Platform.PlatformId = SmartContext.PlatformId) and \
                                (SmartContextId = "{}")'.format(sub_smartcontext_id)

                cursor.execute(query)
                platforms = cursor.fetchall()
                # print (platforms)
                list_platforms.extend(platforms)
            
        except:
            traceback.print_exc()

    return list(set(list_platforms))






















#################################################
# GET SMARTCONTEXT

def api_get_all_smartcontext_id():
    query = 'select SmartContextId from SmartContext'
    list_result = []

    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            list_result.append(result[0])

        return list_result
    except:
        traceback.print_exc()


def api_get_smartcontext_from_datapoint(datapoint_attr, datapoint_value):
    measurements = api_get_measurement_from_datapoint_attribute(datapoint_attr, datapoint_value)
    list_smartcontext = []

    for measurement in measurements:
        results = api_get_smartcontext_from_metric(metric_attr="MetricId", metric_value=measurement)
        list_smartcontext.extend(results)

    return list_smartcontext


def api_get_smartcontext_from_metric(metric_attr, metric_value):
    list_smartcontexts = []

    platforms = api_get_platform_from_metric(metric_attr, metric_value)
    for platform in platforms:
        platform_id = platform[0]
        smartcontexts = api_get_smartcontext_from_platform(platform_attr="PlatformId", platform_value=platform_id)
        list_smartcontexts.extend(smartcontexts)

    return list(set(list_smartcontexts))


def api_get_smartcontext_from_thing(thing_attr, thing_value):
    list_smartcontexts = []
    platforms = api_get_platform_from_thing(thing_attr, thing_value)
    
    for platform in platforms:
        platform_id = platform[0]
        smartcontexts = api_get_smartcontext_from_platform(platform_attr="PlatformId", platform_value=platform_id)
        list_smartcontexts.extend(smartcontexts)

    return list(set(list_smartcontexts))


def api_get_smartcontext_from_source(source_attr, source_value):
    list_smartcontexts = []
    platforms = api_get_platform_from_source(source_attr, source_value)
    # print len(platforms)

    for platform in platforms:
        platform_id = platform[0]
        smartcontexts = api_get_smartcontext_from_platform(platform_attr="SourceId", platform_value=platform_id)
        list_smartcontexts.extend(smartcontexts)

    return list(set(list_smartcontexts))


def api_get_smartcontext_from_platform(platform_attr, platform_value):
    platform_ids = api_get_platform_id_from_platform_attribute(platform_attr, platform_value)
    list_smartcontexts = []

    for platform_id in platform_ids:
        query = 'select SmartContextId, SmartContextName, \
                        ParentSmartContextId, SubSmartContextId, \
                        SmartContext.PlatformId \
                from Platform, SmartContext\
                where (Platform.PlatformId = SmartContext.PlatformId) and \
                    (SmartContext.PlatformId = "{}")'.format(platform_id)

        try:
            cursor.execute(query)
            results = cursor.fetchall()
            list_smartcontexts.extend(results)
            
            for result in results:
                smartcontext_id = result[0]
                # print (smartcontext_id)
                parent_smartcontexts = api_get_parent_smartcontext_from_sub_smartcontext(smartcontext_id)
                list_smartcontexts.extend(parent_smartcontexts)
            
        except:
            traceback.print_exc()

    return list(set(list_smartcontexts))


def api_get_smartcontext_from_smartcontext_attr(smartcontext_attr, smartcontext_value):
    query = 'select * from SmartContext \
             where {}="{}"'.format(smartcontext_attr, smartcontext_value)

    # print (query)
    list_result = []
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            list_result.append(result)

        return list_result
    except:
        traceback.print_exc()


def api_get_sub_smartcontext_from_parent_smartcontext(parent_smartcontext_id):
    """ Get all smartcontext that this smartcontext contains
    return : list of smartcontexts, list_smart
    """
    query = 'select * from SmartContext \
             where ParentSmartContextId = "{}"'.format(parent_smartcontext_id)


    try:
        cursor.execute(query)
        results = cursor.fetchall()

        list_sub_smartcontext_ids = []
        list_sub_smartcontexts = []

        for result in results:
            list_sub_smartcontexts.append(result)
            smartcontext_id = result[0]
            list_sub_smartcontext_ids.append(smartcontext_id)

        # print ("1 ", list_sub_smartcontexts)
        if (list_sub_smartcontext_ids != []):
            for parent_smartcontext_id in list_sub_smartcontext_ids:
                sub_smartcontexts = api_get_sub_smartcontext_from_parent_smartcontext(parent_smartcontext_id)
                # print ("2 ", sub_smartcontexts)

                list_sub_smartcontexts.extend(sub_smartcontexts)
        else:
            return []
                
        return list(set(list_sub_smartcontexts))
    except:
        traceback.print_exc()


def api_get_parent_smartcontext_from_sub_smartcontext(sub_smartcontext_id):
    query = 'select * from SmartContext \
             where SubSmartContextId = "{}"'.format(sub_smartcontext_id)

    try:
        cursor.execute(query)
        results = cursor.fetchall()

        list_parent_smartcontext_ids = []
        list_parent_smartcontexts = []

        for result in results:
            list_parent_smartcontexts.append(result)
            smartcontext_id = result[0]
            list_parent_smartcontext_ids.append(smartcontext_id)

        # print ("1 ", list_parent_smartcontexts)
        if (list_parent_smartcontext_ids != []):
            for smartcontext_id in list_parent_smartcontext_ids:
                parent_smartcontexts = api_get_parent_smartcontext_from_sub_smartcontext(smartcontext_id)
                # print ("2 ", parent_smartcontexts)

                list_parent_smartcontexts.extend(parent_smartcontexts)
        else:
            return []
                
        return list(set(list_parent_smartcontexts))
    except:
        traceback.print_exc()







if __name__ == "__main__":
    x = api_get_all_datapoint()
    # x = api_get_all_metric_id()
    # x = api_get_all_thing_id()
    # x = api_get_all_source_id()
    # x = api_get_all_platform_id()
    # x = api_get_all_smartcontext_id()

    # x = api_get_datapoint_from_datapoint_attr('DataType', 'int')
    # x = api_get_metric_from_metric_attr('SourceId', 'source_id_1')
    # x = api_get_thing_from_thing_attr('ThingName', 'Temperature')
    # x = api_get_source_from_source_attr('PlatformId', 'platform_id_1')
    # x = api_get_platform_from_platform_attr('PlatformName', 'OpenHAB1')
    # x = api_get_smartcontext_from_smartcontext_attr('SmartContextName', 'HPCC')

    # x = api_get_measurement_from_datapoint_attribute('DataType', 'int')
    # x = api_get_metric_id_from_metric_attribute('MetricName', 'Temperature')
    # x = api_get_thing_id_from_thing_attribute('ThingName' , 'Temperature')
    # x = api_get_source_id_from_source_attribute('SourceStatus', 'active')
    # x = api_get_platform_id_from_platform_attribute('PlatformPort' , '8080')
    # x = api_get_smartcontext_id_from_smartcontext_attribute('SmartContextName', 'HPCC')

    # x = api_get_datapoint_from_metric('MetricName', 'Temperature')
    # x = api_get_metric_from_datapoint('DataType', 'int')
    # x = api_get_metric_from_source('SourceType', 'Thing')
    # x = api_get_source_from_metric('MetricName', 'Temperature')
    # x = api_get_source_from_platform('PlatformPort', 8080)
    # x = api_get_platform_from_source('SourceType', 'Thing')
    # x = api_get_thing_from_source('SourceType', 'Thing')
    # x = api_get_source_from_thing('ThingName', 'Temperature')
    # x = api_get_platform_from_smartcontext('SmartContextName', 'HPCC')
    # x = api_get_smartcontext_from_platform('PlatformPort', 8080)
    # x = api_get_sub_smartcontext_from_parent_smartcontext('smartcontext_id_1')
    # x = api_get_parent_smartcontext_from_sub_smartcontext('smartcontext_id_2')

    # x = api_get_datapoint_from_source('SourceStatus', 'active')
    # x = api_get_datapoint_from_thing('ThingName', 'Temperature')
    # x = api_get_datapoint_from_platform('PlatformPort', 8080)
    # x = api_get_datapoint_from_smartcontext('SmartContextId', 'parent_parent_smartcontext_id_1')

    # x = api_get_metric_from_thing('ThingName', 'Temperature')
    # x = api_get_metric_from_platform('PlatformPort', 8080)
    # x = api_get_metric_from_smartcontext('SmartContextId', 'smartcontext_id_1')
    
    # x = api_get_thing_from_datapoint('value', 32)
    # x = api_get_thing_from_platform('PlatformPort', 8080)
    # x = api_get_thing_from_smartcontext('SmartContextId', 'smartcontext_id_1')
    # x = api_get_thing_from_metric('MetricStatus', 'active')

    # x = api_get_source_from_smartcontext('SmartContextName', 'HPCC')

    # x = api_get_platform_from_metric('MetricName', 'Temperature')
    # x = api_get_platform_from_thing('ThingName', 'Temperature')

    # x = api_get_smartcontext_from_source('SourceStatus', 'active')
    # x = api_get_smartcontext_from_thing('ThingGlobalId', "source_id_6")
    # x = api_get_smartcontext_from_metric('MetricLocalId', 'metric_local_id_2')
    # x = api_get_smartcontext_from_datapoint('DataType', 'int')


    print (x)
    print (len(x))