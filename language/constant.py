from language import Languague


class Constant(Languague):
    ###################################
    # CONSTANT PARSER

    def __init__(self):
        Languague.__init__(self)


    def constant_parser(self):
        pass


    def check_constant_valid(self, constant):
        if (type(constant) is str or type(constant) is unicode):
            return True
        else:
            return False



if __name__=="__main__":
    const = Constant()
    print (const.check_constant_valid('a'))