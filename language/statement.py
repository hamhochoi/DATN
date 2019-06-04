from language import Languague

class Statement(Languague):
    ###############################
    # STATEMENT PARSER

    def __init__(self):
        Languague.__init__(self)

    def query(self):
        pass

    def rule(self):
        pass



# if __name__ == "__main__":
#     with open(os.getcwd()  + '/utils/statement_compare.json', 'r') as json_file:
#         query = json.load(json_file)
#         select_values = query['select'].split(",")
#         # print (select_values)
#         where_condition = query['where']['condition']

#         rule = query['rule']

#         for select_value in select_values:
#             _, resutl = Statement().query(select_value, where_condition)
#             print (resutl) 

#         rule = json.dumps(rule)

#         result = Statement().rule(rule)
#         print (result)