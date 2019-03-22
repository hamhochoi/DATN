from language.statement import Statement
from language.condition import Condition


class Query(Statement):

    def __init__(self):
        Statement.__init__()


    def get_level(self, value):
        """Get level 

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
        if (from_value not in self.list_ontology_object)# and (from_value not in self.list_ident):
            return False
        else:
            return True


    def check_select_from(self, select_value, from_value):
        """Check if select_value isn't at higher level than from value

        Return : True if select_value isn't at higher level than from value
                 False if otherwise
        """
        select_level = self.get_level(select_value)
        from_level   = self.get_level(from_value)

        if (select_level <= from_level):      # If selecdt_level == from_level, \ 
            return True                       #--> Select ontology's attribute from ontology Object
        else:
            return False
        

    def get_select_from_result(self, select_value, from_value):
        """Implement select Object from Object
        
        Call API to query DB to get result.

        Return: (Object) The result of select...from query
        """
        pass

    
    def check_where_condition(self, select_from_query_result, select_value, where_value):
        """Check if select_value at higher level than where_value

        Args:
            select_from_query_result: (Object)   Result object of select...from query
            select_value            : (str)      select query's parameter
            where_value             : (str)      where query's parameter

        Return 
            True if select_value at higher
        """


    def query(self, select_value, from_value, where_value):
        """Parse the statement, check if arguments are valid
           
        Return: True if arguments are valid
                False if *select_value is higher level than from_value 
                         *or where_condition is not satisfy
        """

        select_check = self.check_select(select_value)
        from_check   = self.check_from(from_value)
        
        if (select_check is True and from_check is True):
            select_from_check = self.check_select_from(select_value, from_value)

            # If select_level and from_level are valid
            # Get select ... from query result
            if (select_from_check is True):
                select_from_query_result = self.get_select_from_result(select_value, from_value)
                
                # Check filter condition (where parameter)
                check_where_result = self.check_where_condition(select_from_query_result, \
                                                                select_value, where_value)
                


                

