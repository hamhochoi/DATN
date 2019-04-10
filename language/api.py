import MySQLdb
from influxdb import InfluxDBClient
import traceback


# Influx connection
client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('datn')

# MySQL connection
db = MySQLdb.connect("localhost","root","root","datn" )
cursor = db.cursor()



###########################################################
# BASE API

def api_get_metric_id_from_metric_attribute(metric_attribute):
    query = 'select MetricId from Metric \
             where MetricId="{}" or SourceId="{}" or \
                   MetricName="{}" or MetricType="{}" or \
                   Unit="{}" or MetricDomain="{}" or \
                   MetricStatus="{}" or MetricLocalId="{}" ;'\
                   .format(metric_attribute, metric_attribute, \
                           metric_attribute, metric_attribute, \
                           metric_attribute, metric_attribute, \
                           metric_attribute, metric_attribute)
    # print (query)
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        # print (results)

        return results
    except:
        traceback.print_exc()


def api_get_thing_id_from_thing_attribute(thing_attribute):
    query = 'select ThingGlobalId from Thing \
             where ThingGlobalId="{}" or ThingName="{}" ;'\
                   .format(thing_attribute, thing_attribute)
    # print (query)
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        # print (results)

        return results
    except:
        traceback.print_exc()


def api_get_source_id_from_source_attribute(source_attribute):
    query = 'select SourceId from IoTSource \
             where SourceId="{}" or EndPoint="{}" or \
                   SourceStatus="{}" or Description="{}" or\
                   SourceType="{}" or Label="{}" or \
                   PlatformId="{}" or LocalId="{}" ;'\
                   .format(source_attribute, source_attribute, \
                           source_attribute, source_attribute, \
                           source_attribute, source_attribute, \
                           source_attribute, source_attribute)
    # print (query)
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        # print (results)

        return results
    except:
        traceback.print_exc()


def api_get_platform_id_from_platform_attribute(platform_attribute):
    query = 'select PlatformId from Platform \
             where PlatformId="{}" or PlatformName="{}" or \
                   PlatformType="{}" or PlatformHost="{}" or\
                   PlatformPort="{}" or PlatformStatus="{}" or \
                   LastResponse="{}" ;'\
                   .format(platform_attribute, platform_attribute, \
                           platform_attribute, platform_attribute, \
                           platform_attribute, platform_attribute, \
                           platform_attribute)
    # print (query)
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        # print (results)

        return results
    except:
        traceback.print_exc()


def api_get_smartcontext_id_from_smartcontext_attribute(smartcontext_attribute):
    query = 'select SmartContextId from SmartContext \
             where SmartContextId="{}" or SmartContextName="{}" or \
                   ParentSmartContextId="{}" or SubSmartContextId="{}" or\
                   PlatformId="{}" ;'\
                   .format(smartcontext_attribute, smartcontext_attribute, \
                           smartcontext_attribute, smartcontext_attribute, \
                           smartcontext_attribute)
    # print (query)
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        # print (results)

        return results
    except:
        traceback.print_exc()

########################################################
# Get all object in database

def api_get_all_metric():
    query = 'select MetricId from Metric'

    try:
        cursor.execute(query)
        results = cursor.fetchall()
        # print (results)

        return results
    except:
        traceback.print_exc()


def api_get_all_thing():
    query = 'select ThingGlobalId from Thing'
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        # print (results)

        return results
    except:
        traceback.print_exc()

def api_get_all_source():
    query = 'select SourceId from IoTSource'
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        # print (results)

        return results
    except:
        traceback.print_exc()

def api_get_all_platform():
    query = 'select PlatformId from Platform'
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        # print (results)

        return results
    except:
        traceback.print_exc()


def api_get_all_smartcontext():
    query = 'select SmartContextId from SmartContext'
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        # print (results)

        return results
    except:
        traceback.print_exc()



######################################################################################
# END OF BASE APIs

def api_get_datapoint_from_metric(metric_id):
    results = client.query('SELECT * FROM "datn"."autogen".{} '.format(metric_id))
    points = results.get_points()

    list_point = []
    for point in points:
        # print (point)
        list_point.append(point)

    return list_point


def api_get_metric_from_source(source_id):
    try:
        query = ' select * from Metric where SourceId = "{}";'.format(source_id)
        cursor.execute(query)
        results = cursor.fetchall()
        # print (results)

        return results
    except:
        traceback.print_exc()

    
def api_get_source_from_metric(metric_id):
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

        return results
    except:
        traceback.print_exc()


def api_get_source_from_platform(platform_id):
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
        
        return results
    except:
        traceback.print_exc()


def api_get_platform_from_source(source_id):
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
        
        return results
    except:
        traceback.print_exc()


