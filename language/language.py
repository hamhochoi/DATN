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
    

    def get_key_word_from_db(self):
        pass


    ###############################
    # STATEMENT PARSER

    def statement(self, select_value, from_value, where_value):
        """Parse the statement, check if arguments are valid
           
        Return: True if arguments are valid
                False if *select_value is higher level than from_value 
                         *or where_condition is not satisfy
        """

        select_check = self.check_select(select_value)
        from_check   = self.check_from(from_value)
        
        if (select_check is True and from_check is True):
            select_from_check = self.check_select_from(select_value, from_value)

            # If 
            if (select_from_check is True):
                select_from_query_result = self.query_select_from(select_value, from_value)
                if ()

                

    def query_select_from(self, select_value, from_value):
        """Implement select Object from Object
        
        Call API to query DB to get result.

        Return: the result of select...from query
        """
        pass


    def query_parser(self):
        pass


    def rule_parser(self):
        pass


    def assignment_parser(self):
        pass


    def check_select(self, select_value):
        """Check if select_value is a keyword

        Return True if select_value is in list_keyword
               False otherwise
        """

        if (select_value not in self.list_key_words):
            return False
        else:
            return True

    
    def check_from(self, from_value):
        """Check if from_value is in list_keyword or in ident_list or not

        Return True if from_value is in list_keyword or ident_list
               False otherwise
        """
        if (from_value not in self.list_key_words)# and (from_value not in self.list_ident):
            return False
        else:
            return True


    def check_select_from(self, select_value, from_value):
        """Check if select_value isn't at higher level than from value

        Return : True if select_value isn't at higher level than from value
                 False if otherwise
        """

        if (from_value in self.smart_context_level):
            return True
        elif (from_value in self.platform_level):
            if (select_value in self.platform_level or \
                select_value in self.smart_context_level \
            ):
                return False
            else:
                return True
        elif (from_value in self.source_level):
            if (select_value in self.platform_level or \
                select_value in self.smart_context_level or \
                select_value in self.source_level \
            ):    
                return False
            else:
                return True
        elif (from_value in self.metric_level):
            if (select_value in self.platform_level or \
                select_value in self.smart_context_level or \
                select_value in self.source_level or \
                select_value in self.metric_level or \
                select_value in self.thing_level \
            ):    
                return False
            else:
                return True
        elif (from_value in self.thing_level):
            if (select_value in self.platform_level or \
                select_value in self.smart_context_level or \
                select_value in self.source_level or \
                select_value in self.metric_level or \
                select_value in self.thing_level \
            ):    
                return False
            else:
                return True
        elif (from_value in self.data_point_level):
            return False


    def query_select_from_where(self, select_value, where_value, select_from_query_result):
        """Check filter condition

        Return None if dont have filter condition
        """

        if (where_value != ""): # If have where condition
            check_condition_result = self.condition_parser(where_value)
            return check_condition_result
        else:                   # Dont have any where condition
            return None

    
    def check_where_condition(self, select_value, where_value):
        """Check if select_value at higher level than where_value

        Return True if select_value at higher level than where_value
               False otherwise
        """


    def check_level(self, value):
        """Check level 

        Return: 0 : if smart_context_level
                1 : if platform_level
                2 : if source_level
                3 : if thing_level
                4 : if metric_level
                5 : if data_point_level
                -1: Error
        """
        if (value in self.smart_context_level):
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
    

    ###################################
    # CONDITION PARSER
    def condition_parser(self):
        pass
    

    ###################################
    # EXPRESSION PARSER
    def expression_parser(self):
        pass


    ###################################
    # TERM PARSER
    def term_parser(self):
        pass


    ###################################
    # CONSTANT PARSER
    def constant_parser(self):
        pass


    ###################################
    # ACTION PARSER
    def action_parser(self):        
        pass



    ###################################