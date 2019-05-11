# from language.statement import Statement
# from language.condition import Condition
# from language.api import *
import json
from statement import Statement
from condition import Condition
from api import *
import os
from language import Languague 


class Query(Statement):
    def __init__(self):
        Statement.__init__(self)
        

    def query(self, select_value, where_condition):
        """Implement select Object from Object
        Call API to query DB to get result.

        Params:
            select_value    : string _ one/many attribute want to select
            where_condition : json   _ filter condition

        Return: (Object) The result of select...from query
        """
        # Handle SELECT.
        select_level = self.get_level(select_value)
        _, results = Condition().check_condition(json.dumps(where_condition), select_level)
        # print (results)

        list_result = []
        if (select_level == 0): # smartcontext
            if (select_value == "SmartContextId"):
                for result in results:
                    list_result.append(result[0])
            elif (select_value == "SmartContextName"):
                for result in results:
                    list_result.append(result[1])
            elif (select_value == "ParentSmartContextId"):
                for result in results:
                    list_result.append(result[2])
            elif (select_value == "SubSmartContextId"):
                for result in results:
                    list_result.append(result[3])
            elif (select_value == "PlatformId"):
                for result in results:
                    list_result.append(result[4])
            else:
                return False, None
        elif (select_level == 1):   # platform
            if (select_value == "PlatformId"):
                for result in results:
                    list_result.append(result[0])
            elif (select_value == "PlatformName"):
                for result in results:
                    list_result.append(result[1])
            elif (select_value == "PlatformType"):
                for result in results:
                    list_result.append(result[2])
            elif (select_value == "PlatformHost"):
                for result in results:
                    list_result.append(result[3])
            elif (select_value == "PlatformPort"):
                for result in results:
                    list_result.append(result[4])
            elif (select_value == "PlatformStatus"):
                for result in results:
                    list_result.append(result[5])
            elif (select_value == "LastResponse"):
                for result in results:
                    list_result.append(result[6])
            else:
                return False, None
        elif (select_level == 2):
            if (select_value == "SourceId"):
                for result in results:
                    list_result.append(result[0])
            elif (select_value == "EndPoint"):
                for result in results:
                    list_result.append(result[1])
            elif (select_value == "SourceStatus"):
                for result in results:
                    list_result.append(result[2])
            elif (select_value == "Description"):
                for result in results:
                    list_result.append(result[3])
            elif (select_value == "SourceType"):
                for result in results:
                    list_result.append(result[4])
            elif (select_value == "Label"):
                for result in results:
                    list_result.append(result[5])
            elif (select_value == "PlatformId"):
                for result in results:
                    list_result.append(result[6])
            elif (select_value == "LocalId"):
                for result in results:
                    list_result.append(result[7])
            else:
                return False, None
        elif (select_level == 3):
            if (select_value == "ThingName"):
                for result in results:
                    list_result.append(result[0])
            elif (select_value == "ThingGlobalId"):
                for result in results:
                    list_result.append(result[1])
            else:
                return False, None
        elif (select_level == 4):
            if (select_value == "MetricId"):
                for result in results:
                    list_result.append(result[0])
            elif (select_value == "SourceId"):
                for result in results:
                    list_result.append(result[1])
            elif (select_value == "MetricName"):
                for result in results:
                    list_result.append(result[2])
            elif (select_value == "MetricType"):
                for result in results:
                    list_result.append(result[3])
            elif (select_value == "Unit"):
                for result in results:
                    list_result.append(result[4])
            elif (select_value == "MetricDomain"):
                for result in results:
                    list_result.append(result[5])
            elif (select_value == "MetricStatus"):
                for result in results:
                    list_result.append(result[6])
            elif (select_value == "MetricLocalId"):
                for result in results:
                    list_result.append(result[7])
            else:
                return False, None
        elif (select_level == 5):
            if (select_value == "time"):
                for result in results:
                    list_result.append(result[2])
            elif (select_value == "value"):
                for result in results:
                    list_result.append(result[1])
            elif (select_value == "DataType"):
                for result in results:
                    list_result.append(result[0])
            else:
                return False, None

        return True, list_result


if __name__ == "__main__":
    with open(os.getcwd()  + '/utils/statement_format.json', 'r') as json_file:
        query = json.load(json_file)
        select_value = query['select']
        where_condition = query['where']['condition']

        _, resutl = Query().query(select_value, where_condition)
        print (resutl)

    