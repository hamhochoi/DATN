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
        # print (_)

        list_result = []
        if (select_level == 0): # smartcontext
            if (select_value == "SmartContext"):
                for result in results:
                    list_result.append(result)
            elif (select_value == "SmartContextId"):
                for result in results:
                    list_result.append(result["SmartContextId"])
            elif (select_value == "SmartContextName"):
                for result in results:
                    list_result.append(result["SmartContextName"])
            elif (select_value == "ParentSmartContextId"):
                for result in results:
                    list_result.append(result["ParentSmartContextId"])
            elif (select_value == "SubSmartContextId"):
                for result in results:
                    list_result.append(result["SubSmartContextId"])
            elif (select_value == "HasPlatform"):
                for result in results:
                    list_result.append(result["HasPlatform"])
            else:
                return False, None
        elif (select_level == 1):   # platform
            if (select_value == "Platform"):
                for result in results:
                    list_result.append(result)
            elif (select_value == "PlatformId"):
                for result in results:
                    list_result.append(result["PlatformId"])
            elif (select_value == "PlatformName"):
                for result in results:
                    list_result.append(result["PlatformName"])
            elif (select_value == "PlatformType"):
                for result in results:
                    list_result.append(result["PlatformType"])
            elif (select_value == "PlatformHost"):
                for result in results:
                    list_result.append(result["PlatformHost"])
            elif (select_value == "PlatformPort"):
                for result in results:
                    list_result.append(result["PlatformPort"])
            elif (select_value == "PlatformStatus"):
                for result in results:
                    list_result.append(result["PlatformStatus"])
            elif (select_value == "HasSource"):
                for result in results:
                    list_result.append(result["HasSource"])
            else:
                return False, None
        elif (select_level == 2):
            if (select_value == "Source"):
                for result in results:
                    list_result.append(result)
            elif (select_value == "SourceId"):
                for result in results:
                    list_result.append(result["SourceId"])
            elif (select_value == "EndPoint"):
                for result in results:
                    list_result.append(result["EndPoint"])
            elif (select_value == "SourceStatus"):
                for result in results:
                    list_result.append(result["SourceStatus"])
            elif (select_value == "Description"):
                for result in results:
                    list_result.append(result["Description"])
            elif (select_value == "SourceType"):
                for result in results:
                    list_result.append(result["SourceType"])
            elif (select_value == "Label"):
                for result in results:
                    list_result.append(result["Label"])
            elif (select_value == "LocalId"):
                for result in results:
                    list_result.append(result["LocalId"])
            elif (select_value == "HasMetric"):
                for result in results:
                    list_result.extend(result["HasMetric"])
            else:
                return False, None
        elif (select_level == 4):
            if (select_value == "Metric"):
                for result in results:
                    list_result.append(result)
            elif (select_value == "MetricId"):
                for result in results:
                    list_result.append(result["MetricId"])
            elif (select_value == "MetricName"):
                for result in results:
                    list_result.append(result["MetricName"])
            elif (select_value == "MetricType"):
                for result in results:
                    list_result.append(result["MetricType"])
            elif (select_value == "Unit"):
                for result in results:
                    list_result.append(result["Unit"])
            elif (select_value == "MetricDomain"):
                for result in results:
                    list_result.append(result["MetricDomain"])
            elif (select_value == "MetricStatus"):
                for result in results:
                    list_result.append(result["MetricStatus"])
            elif (select_value == "MetricLocalId"):
                for result in results:
                    list_result.append(result["MetricLocalId"])
            elif (select_value == "CanSetState"):
                for result in results:
                    list_result.append(result["CanSetState"])
            elif (select_value == "HasDatapoint"):
                for result in results:
                    list_result.append(result["HasDatapoint"])
            else:
                return False, None
        elif (select_level == 5):
            if (select_value == "DataPoint"):
                for result in results:
                    list_result.append(result)
            elif (select_value == "time"):
                for result in results:
                    list_result.append(result["time"])
            elif (select_value == "value"):
                for result in results:
                    list_result.append(result["value"])
            elif (select_value == "DataType"):
                for result in results:
                    list_result.append(result["DataType"])
            elif (select_value == "DataPointId"):
                for result in results:
                    list_result.append(result["DataPointId"])
            else:
                return False, None

        return True, list_result


if __name__ == "__main__":
    with open(os.getcwd()  + '/utils/statement_compare.json', 'r') as json_file:
        query = json.load(json_file)
        select_values = query['select'].split(",")
        # print (select_values)
        where_condition = query['where']['condition']

        for select_value in select_values:
            _, resutl = Query().query(select_value, where_condition)
            print (resutl)

    