import json
from statement import Statement
from condition import Condition
from api import *
import os
from language import Languague 
import traceback
import requests
import random
from Fog.Filter.Filter import Filter




class Rule(Statement):
    def __init__(self):
        Statement.__init__(self)
        BROKER_CLOUD = "159.65.7.246"
        self.host_api_set_state = "http://{}:5000/api/metric".format(BROKER_CLOUD)
        self.filter_ = Filter(broker_fog="broker.hivemq.com")


    def rule(self, rule):
        """ Check Rule syntax and semantic.
            If True, create event to Rule Engine
            If False, do nothing

        Params: rule (json) : rule to check

        Return : 
            True if successfuly add rule to RuleEngine's database
            False if syntax invalid OR semantic invalid OR failed to add rule
        """
        
        # Check if rule is syntax valid
        try:
            rule = json.loads(rule)  

            # Check if field      
            if_field   = rule['if']
            datapoint_level = 5 
            check_condition_result, result = Condition().check_condition(json.dumps(if_field), datapoint_level)
            print (check_condition_result, result)


            if (check_condition_result == True and len(result) != 0):
                then_field = rule['then']
                then_field = json.dumps(then_field)
                actions = json.loads(then_field)
                action_list = []
                for action in actions:
                    metric_id = action["MetricId"]
                    platform = api_get_platform_from_metric(metric_attr="MetricId", metric_value=metric_id)[0]
                    platform_id = platform["PlatformId"]
                    topic = str(platform_id) + '/request/api_set_state'

                    value     = action["value"]                    
                    message = {
                        "header" : {},
                        "body":{
                            "MetricId"  : metric_id,
                            "new_value" : value
                        }
                    }

                    self.filter_.api_set_state(topic, json.dumps(message))
                    print ("called Quan's API")
                    time.sleep(1)
            else:
                else_field = rule['else']
                else_field = json.dumps(else_field)
                actions = json.loads(else_field)
                action_list = []
                for action in actions:
                    metric_id = action["MetricId"]
                    platform = api_get_platform_from_metric(metric_attr="MetricId", metric_value=metric_id)[0]
                    platform_id = platform["PlatformId"]
                    value     = action["value"]
                    
                    message = {
                        "header" : {},
                        "body":{
                            "MetricId"  : metric_id,
                            "new_value" : value
                        }
                    }

                    topic = str(platform_id) + '/request/api_set_state'
                    self.filter_.api_set_state(topic, json.dumps(message))
                    print ("called set state API")
            return True
        except:
            traceback.print_exc()
            return False



if __name__ == "__main__":
    with open(os.getcwd()  + '/utils/statement_format.json', 'r') as json_file:
        query = json.load(json_file)
        rule = query['rule']
        rule = json.dumps(rule)

        result = Rule().rule(rule)
        print (result)