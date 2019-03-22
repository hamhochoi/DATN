class Languague():
    def __init__(self):
        self.list_key_words = [
            'SmartContext', \
                'smart_context_id', 'smart_context_name', \
                'is_sub_smart_context_of', 'has_sub_smart_context', \
                'has_platform', \
            'Platform', \
                'platform_id', \
                'platform_name', \
                'has_source', \
            'Source', \
                'source_global_id', \
                'source_local_id', \
                'source_name', \
                'has_thing', \
                'has_metric', \
                'has_type', \
            'Thing', \
                'thing_id', \
                'thing_name', \
            'Metric', \
                'metric_global_id', \
                'metric_local_id', \
                'metric_name', \
                'metric_status', \
                'can_set_state', \
                'has_unit', \
            'DataPoint', \
                'belong_metric', \
                'has_time_collect', \
                'has_value', \
                'has_data_type'
        ]

        """Just ignore ident for now

        self.list_ident = []
        """
        self.smart_context_level = [
            "SmartContext", "smart_context_id", \
            "smart_context_name", "is_sub_smart_context_of", \
            "has_sub_smart_context", "has_platform" \
        ]
        self.platform_level = [
            "Platform", "platform_id", \
            "platform_name", "has_source" \
        ]
        self.source_level = [
            "Source", "source_global_id", \
            "source_local_id", "source_name", \
            "has_thing", "has_metric", "has_type" \
        ]
        self.thing_level = [
            "Thing", "thing_id", "thing_name" \
        ]
        self.metric_level = [
            "Metric", "metric_global_id", \
            "metric_local_id", "metric_name", \
            "metric_status", "can_set_state", \
            "has_unit" \
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


    def get_key_word_from_db(self):
        pass




    def query_parser(self):
        pass


    def rule_parser(self):
        pass


    def assignment_parser(self):
        pass
