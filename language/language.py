class Languague():
    def __init__(self):
        self.list_key_words = [
            'SmartContext', \
                'SmartContextId', 'SmartContextName', \
                'SubSmartContextId', 'ParentSmartContextId', \
                'HasPlatform', \
            'Platform', \
                'PlatformId', \
                'PlatformName', \
                'PlatformPort', \
                'HasSource', \
                'PlatformType', \
                'PlatformHost', \
                'PlatformStatus', \
            'Source', \
                'SourceId', \
                'LocalId', \
                'HasMetric', \
                'SourceStatus', \
                'SourceType', \
                'EndPoint', \
                'Label', \
            # 'Thing', \
            #     'ThingGlobalId', \
            #     'ThingName', \
                # 'thing_belong_source', \
            'Metric', \
                'MetricId', \
                'MetricLocalId', \
                'MetricName', \
                'MetricStatus', \
                'CanSetState', \
                'Unit', \
                'MetricType', \
                'MetricDomain', \
                'HasDatapoint', \
            'DataPoint', \
                'DataPointId', \
                'time', \
                'value', \
                'DataType'
        ]

        """Just ignore ident for now

        self.list_ident = []
        """
        self.smartcontext_level = [
            "SmartContext", "SmartContextId", \
            "SmartContextName", "SubSmartContextId", \
            "ParentSmartContextId", "HasPlatform" \
        ]
        self.platform_level = [
                'Platform', \
                'PlatformId', \
                'PlatformName', \
                'PlatformPort', \
                'HasSource', \
                'PlatformType', \
                'PlatformHost', \
                'PlatformStatus' \
        ]
        self.source_level = [
                'Source', \
                'SourceId', \
                'LocalId', \
                'HasMetric', \
                'SourceStatus', \
                'SourceType', \
                'EndPoint', \
                'Label' \
        ]
        self.thing_level = [
            "Thing", "ThingGlobalId", "ThingName"#, \
            # "thing_belong_source" \
        ]
        self.metric_level = [
                'Metric', \
                'MetricId', \
                'MetricLocalId', \
                'MetricName', \
                'MetricStatus', \
                'CanSetState', \
                'Unit', \
                'MetricType', \
                'MetricDomain', \
                'HasDatapoint' \
        ]
        self.data_point_level = [
                'DataPoint', \
                'DataPointId', \
                'time', \
                'value', \
                'DataType'
        ]
        self.list_ontology_object = [
            "SmartContext", "Platform", \
            "Source", # "Thing", \
            "Metric", "DataPoint" \
        ]

        self.list_comparator = [">", "<" , ">=" , "<=", "=" , "!="]
        self.list_logic = ["AND", "OR"]


    def get_level(self, value):
        """Get level 

        Return: 0 : if smartcontext_level
                1 : if platform_level
                2 : if source_level
                3 : if thing_level
                4 : if metric_level
                5 : if data_point_level
                -1: Error
        """
        if (value in self.smartcontext_level):
            return 0
        elif (value in self.platform_level):
            return 1
        elif (value in self.source_level):
            return 2
        elif (value in self.thing_level):
            return 3
        elif (value in self.metric_level):
            return 4
        elif (value in self.data_point_level):
            return 5
        else:
            return -1