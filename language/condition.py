#!/usr/bin/python
# -*- coding: utf-8 -*-
from language import Languague
from expression import Expression
import json
from api import *
import traceback


class Condition(Languague):
    ###################################
    # CONDITION PARSER

    def __init__(self):
        Languague.__init__(self)


    def intersection(self, a, b):
        # get intersect 2 lists
        result = []
        for x in a:
            if (x in b):
                result.append(x)

        return result


    def union(self, a, b):
        # get union of 2 lists
        result = a
        for x in b:
            if (x not in a):
                result.append(x)

        return result


    def check_keyword_syntax_valid(self, keyword):
        if (keyword in self.list_key_words):
            return True
        else:
            return False

    
    def check_comparator_syntax_valid(self, comparator):
        if (comparator in self.list_comparator):
            return True
        else:
            return False


    def check_operator(self, operator):
        if (operator in self.list_logic):
            return True
        else:
            return False


    def check_compare_field(self, compare_json, object_to_check_level):
        """ Check compare field syntax and sematic

        Params: 
            compare_json    : a condition (in json format)
            list_object_to_check_level : level of object to check the condition (string)

        Return: 
            True, result : if syntax and semantic valid
                           result is a list of ontology object
            False, None: if syntax invalid
        """
        compare_json = json.loads(compare_json)
        try:
            keyword = compare_json['keyword']
            comparator = compare_json['comparator']
            expression = compare_json['expression']
            # print (keyword)
            # print (expression)
            # print (comparator)
        except Exception as e:
            traceback.print_exc()
            return False, None

        # CHECK SYNTAX
        is_keyword_valid = self.check_keyword_syntax_valid(keyword)
        if (is_keyword_valid == False):
            return False, None

        is_comparator_valid = self.check_comparator_syntax_valid(comparator)
        if (is_comparator_valid == False):
            return False, None

        is_expression_valid, expression_value = Expression().check_expression_valid(expression)
        if (is_expression_valid == False):
            return False, None


        # CHECK SEMANTIC
        keyword_level = self.get_level(keyword)

        # print (comparator)
        # print ("keyword level: {}".format(keyword_level))
        # print ("object level : {}".format(object_to_check_level))

        if (comparator == "="):            
            if (keyword_level == 0):    # keyword == smartcontext
                if (object_to_check_level == 0):    # Need to get smartcontext from smartcontext_attr
                    result = api_get_smartcontext_from_smartcontext_attr(keyword, expression)
                elif (object_to_check_level == 1):  # Need to get platform from smartcontext_attr
                    result = api_get_platform_from_smartcontext(keyword, expression)
                elif (object_to_check_level == 2):  # Need to get source from smartcontext_attr
                    result = api_get_source_from_smartcontext(keyword, expression)
                elif (object_to_check_level == 3):  # Need to get thing from smartcontext_attr
                    result = api_get_thing_from_smartcontext(keyword, expression)
                elif (object_to_check_level == 4):  # Need to get metric from smartcontext_attr
                    result = api_get_metric_from_smartcontext(keyword, expression)
                elif (object_to_check_level == 5):  # Need to get datapoint from smartcontext_attr
                    result = api_get_datapoint_from_smartcontext(keyword, expression)
                else:
                    return False, None
            elif (keyword_level == 1):  # keyword == platform

                if (object_to_check_level == 0):    # Need to get smartcontext from platform_id
                    result = api_get_smartcontext_from_platform(keyword, expression)
                elif (object_to_check_level == 1):  # Need to get platform from platform_id
                    result = api_get_platform_from_platform_attr(keyword, expression)
                elif (object_to_check_level == 2):  # Need to get source from platform_id
                    result = api_get_source_from_platform(keyword, expression)
                elif (object_to_check_level == 3):  # Need to get thing from platform_id
                    result = api_get_thing_from_platform(keyword, expression)
                elif (object_to_check_level == 4):  # Need to get metric from platform_id
                    result = api_get_metric_from_platform(keyword, expression)
                elif (object_to_check_level == 5):  # Need to get datapoint from platform_id
                    result = api_get_datapoint_from_platform(keyword, expression)
                else:
                    return False, None
            elif (keyword_level == 2):  # keyword == source
                if (object_to_check_level == 0):    # Need to get smartcontext from source_attr
                    result = api_get_smartcontext_from_source(keyword, expression)
                elif (object_to_check_level == 1):  # Need to get platform from source_attr
                    result = api_get_platform_from_source(keyword, expression)
                elif (object_to_check_level == 2):  # Need to get source from source_attr
                    result = api_get_source_from_source_attr(keyword, expression)
                elif (object_to_check_level == 3):  # Need to get thing from source_attr
                    result = api_get_thing_from_source(keyword, expression)
                elif (object_to_check_level == 4):  # Need to get metric from source_attr
                    result = api_get_metric_from_source(keyword, expression)
                elif (object_to_check_level == 5):  # Need to get datapoint from source_attr
                    result = api_get_datapoint_from_source(keyword, expression)
                else:
                    return False, None
            elif (keyword_level == 3):  # keyword == thing
                if (object_to_check_level == 0):    # Need to get smartcontext from thing_attr
                    result = api_get_smartcontext_from_thing(keyword, expression)
                elif (object_to_check_level == 1):  # Need to get platform from thing_attr
                    result = api_get_platform_from_thing(keyword, expression)
                elif (object_to_check_level == 2):  # Need to get source from thing_attr
                    result = api_get_source_from_thing(keyword, expression)
                elif (object_to_check_level == 3):  # Need to get thing from thing_attr
                    result = api_get_thing_from_thing_attr(keyword, expression)
                elif (object_to_check_level == 4):  # Need to get metric from thing_attr
                    result = api_get_metric_from_thing(keyword, expression)
                elif (object_to_check_level == 5):  # Need to get datapoint from thing_attr
                    result = api_get_datapoint_from_thing(keyword, expression)
                else:
                    return False, None
            elif (keyword_level == 4):  # keyword == metric
                if (object_to_check_level == 0):    # Need to get smartcontext from metric_attr
                    result = api_get_smartcontext_from_metric(keyword, expression)
                elif (object_to_check_level == 1):  # Need to get platform from metric_attr
                    result = api_get_platform_from_metric(keyword, expression)
                elif (object_to_check_level == 2):  # Need to get source from metric_attr
                    result = api_get_source_from_metric(keyword, expression)
                elif (object_to_check_level == 3):  # Need to get thing from metric_attr
                    result = api_get_thing_from_metric(keyword, expression)
                elif (object_to_check_level == 4):  # Need to get metric from metric_attr
                    result = api_get_metric_from_metric_attr(keyword, expression)
                elif (object_to_check_level == 5):  # Need to get datapoint from metric_attr
                    result = api_get_datapoint_from_metric(keyword, expression)
                else:
                    return False, None
            elif (keyword_level == 5):  # keyword == datapoint
                if (object_to_check_level == 0):    # Need to get smartcontext from mesurement
                    result = api_get_smartcontext_from_datapoint(keyword, expression)
                elif (object_to_check_level == 1):  # Need to get platform from mesurement
                    result = api_get_platform_from_datapoint(keyword, expression)
                elif (object_to_check_level == 2):  # Need to get source from mesurement
                    result = api_get_source_from_datapoint(keyword, expression)
                elif (object_to_check_level == 3):  # Need to get thing from mesurement
                    result = api_get_thing_from_datapoint(keyword, expression)
                elif (object_to_check_level == 4):  # Need to get metric from mesurement
                    result = api_get_metric_from_datapoint(keyword, expression)
                elif (object_to_check_level == 5):  # Need to get datapoint from mesurement
                    result = api_get_datapoint_from_datapoint_attr(keyword, expression)  
                else:
                    return False, None
            else:
                return False, None
        else:   # Comparator is not "="
            return False, None

        return True, result


    def check_logic_field(self, logic_json, object_to_check_level):
        """ Check if logic_json is syntax valid
        """
        logic_json = json.loads(logic_json)
        try:
            operation = logic_json['operation']
            condition_1 = logic_json['condition_1']
            condition_2 = logic_json['condition_2']
            # print (operation)
            # print (condition_1)
            # print (condition_2)
        except Exception as e:
            traceback.print_exc()
            return False, None

        is_operation_valid = self.check_operator(operation)
        if (is_operation_valid == False):
            return False, None

        is_condition_1_valid, result_1 = self.check_condition(json.dumps(condition_1), object_to_check_level)
        if (is_condition_1_valid == False):
            return False, None
        
        is_condition_2_valid, result_2 = self.check_condition(json.dumps(condition_2), object_to_check_level)
        if (is_condition_2_valid == False):
            return False, None


        ###################################################
        ###################################################
        ## CHECK SEMANTIC

        if (is_condition_1_valid == True and \
            is_condition_2_valid == True and \
            is_operation_valid   == True
        ):
            if (operation == "AND"):
                # print (result_1)
                # print (result_2)
                result = self.intersection(result_1, result_2)
            elif (operation == "OR"):
                # result = list(set(result_1) | set(result_2))
                result = self.union(result_1, result_2)

        return True, result


    def check_in_bracket_field(self, in_bracket_json, object_to_check_level):
        """Check if in_bracket_json is syntax valid
        """
        in_bracket_json = json.loads(in_bracket_json)
        try:
            condition = in_bracket_json['condition']
        except Exception as e:
            traceback.print_exc()
            return False, None

        is_condition_valid, result = self.check_condition(json.dumps(condition), object_to_check_level)
        # print (is_condition_valid)
        if (is_condition_valid == False):
            return False, None

        return True, result


    def check_condition(self, condition, object_to_check_level):
        """ Check if condition is syntax and semantic valid

        Valid syntax: There is one and only one of those field (in_bracket, logic, compare) in each condition.

        Params:
            condition (json): condition to check
            object_to_check_level: level of object to check with the condition

        Return:
            True, result: if syntax and semantic valid
            False, None : if otherwise 
        """

        condition = json.loads(condition)
        try:
            compare = condition['compare']
            logic   = condition['logic']
            in_bracket = condition['in_bracket']
            # print (compare)
            # print (logic)
            # print (in_bracket)
            # print ("###################")
        except Exception as e:
            traceback.print_exc()
            return False, None

        if (compare != {}):
            is_compare_valid, result = self.check_compare_field(json.dumps(compare), object_to_check_level)
            # print ("check compare: ", is_compare_valid)
            if (is_compare_valid == False):
                return False, None
        elif (logic != {}):
            is_logic_valid, result = self.check_logic_field(json.dumps(logic), object_to_check_level)
            # print ("Check logic: ", is_logic_valid)
            if (is_logic_valid == False):
                return False, None
        elif (in_bracket != {}):
            is_in_bracket_valid, result = self.check_in_bracket_field(json.dumps(in_bracket), object_to_check_level)
            # print ("Check in bracket", is_in_bracket_valid)
            if (is_in_bracket_valid == False):
                return False, None
        else:
            # Both 3 fielld == {}
            # --> return False 
            return False, None

        return True, result