def api_get_thing_from_source(source_id):
    query = 'select ThingName, ThingGlobalId \
             from Thing, IoTSource\
             where (Thing.ThingGlobalId = IoTSource.SourceId) and \
                   (SourceId = "{}")'.format(source_id)

    try:
        cursor.execute(query)
        results = cursor.fetchall()
        # print (results)
        
        return results
    except:
        traceback.print_exc()


def api_get_source_from_thing(thing_id):
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
        
        return results
    except:
        traceback.print_exc()


def api_get_platform_from_smartcontext(smartcontext_id):
    list_platforms = []

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
        
        return list_platforms
    except:
        traceback.print_exc()


def api_get_smartcontext_from_platform(platform_id):
    query = 'select SmartContextId, SmartContextName, \
                    ParentSmartContextId, SubSmartContextId, \
                    SmartContext.PlatformId \
             from Platform, SmartContext\
             where (Platform.PlatformId = SmartContext.PlatformId) and \
                   (SmartContext.PlatformId = "{}")'.format(platform_id)
    list_smartcontexts = []

    try:
        cursor.execute(query)
        results = cursor.fetchall()
        list_smartcontexts.extend(results)
        
        for result in results:
            smartcontext_id = result[0]
            # print (smartcontext_id)
            parent_smartcontexts = api_get_parent_smartcontext_from_sub_smartcontext(smartcontext_id)
            list_smartcontexts.extend(parent_smartcontexts)
        
        return list_smartcontexts
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
                
        return list_sub_smartcontexts
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
                
        return list_parent_smartcontexts
    except:
        traceback.print_exc()



###################################################
# GET DATAPOINT

def api_get_datapoint_from_source(source_id):
    list_datapoints = []

    metrics = api_get_metric_from_source(source_id)
    for metric in metrics:
        metric_id = metric[0]
        datapoints = api_get_datapoint_from_metric(metric_id)
        list_datapoints.extend(datapoints)

    # print (list_datapoints)
    return list_datapoints


def api_get_datapoint_from_thing(thing_id):
    list_datapoints = []

    sources = api_get_source_from_thing(thing_id)
    for source in sources:
        source_id = source[0]
        datapoints = api_get_datapoint_from_source(source_id)
        list_datapoints.extend(datapoints)
    
    # print (list_datapoints)
    return list_datapoints


def api_get_datapoint_from_platform(platform_id):
    list_datapoints = []

    sources = api_get_source_from_platform(platform_id)
    for source in sources:
        source_id = source[0]
        datapoints = api_get_datapoint_from_source(source_id)
        list_datapoints.extend(datapoints)
    
    # print (list_datapoints)
    return list_datapoints


def api_get_datapoint_from_smartcontext(smartcontext_id):
    list_datapoints = []

    platforms = api_get_platform_from_smartcontext(smartcontext_id)
    # print (platforms)
    for platform in platforms:
        platform_id = platform[0]
        # print (platform_id)
        datapoints = api_get_datapoint_from_platform(platform_id)
        list_datapoints.extend(datapoints)

    # print (list_datapoints)
    return list_datapoints


def api_get_metric_from_thing(thing_id):
    list_metrics = []

    things = api_get_thing_from_source(thing_id)
    # print (things)

    for thing in things:
        source_id = thing[1]
        metrics = api_get_metric_from_source(source_id)
        list_metrics.extend(metrics)

    # print (list_metrics)
    return list_metrics


def api_get_metric_from_platform(platform_id):
    list_metrics = []

    sources = api_get_source_from_platform(platform_id)
    for source in sources:
        source_id = source[0]
        metrics = api_get_metric_from_source(source_id)
        list_metrics.extend(metrics)

    # print (list_metrics)
    return list_metrics


def api_get_metric_from_smartcontext(smartcontext_id):
    list_metrics = []

    sub_smartcontexts = api_get_sub_smartcontext_from_parent_smartcontext(smartcontext_id)

    for smartcontext in sub_smartcontexts:
        smartcontext_id = smartcontext[0]
        platforms = api_get_platform_from_smartcontext(smartcontext_id)
        for platform in platforms:
            platform_id = platform[0]
            metrics = api_get_metric_from_platform(platform_id)
            list_metrics.extend(metrics)

    # print (list_metrics)
    return list_metrics



#######################################################
## GET THING

def api_get_thing_from_platform(platform_id):
    list_things = []

    sources = api_get_source_from_platform(platform_id)
    for source in sources:
        source_id = source[0]
        things = api_get_thing_from_source(source_id)
        list_things.extend(things)


    # print (list_things)
    return list_things 


def api_get_thing_from_smartcontext(smartcontext_id):
    list_things = []

    sub_smartcontexts = api_get_sub_smartcontext_from_parent_smartcontext(smartcontext_id)
    for smartcontext in sub_smartcontexts:
        smartcontext_id = smartcontext[0]
        platforms = api_get_platform_from_smartcontext(smartcontext_id)
        for platform in platforms:
            platform_id = platform[0]
            things = api_get_thing_from_platform(platform_id)
            list_things.extend(things)

    
    return list_things



