import json
import os
import traceback
from statement_query import Query
from statement_rule import Rule



if __name__ == "__main__":
    with open(os.getcwd()  + '/utils/statement_compare.json', 'r') as json_file:
        query = json.load(json_file)
        select_values = query['select'].split(",")
        print ("Query")
        where_condition = query['where']['condition']
        for select_value in select_values:
            _, resutl = Query().query(select_value, where_condition)
            print (resutl) 
        
        print ("****************************************")
        print ("Rule")
        rule = query['rule']
        rule = json.dumps(rule)
        result = Rule().rule(rule)
        print (result)