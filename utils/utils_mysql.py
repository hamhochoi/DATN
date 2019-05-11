# import MySQLdb
# import traceback

# db = MySQLdb.connect("localhost","root","root","datn" )
# cursor = db.cursor()
# # cursor.execute("create database datn")

# # cursor.execute("SHOW databases")

# try:
#     # DROP TABLE
#     cursor.execute("drop table if exists SmartContext;")
#     cursor.execute("drop table if exists Metric;")
#     cursor.execute("drop table if exists IoTSource")
#     cursor.execute("drop table if exists Thing;")
#     cursor.execute("drop table if exists Platform;")


#     # CREATE TABLE
#     cursor.execute("create table if not exists Thing(ThingName varchar(50), ThingGlobalId varchar(50), \
#                                                     primary key (ThingGlobalId) ); ")

#     cursor.execute("create table if not exists Platform(PlatformId varchar(50), PlatformName varchar(30), \
#                                         PlatformType varchar(30), PlatformHost varchar(30), \
#                                         PlatformPort int, PlatformStatus varchar(10), \
#                                         LastResponse varchar(50), primary key (PlatformId) ) ; ")

#     cursor.execute(' create table if not exists IoTSource (SourceId varchar(50), \
#                                         EndPoint varchar(50), SourceStatus varchar(20), \
#                                         Description varchar(200), SourceType varchar(20), \
#                                         Label varchar(100), PlatformId varchar(50), \
#                                         LocalId varchar(50), primary key (SourceId), \
#                                         foreign key fk_iotsource_thing (SourceId) \
#                                         references Thing(ThingGlobalId), \
#                                         foreign key fk_iotsource_platform (PlatformId)\
#                                         references Platform(PlatformId) ); ')

#     cursor.execute(' create table if not exists Metric(MetricId varchar(150), SourceId varchar(50), \
#                                         MetricName varchar(50), MetricType varchar(20), \
#                                         Unit varchar(20), MetricDomain varchar(20), \
#                                         MetricStatus varchar(20), MetricLocalId varchar(50), \
#                                         primary key (MetricId), \
#                                         foreign key fk_metric_iotsource (SourceId)\
#                                         references IoTSource(SourceId) ); ')

#     cursor.execute(' create table if not exists SmartContext(SmartContextId varchar(50), \
#                                         SmartContextName varchar(100), ParentSmartContextId varchar(50), \
#                                         SubSmartContextId varchar(50), PlatformId varchar(50), \
#                                         primary key (SmartContextId, ParentSmartContextId, SubSmartContextId), \
#                                         foreign key fk_smartcontext_platform (PlatformId) \
#                                         references Platform(PlatformId)) ;')


#     # INSERT VALUES TO TABLES

#     # INSERT THING
#     cursor.execute(' insert into Thing (ThingName, ThingGlobalId) \
#                     values ("Temperature", "source_id_1");')
#     cursor.execute(' insert into Thing (ThingName, ThingGlobalId) \
#                     values ("Temperature", "source_id_2");')
#     cursor.execute(' insert into Thing (ThingName, ThingGlobalId) \
#                     values ("Temperature", "source_id_3");')
#     cursor.execute(' insert into Thing (ThingName, ThingGlobalId) \
#                     values ("Temperature", "source_id_4");')
#     cursor.execute(' insert into Thing (ThingName, ThingGlobalId) \
#                     values ("Temperature", "source_id_5");')
#     cursor.execute(' insert into Thing (ThingName, ThingGlobalId) \
#                     values ("Temperature", "source_id_6");')

#     # INSERT PLATFORM

#     cursor.execute(' insert into Platform (PlatformId, PlatformName, PlatformType, \
#                                         PlatformHost, PlatformPort, PlatformStatus, \
#                                         LastResponse)\
#                     values ("platform_id_1", "OpenHAB1", "string", \
#                             "0.0.0.0", "8080", "active", \
#                             "2019-04-09T07:02:49.923692Z" ) ;')

#     cursor.execute(' insert into Platform (PlatformId, PlatformName, PlatformType, \
#                                         PlatformHost, PlatformPort, PlatformStatus, \
#                                         LastResponse)\
#                     values ("platform_id_2", "OpenHAB2", "string", \
#                             "0.0.0.0", "8080", "active", \
#                             "2019-04-09T07:02:49.923692Z" ) ;')

#     cursor.execute(' insert into Platform (PlatformId, PlatformName, PlatformType, \
#                                         PlatformHost, PlatformPort, PlatformStatus, \
#                                         LastResponse)\
#                     values ("platform_id_3", "HomeAssistant3", "string", \
#                             "0.0.0.0", "8080", "active", \
#                             "2019-04-09T07:02:49.923692Z" ) ;')

#     cursor.execute(' insert into Platform (PlatformId, PlatformName, PlatformType, \
#                                         PlatformHost, PlatformPort, PlatformStatus, \
#                                         LastResponse)\
#                     values ("platform_id_4", "HomeAssistant4", "string", \
#                             "0.0.0.0", "8080", "active", \
#                             "2019-04-09T07:02:49.923692Z" ) ;')

