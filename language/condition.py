from language import Languague
from expression import Expression
import json


class Condition(Languague):
    ###################################
    # CONDITION PARSER

    def __init__(self):
        Languague.__init__(self)

    
    def condition_parser(self):
        pass

    
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


    def check_compare_field(self, compare_json):
        """ Check compare field syntax and sematic
        """
        compare_json = json.loads(compare_json)
        try:
            keyword = compare_json['keyword']
            comparator = compare_json['comparator']
            expression = compare_json['expression']
        except Exception as e:
            print (e)
            return False

        is_keyword_valid = self.check_keyword_syntax_valid(keyword)
        if (is_keyword_valid == False):
            return False

        is_comparator_valid = self.check_comparator_syntax_valid(comparator)
        if (is_comparator_valid == False):
            return False

        is_expression_valid, expression_value = Expression().check_expression_valid(expression)
        if (is_expression_valid == False):
            return False

        return True


    def check_logic_field(self, logic_json):
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
            print (e)
            return False

        is_operation_valid = self.check_operator(operation)
        if (is_operation_valid == False):
            return False

        is_condition_1_valid = self.check_condition_syntax_valid(json.dumps(condition_1))
        if (is_condition_1_valid == False):
            return False
        
        is_condition_2_valid = self.check_condition_syntax_valid(json.dumps(condition_2))
        if (is_condition_2_valid == False):
            return False

        return True


    def check_in_bracket_field(self, in_bracket_json):
        """Check if in_bracket_json is syntax valid
        """
        in_bracket_json = json.loads(in_bracket_json)
        try:
            condition = in_bracket_json['condition']
        except Exception as e:
            print (e)
            return False

        is_condition_valid = self.check_condition_syntax_valid(json.dumps(condition))
        # print (is_condition_valid)
        if (is_condition_valid == False):
            return False

        return True


    def check_condition_syntax_valid(self, condition):
        """ Check if condition is syntax valid

        Valid syntax: There is one and only one of those field (in_bracket, logic, compare) in each condition.

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
            print (e)
            return False

        if (compare != {}):
            is_compare_valid = self.check_compare_field(json.dumps(compare))
            # print (is_compare_valid)
            if (is_compare_valid == False):
                return False
        elif (logic != {}):
            is_logic_valid = self.check_logic_field(json.dumps(logic))
            # print (is_logic_valid)
            if (is_logic_valid == False):
                return False
        elif (in_bracket != {}):
            is_in_bracket_valid = self.check_in_bracket_field(json.dumps(in_bracket))
            # print (is_in_bracket_valid)
            if (is_in_bracket_valid == False):
                return False
        else:
            # Both 3 fielld == {}
            # --> return False 
            return False
        return True


if __name__ == "__main__":
    condition = Condition()
    compare = {
        "keyword" : "metric_global_id",
        "comparator" : "=",
        "expression" : "metric_id_1"
    }

    logic = {
        "operation" : "AND",
        "condition_1" : {
            "compare" : {
                "keyword" : "metric_id",
                "comparator" : "=",
                "expression" : "metric_id_1"
            },
            "logic" : {},
            "in_bracket" : {}
        }, 
        "condition_2" : {
            "compare" : {
                "keyword" : "platform_id",
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
                        "keyword" : "metric_id",
                        "comparator" : "=",
                        "expression" : "metric_id_1"
                    },
                    "logic" : {},
                    "in_bracket" : {}
                }, 
                "condition_2" : {
                    "compare" : {
                        "keyword" : "platform_id",
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
            "keyword" : "metric_global_id",
            "comparator" : "=",
            "expression" : "metric_id_1"
        },
        "logic" : {}, 
        "in_bracket" : {}
    }

    condition_json_2 = {
        "compare" : {},
        "logic" : {
            "operation" : "AND",
            "condition_1" : {
                "compare" : {
                    "keyword" : "metric_global_id",
                    "comparator" : "=",
                    "expression" : "metric_id_1"
                },
                "logic" : {},
                "in_bracket" : {}
            }, 
            "condition_2" : {
                "compare" : {
                    "keyword" : "platform_id",
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
                            "keyword" : "metric_global_id",
                            "comparator" : "=",
                            "expression" : "metric_id_1"
                        },
                        "logic" : {},
                        "in_bracket" : {}
                    }, 
                    "condition_2" : {
                        "compare" : {
                            "keyword" : "platform_id",
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
                                    "keyword" : "source_global_id",
                                    "comparator" : "=",
                                    "expression" : "source_id_1"
                                }
                            },
                            "condition_2" : {
                                "logic" : {},
                                "in_bracket" : {},
                                "compare" : {
                                    "keyword" : "source_global_id",
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
                    "keyword" : "source_global_id",
                    "comparator" : "=",
                    "expression" : "source_id_3"
                },
                "logic" : {},
                "in_bracket" : {}
            }
        },
        'in_bracket' : {}
    }
    # result = condition.check_compare_field(json.dumps(compare)) 
    # result = condition.check_logic_field(json.dumps(logic)) 
    # result = condition.check_compare_field(json.dumps(in_bracket)) 
    # result = condition.check_condition_syntax_valid(json.dumps(condition_json_1))
    # result = condition.check_condition_syntax_valid(json.dumps(condition_json_2))
    # result = condition.check_condition_syntax_valid(json.dumps(condition_json_3))
    result = condition.check_condition_syntax_valid(json.dumps(condition_json_4))
    print (result)