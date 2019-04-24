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
        # Handle SELECT.
        select_level = self.get_level(select_value)
        if (select_level == 0): # smartcontext
            # results = api_get_all_smartcontext()
        elif (select_level == 1):
            # results = api_get_all_platform()
        elif (select_level == 2):
            # results = api_get_all_source()
        elif (select_level == 3):
            # results = api_get_all_thing()
        elif (select_level == 4):
            # results = api_get_all_metric()
        elif (select_level == 5):
            # results = api_get_all_datapoint()

        return results


    def get_where_result(self, select_value, where_condition):
        """
        There is only one field (of {'compare', 'logic' and 'in_bracket'})
        has value, others will = '{}'
        """

        # Check if where_condition is syntax and semantic valid
        

            

















    def check_where_condition(self, select_from_query_result, select_value, where_value):
        """TODO
        """
        



    def query(self, select_value, where_value):
        """Parse the statement, check if arguments are valid
           
        Params:
            select_value : string _ attribute want to get
                           ex: select ThingId, SmartContextName, ...
            where_value  : json   _ condition to filter the result
                           
        Return: True if arguments are valid
                False if *select_value is higher level than from_value 
                         *or where_condition is not satisfy
        """

        select_check = self.check_select(select_value)
        
        if (select_check is True):
            select_from_query_result = self.get_select_from_result(select_value, from_value)
            
            # Check filter condition (where parameter)
            check_where_result = self.check_where_condition(select_from_query_result, \
                                                                select_value, where_value)
                


                


if __name__ == "__main__":
    with open('../utils/query_format.json', 'r') as json_file:
        query = json.load(json_file)
        # print (query)
    Query().check_syntax_query(query)