####################################################
# GET SOURCE

def api_get_source_from_smartcontext(smartcontext_id):
    list_sources = []

    sub_smartcontexts = api_get_sub_smartcontext_from_parent_smartcontext(smartcontext_id)
    for smartcontext in sub_smartcontexts:
        smartcontext_id = smartcontext[0]

        platforms = api_get_platform_from_smartcontext(smartcontext_id)
        for platform in platforms:
            platform_id = platform[0]
            sources = api_get_source_from_platform(platform_id)
            list_sources.extend(sources)


    return list_sources


#####################################################
# GET PLATFORM

def api_get_platform_from_metric(metric_id):
    list_platforms = []

    sources = api_get_source_from_metric(metric_id)
    for source in sources:
        source_id = source[0]
        platforms = api_get_platform_from_source(source_id)
        list_platforms.extend(platforms)


    return list_platforms


def api_get_platform_from_thing(thing_id):
    list_platforms = []

    sources = api_get_source_from_thing(thing_id)
    for source in sources:
        source_id = source[0]
        platforms = api_get_platform_from_source(source_id)
        list_platforms.extend(platforms)


    return list_platforms


#################################################
# GET SMARTCONTEXT

def api_get_smartcontext_from_source(source_id):
    list_smartcontexts = []

    platforms = api_get_platform_from_source(source_id)
    for platform in platforms:
        platform_id = platform[0]
        smartcontexts = api_get_smartcontext_from_platform(platform_id)
        list_smartcontexts.extend(smartcontexts)

    return list_smartcontexts


def api_get_smartcontext_from_thing(thing_id):
    list_smartcontexts = []

    platforms = api_get_platform_from_thing(thing_id)
    for platform in platforms:
        platform_id = platform[0]
        smartcontexts = api_get_smartcontext_from_platform(platform_id)
        list_smartcontexts.extend(smartcontexts)

    return list_smartcontexts


def api_get_smartcontext_from_metric(metric_id):
    list_smartcontexts = []

    platforms = api_get_platform_from_metric(metric_id)
    for platform in platforms:
        platform_id = platform[0]
        smartcontexts = api_get_smartcontext_from_platform(platform_id)
        list_smartcontexts.extend(smartcontexts)

    return list_smartcontexts





if __name__ == "__main__":
    # x = api_get_all_metric()
    # x = api_get_all_thing()
    # x = api_get_all_source()
    # x = api_get_all_platform()
    # x = api_get_all_smartcontext()
    # x = api_get_metric_id_from_metric_attribute('metric_id_1')
    # x = api_get_thing_id_from_thing_attribute('Temperature')
    # x = api_get_source_id_from_source_attribute('active')
    # x = api_get_platform_id_from_platform_attribute('8080')
    # x = api_get_smartcontext_id_from_smartcontext_attribute('HPCC')
    # x = api_get_datapoint_from_metric('metric_id_1')
    # x = api_get_metric_from_source('source_id_1')
    # x = api_get_source_from_metric('metric_id_1')
    # x = api_get_source_from_platform('platform_id_1')
    # x = api_get_platform_from_source('source_id_1')
    # x = api_get_thing_from_source('source_id_1')
    # x = api_get_source_from_thing('source_id_1')
    # x = api_get_platform_from_smartcontext('smartcontext_id_1')
    # x = api_get_smartcontext_from_platform('platform_id_6')
    # x = api_get_sub_smartcontext_from_parent_smartcontext('parent_parent_smartcontext_id_1')
    # x = api_get_parent_smartcontext_from_sub_smartcontext('smartcontext_id_2')
    # x = api_get_datapoint_from_source('source_id_1')
    # x = api_get_datapoint_from_thing('source_id_1')
    # x = api_get_datapoint_from_platform('platform_id_1')
    # x = api_get_datapoint_from_smartcontext('parent_parent_smartcontext_id_1')
    # x = api_get_metric_from_thing('source_id_1')
    # x = api_get_metric_from_platform('platform_id_1')
    # x = api_get_metric_from_smartcontext('smartcontext_id_1')
    # x = api_get_thing_from_platform('platform_id_1')
    # x = api_get_thing_from_smartcontext('smartcontext_id_1')
    # x = api_get_source_from_smartcontext('smartcontext_id_1')
    # x = api_get_platform_from_metric('metric_id_1')
    # x = api_get_platform_from_thing('source_id_6')
    # x = api_get_smartcontext_from_source('source_id_6')
    # x = api_get_smartcontext_from_thing("source_id_6")
    # x = api_get_smartcontext_from_metric('metric_id_10')


    print (x)