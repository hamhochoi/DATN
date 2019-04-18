from language import Languague
from constant import Constant


class Term(Languague):
    ###################################
    # TERM PARSER

    def __init__(self):
        Languague.__init__(self)

        
    def term_parser(self):
        pass


    def check_term_valid(self, term):
        """ Check if term is syntax and semantic valid

        Term include 'const', '*', '/'

        return : 
                True, value of term if 'term' is valid
                False, None         if 'term' is not valid
        """

        term_stars = term.split("*")
        # IF term is const
        if (len(term_stars) == 1):  # term == const
            term_value = term_stars[0]
            is_constant = Constant().check_constant_valid(term_value)
            if is_constant == False:
                return False, None
            else:
                return True, term_value


        # IF term is not const
        for term_star_idx in range(len(term_stars)):
            term_star = term_stars[term_star_idx]
            term_splashes = term_star.split("/")
            
            for term_splash_idx in range(len(term_splashes)):
                # Check syntax
                term_splash = term_splashes[term_splash_idx]
                if (Constant().check_constant_valid(term_splash) == False):
                        return False, None
                else:
                    # Check if term_splash must be a number
                    try:
                        term_splash = float(term_splash)
                    except:
                        return False, None

                # Check semantic
                if (term_splash_idx == 0):
                    term_star_value = term_splash              
                else:
                    term_star_value = term_star_value / term_splash

            # Check semantic
            if (term_star_idx == 0):
                term_value = term_star_value
            else:
                term_value = term_value * term_star_value

        return True, term_value



if __name__=="__main__":
    term = Term()

    # term_string = '3'
    term_string = 'a'
    # term_string = '3*4'
    # term_string = '3/4'
    # term_string = '3/4*8'

    is_term_valid, term_value = term.check_term_valid(term_string)

    if is_term_valid:
        print (term_value)