if __name__ == "__main__":
    condition = Condition()
    compare = {
        "keyword" : "MetricId",
        "comparator" : "=",
        "expression" : "metric_id_1"
    }

    logic = {
        "operation" : "AND",
        "condition_1" : {
            "compare" : {
                "keyword" : "MetricId",
                "comparator" : "=",
                "expression" : "metric_id_1"
            },
            "logic" : {},
            "in_bracket" : {}
        }, 
        "condition_2" : {
            "compare" : {
                "keyword" : "PlatformId",
                "comparator" : "=",
                "expression" : "platform_id_1"
            },
            "logic" : {},
            "in_bracket" : {}
        }
    }

    in_bracket = {
        "condition" : {
            "compare" : {},
            "logic" : {
                "operation" : "AND",
                "condition_1" : {
                    "compare" : {
                        "keyword" : "MetricId",
                        "comparator" : "=",
                        "expression" : "metric_id_1"
                    },
                    "logic" : {},
                    "in_bracket" : {}
                }, 
                "condition_2" : {
                    "compare" : {
                        "keyword" : "PlatformId",
                        "comparator" : "=",
                        "expression" : "platform_id_1"
                    },
                    "logic" : {},
                    "in_bracket" : {}
                }
            },
            "logic" : {}
        }
    }

    condition_json_1 = {
        "compare" : {
            "keyword" : "SmartContextName",
            "comparator" : "=",
            "expression" : "HPCC"
        },
        "logic" : {}, 
        "in_bracket" : {}
    }

    condition_json_2 = {
        "compare" : {},
        "logic" : {
            "operation" : "OR",
            "condition_1" : {
                "compare" : {
                    "keyword" : "MetricId",
                    "comparator" : "=",
                    "expression" : "metric_id_1"
                },
                "logic" : {},
                "in_bracket" : {}
            }, 
            "condition_2" : {
                "compare" : {
                    "keyword" : "PlatformId",
                    "comparator" : "=",
                    "expression" : "platform_id_1"
                },
                "logic" : {},
                "in_bracket" : {}
            }
        }, 
        "in_bracket" : {}
    }

    condition_json_3 ={
        "compare" : {},
        "logic" : {}, 
        "in_bracket" : {
            "condition" : {
                "compare" : {},
                "logic" : {
                    "operation" : "AND",
                    "condition_1" : {
                        "compare" : {
                            "keyword" : "MetricId",
                            "comparator" : "=",
                            "expression" : "metric_id_1"
                        },
                        "logic" : {},
                        "in_bracket" : {}
                    }, 
                    "condition_2" : {
                        "compare" : {
                            "keyword" : "PlatformId",
                            "comparator" : "=",
                            "expression" : "platform_id_1"
                        },
                        "logic" : {},
                        "in_bracket" : {}
                    }
                },
                "in_bracket" : {}
            }
        }
    }

    condition_json_4 = {
        "compare" : {},
        "logic" : {
            "operation" : "AND",
            "condition_1" : {
                "compare" : {},
                "logic" : {},
                "in_bracket" : {
                    "condition" : {
                        "compare" : {},
                        "in_bracket" : {},
                        "logic" : {
                            "operation" : "OR",
                            "condition_1" : {
                                "logic" : {},
                                "in_bracket" : {},
                                "compare" : {
                                    "keyword" : "SourceId",
                                    "comparator" : "=",
                                    "expression" : "source_id_1"
                                }
                            },
                            "condition_2" : {
                                "logic" : {},
                                "in_bracket" : {},
                                "compare" : {
                                    "keyword" : "SourceId",
                                    "comparator" : "=",
                                    "expression" : "source_id_2"
                                }
                            }
                        }
                    }
                }
            },
            "condition_2" : {
                "compare" : {
                    "keyword" : "value",
                    "comparator" : "=",
                    "expression" : "27"
                },
                "logic" : {},
                "in_bracket" : {}
            }
        },
        'in_bracket' : {}
    }

    # object_to_check = {
    #     'DataType': 'int',
    #     'value': "28", 
    #     'time': '2019-04-28T08:01:00Z'
    # }

    object_to_check_level = 4
    # result = condition.check_compare_field(json.dumps(compare), object_to_check) 
    # result = condition.check_logic_field(json.dumps(logic)) 
    # result = condition.check_compare_field(json.dumps(in_bracket), object_to_check_level) 
    # result = condition.check_condition(json.dumps(condition_json_1), object_to_check_level)
    # result = condition.check_condition(json.dumps(condition_json_2), object_to_check_level)
    # _, result = condition.check_condition(json.dumps(condition_json_3), object_to_check_level)
    _, result = condition.check_condition(json.dumps(condition_json_4), object_to_check_level)
    print (result)
    print (len(result))