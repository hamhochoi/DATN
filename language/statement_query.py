# from language.statement import Statement
# from language.condition import Condition
# from language.api import *
import json
from statement import Statement
from condition import Condition
from api import *


class Query(Statement):

    def __init__(self):
        Statement.__init__(self)


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


    def check_syntax_query(self, query):
        try:
            select_value    = query['select']
            where_condition = query['where']

            # Check 'select' field
            if (select_value == '' or select_value == None):
                return False
            
            # Check 'where' field
            result = self.check_syntax_where(where_condition)
            return result

        except:
            return False


    def check_syntax_where(self, where_condition):
        """ Check if "where" query is valid 

        return False if where_condition doesn't have (compare, logic, in_bracket) fields.
               True otherwises
        """

        try:
            compare_value    = where_condition['compare']
            logic_value      = where_condition['logic']
            in_bracket_value = where_condition['in_bracket']

            return True
        except:
            return False


    def check_select(self, select_value):
        """Check if select_value is a keyword

        Return True if select_value is in list_keyword
               False otherwise
        """

        if (select_value not in self.list_key_words):
            return False
        else:
            return True

    
    # def check_from(self, from_value): 
    #     """Check if from_value is in list_keyword or in ident_list or not

    #     Return True if from_value is in list_keyword or ident_list
    #            False otherwise
    #     """
    #     if (from_value not in self.list_ontology_object)# and (from_value not in self.list_ident):
    #         return False
    #     else:
    #         return True
        

    def get_select_result(self, select_value, from_value):
        """Implement select Object from Object
        
        Call API to query DB to get result.

        Return: (Object) The result of select...from query
        """
        select_level = self.get_level(select_value)

        # Handle SELECT.
        if (select_level == 0): # smartcontext
            results = api_get_all_smartcontext()
        elif (select_level == 1):
            results = api_get_all_platform()
        elif (select_level == 2):
            results = api_get_all_source()
        elif (select_level == 3):
            results = api_get_all_thing()
        elif (select_level == 4):
            results = api_get_all_metric()
        elif (select_level == 5):
            results = api_get_all_datapoint()


    def get_where_result(self, select_value, where_condition):
        pass



















    def check_where_condition(self, select_from_query_result, select_value, where_value):
        """TODO
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
                


                


if __name__ == "__main__":
    with open('../utils/query_format.json', 'r') as json_file:
        query = json.load(json_file)
        # print (query)
    Query().check_syntax_query(query)