#     cursor.execute(' insert into Platform (PlatformId, PlatformName, PlatformType, \
#                                         PlatformHost, PlatformPort, PlatformStatus, \
#                                         LastResponse)\
#                     values ("platform_id_5", "ThingBoard5", "string", \
#                             "0.0.0.0", "8080", "active", \
#                             "2019-04-09T07:02:49.923692Z" ) ;')

#     cursor.execute(' insert into Platform (PlatformId, PlatformName, PlatformType, \
#                                         PlatformHost, PlatformPort, PlatformStatus, \
#                                         LastResponse)\
#                     values ("platform_id_6", "ThingBoard6", "string", \
#                             "0.0.0.0", "8080", "active", \
#                             "2019-04-09T07:02:49.923692Z" ) ;')
#     # INSERT SOURCE

#     cursor.execute(' insert into IoTSource (SourceId, EndPoint, SourceStatus, \
#                                             Description, SourceType, Label, \
#                                             PlatformId, LocalId) \
#                     values ("source_id_1", "http://0.0.0.0:8124/api/states", "active", \
#                             "", "Thing", "", \
#                             "platform_id_1", "thing-sensor.temperature") ;')

#     cursor.execute(' insert into IoTSource (SourceId, EndPoint, SourceStatus, \
#                                             Description, SourceType, Label, \
#                                             PlatformId, LocalId) \
#                     values ("source_id_2", "http://0.0.0.0:8124/api/states", "active", \
#                             "", "Thing", "", \
#                             "platform_id_2", "thing-sensor.temperature") ;')

#     cursor.execute(' insert into IoTSource (SourceId, EndPoint, SourceStatus, \
#                                             Description, SourceType, Label, \
#                                             PlatformId, LocalId) \
#                     values ("source_id_3", "http://0.0.0.0:8124/api/states", "active", \
#                             "", "Thing", "", \
#                             "platform_id_3", "thing-sensor.temperature") ;')

#     cursor.execute(' insert into IoTSource (SourceId, EndPoint, SourceStatus, \
#                                             Description, SourceType, Label, \
#                                             PlatformId, LocalId) \
#                     values ("source_id_4", "http://0.0.0.0:8124/api/states", "active", \
#                             "", "Thing", "", \
#                             "platform_id_4", "thing-sensor.temperature") ;')

#     cursor.execute(' insert into IoTSource (SourceId, EndPoint, SourceStatus, \
#                                             Description, SourceType, Label, \
#                                             PlatformId, LocalId) \
#                     values ("source_id_5", "http://0.0.0.0:8124/api/states", "active", \
#                             "", "Thing", "", \
#                             "platform_id_5", "thing-sensor.temperature") ;')


#     cursor.execute(' insert into IoTSource (SourceId, EndPoint, SourceStatus, \
#                                             Description, SourceType, Label, \
#                                             PlatformId, LocalId) \
#                     values ("source_id_6", "http://0.0.0.0:8124/api/states", "active", \
#                             "", "Thing", "", \
#                             "platform_id_6", "thing-sensor.temperature") ;')


#     # INSERT METRIC

#     cursor.execute(' insert into Metric (MetricID, MetricName, SourceId, MetricType, \
#                                         Unit, MetricDomain, MetricStatus, MetricLocalId) \
#                     values ("metric_id_1", "Temperature", "source_id_1", "Gauge", \
#                             "*C", "sensor", "active", "metric_local_id") ;')

#     cursor.execute(' insert into Metric (MetricID, MetricName, SourceId, MetricType, \
#                                         Unit, MetricDomain, MetricStatus, MetricLocalId) \
#                     values ("metric_id_2", "Temperature", "source_id_1", "Gauge", \
#                             "*F", "sensor", "active", "metric_local_id_2") ;')
#     ##
#     cursor.execute(' insert into Metric (MetricID, MetricName, SourceId, MetricType, \
#                                         Unit, MetricDomain, MetricStatus, MetricLocalId) \
#                     values ("metric_id_11", "Temperature", "source_id_2", "Gauge", \
#                             "*C", "sensor", "active", "metric_local_id") ;')

#     cursor.execute(' insert into Metric (MetricID, MetricName, SourceId, MetricType, \
#                                         Unit, MetricDomain, MetricStatus, MetricLocalId) \
#                     values ("metric_id_12", "Temperature", "source_id_2", "Gauge", \
#                             "*F", "sensor", "active", "metric_local_id_2") ;')

#     ##
#     cursor.execute(' insert into Metric (MetricID, MetricName, SourceId, MetricType, \
#                                         Unit, MetricDomain, MetricStatus, MetricLocalId) \
#                     values ("metric_id_3", "Temperature", "source_id_1", "Gauge", \
#                             "*C", "sensor", "active", "metric_local_id") ;')

