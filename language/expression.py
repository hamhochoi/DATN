from language import Languague
from term import Term


class Expression(Languague):
    ###################################
    # EXPRESSION PARSER

    def __init__(self):
        Languague.__init__(self)


    def expression_parser(self):
        pass


    def check_expression_valid(self, expression):
        """ Check if expression is syntax valid and semantic valid

        Expression contain 'term', +, -

        return : 
                False, None            if expression is not syntax valid
                True, expression value if expression is syntax valid
        """

        mark = expression[0]
        if (mark == '-'):
            # Negative number
            mark_value = -1.0
            expression = expression[1:]
        elif (mark == '+'):
            # Positive number
            mark_value = 1.0
            expression = expression[1:]
        else:
            # Not number
            mark_value = 0.0
        

        expression_pluses = expression.split('+')

        # IF Expression == Term
        if (len(expression_pluses) == 1):
            is_expression_valid, expression_value = Term().check_term_valid(expression_pluses[0])

            if (is_expression_valid == False):
                return False, None
            else:
                try:
                    # IF Term is number
                    expression_value = float(expression_value)
                    expression_value = expression_value * mark_value
                except:
                    # IF Term is string
                    pass
                return True, expression_value
        else:   # IF Expression = Term +(-) Term
            for expression_plus_idx in range(len(expression_pluses)):
                expression_plus = expression_pluses[expression_plus_idx]
                # print (expression_plus)
                expression_minuses = expression_plus.split("-")
                for expression_minus_idx in range(len(expression_minuses)):
                    expression_minus = expression_minuses[expression_minus_idx]
                    
                    # Check syntax
                    # Check if expression_minus is a Term
                    is_term_valid, term_value = Term().check_term_valid(expression_minus)
                    if (is_term_valid == False):
                        return False, None
                    else:
                        try:
                            term_value = float(term_value)
                        except:
                            return False, None

                    # Check semantic
                    if (expression_minus_idx == 0):
                        expression_plus_value = term_value
                    else:
                        expression_plus_value = expression_plus_value - term_value                

                # Check semantic
                if (expression_plus_idx == 0):
                    expression_value = expression_plus_value
                else:
                    expression_value = expression_value + expression_plus_value


            return True, expression_value



if __name__ == "__main__":
    expression = Expression()

    expression_string = 'metric_id_1'
    # expression_string = '+30'
    # expression_string = '-40.0'
    # expression_string = '3+4'
    # expression_string = '3*4+5*6-7*8+9*10-1*2'
    # print (expression)
    is_expression_valid, expression_value = expression.check_expression_valid(expression_string)
    if (is_expression_valid == True):
        print (expression_value)