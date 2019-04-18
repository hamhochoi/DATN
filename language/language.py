class Languague():
    def __init__(self):
        self.list_key_words = [
            'SmartContext', \
                'smartcontext_id', 'smartcontext_name', \
                'sub_smartcontext_id', 'parent_smartcontext_id', \
                'platform_id', \
            'Platform', \
                'platform_id', \
                'platform_name', \
                'has_source', \
                'belong_smartcontext', \
            'Source', \
                'source_global_id', \
                'source_local_id', \
                'source_name', \
                'has_thing', \
                'has_metric', \
                'has_type', \
                'belong_platform', \
            'Thing', \
                'thing_id', \
                'thing_name', \
                'thing_belong_source', \
            'Metric', \
                'metric_global_id', \
                'metric_local_id', \
                'metric_name', \
                'metric_status', \
                'can_set_state', \
                'has_unit', \
                'metric_belong_source', \
            'DataPoint', \
                'belong_metric', \
                'has_time_collect', \
                'has_value', \
                'has_data_type'
        ]

        """Just ignore ident for now

        self.list_ident = []
        """
        self.smartcontext_level = [
            "SmartContext", "smartcontext_id", \
            "smartcontext_name", "sub_smartcontext_id", \
            "parent_smartcontext_id", "platform_id" \
        ]
        self.platform_level = [
            "Platform", "platform_id", \
            "platform_name", "has_source", \
            "belong_smartcontext" \
        ]
        self.source_level = [
            "Source", "source_global_id", \
            "source_local_id", "source_name", \
            "has_thing", "has_metric", \
            "has_type", "belong_platform" \
        ]
        self.thing_level = [
            "Thing", "thing_id", "thing_name", \
            "thing_belong_source" \
        ]
        self.metric_level = [
            "Metric", "metric_global_id", \
            "metric_local_id", "metric_name", \
            "metric_status", "can_set_state", \
            "has_unit", "metric_belong_source" \
        ]
        self.data_point_level = [
            "DataPoint", "belong_metric", \
            "has_time_collect", "has_value", \
            "has_data_type" \
        ]
        self.list_ontology_object = [
            "SmartContext", "Platform", \
            "Source", "Thing", \
            "Metric", "DataPoint" \
        ]

        self.list_comparator = [">", "<" , ">=" , "<=", "=" , "!="]
        self.list_logic = ["AND", "OR"]


    def get_key_word_from_db(self):
        pass




    def query_parser(self):
        pass


    def rule_parser(self):
        pass


    def assignment_parser(self):
        pass