#     cursor.execute(' insert into Metric (MetricID, MetricName, SourceId, MetricType, \
#                                         Unit, MetricDomain, MetricStatus, MetricLocalId) \
#                     values ("metric_id_4", "Temperature", "source_id_1", "Gauge", \
#                             "*F", "sensor", "active", "metric_local_id_2") ;')
#     ##

#     cursor.execute(' insert into Metric (MetricID, MetricName, SourceId, MetricType, \
#                                         Unit, MetricDomain, MetricStatus, MetricLocalId) \
#                     values ("metric_id_5", "Temperature", "source_id_3", "Gauge", \
#                             "*C", "sensor", "active", "metric_local_id") ;')

#     cursor.execute(' insert into Metric (MetricID, MetricName, SourceId, MetricType, \
#                                         Unit, MetricDomain, MetricStatus, MetricLocalId) \
#                     values ("metric_id_6", "Temperature", "source_id_3", "Gauge", \
#                             "*F", "sensor", "active", "metric_local_id_2") ;')
#     ##
#     cursor.execute(' insert into Metric (MetricID, MetricName, SourceId, MetricType, \
#                                         Unit, MetricDomain, MetricStatus, MetricLocalId) \
#                     values ("metric_id_7", "Temperature", "source_id_5", "Gauge", \
#                             "*C", "sensor", "active", "metric_local_id") ;')

#     cursor.execute(' insert into Metric (MetricID, MetricName, SourceId, MetricType, \
#                                         Unit, MetricDomain, MetricStatus, MetricLocalId) \
#                     values ("metric_id_8", "Temperature", "source_id_5", "Gauge", \
#                             "*F", "sensor", "active", "metric_local_id_2") ;')

#     ###
#     cursor.execute(' insert into Metric (MetricID, MetricName, SourceId, MetricType, \
#                                         Unit, MetricDomain, MetricStatus, MetricLocalId) \
#                     values ("metric_id_9", "Temperature", "source_id_6", "Gauge", \
#                             "*C", "sensor", "active", "metric_local_id") ;')

#     cursor.execute(' insert into Metric (MetricID, MetricName, SourceId, MetricType, \
#                                         Unit, MetricDomain, MetricStatus, MetricLocalId) \
#                     values ("metric_id_10", "Temperature", "source_id_6", "Gauge", \
#                             "*F", "sensor", "active", "metric_local_id_2") ;')


#     # INSERT SMARTCONTEXT

#     cursor.execute(' insert into SmartContext (SmartContextId, SmartContextName, \
#                                                ParentSmartContextId, SubSmartContextId, \
#                                                PlatformId)\
#                      values ("parent_parent_smartcontext_id_1", "HPCC", \
#                              "", "parent_smartcontext_id_1", "platform_id_1"); ')

#     cursor.execute(' insert into SmartContext (SmartContextId, SmartContextName, \
#                                                ParentSmartContextId, SubSmartContextId, \
#                                                PlatformId)\
#                      values ("parent_smartcontext_id_1", "HPCC", \
#                              "parent_parent_smartcontext_id_1", "smartcontext_id_1", "platform_id_2"); ')

#     cursor.execute(' insert into SmartContext (SmartContextId, SmartContextName, \
#                                                ParentSmartContextId, SubSmartContextId, \
#                                                PlatformId)\
#                      values ("parent_smartcontext_id_1", "HPCC", \
#                              "parent_parent_smartcontext_id_1", "smartcontext_id_2", "platform_id_2"); ')

#     cursor.execute(' insert into SmartContext (SmartContextId, SmartContextName, \
#                                                ParentSmartContextId, SubSmartContextId, \
#                                                PlatformId)\
#                      values ("smartcontext_id_1", "HPCC", \
#                              "parent_smartcontext_id_1", "sub_smartcontext_id_1", "platform_id_3"); ')

#     cursor.execute(' insert into SmartContext (SmartContextId, SmartContextName, \
#                                                ParentSmartContextId, SubSmartContextId, \
#                                                PlatformId)\
#                      values ("smartcontext_id_2", "HPCC", \
#                              "parent_smartcontext_id_1", "sub_smartcontext_id_2", "platform_id_4"); ')

#     cursor.execute(' insert into SmartContext (SmartContextId, SmartContextName, \
#                                                ParentSmartContextId, SubSmartContextId, \
#                                                PlatformId)\
#                      values ("sub_smartcontext_id_1", "HPCC", \
#                              "smartcontext_id_1", "", "platform_id_5"); ')

#     cursor.execute(' insert into SmartContext (SmartContextId, SmartContextName, \
#                                                ParentSmartContextId, SubSmartContextId, \
#                                                PlatformId)\
#                      values ("sub_smartcontext_id_2", "HPCC", \
#                              "smartcontext_id_2", "", "platform_id_6"); ')



#     db.commit()
# except:
#     traceback.print_exc()


# results = cursor.fetchall()
# print (results)

# cursor.execute("select * from SmartContext;")
# results = cursor.fetchall()
# print (results)

# db.close()






















import MySQLdb
import traceback

db = MySQLdb.connect("localhost","root","root","datn" )
cursor = db.cursor()
try:
        
