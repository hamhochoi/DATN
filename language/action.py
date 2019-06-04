from language import Languague
from Fog.Filter.Filter import Filter


class Action(Languague):
    ###################################
    # ACTION PARSER

    def __init__(self):
        Languague.__init__(self)
        self.filter = Filter(broker_fog="broker.hivemq.com")


    def api_set_state(self, topic, message):        
        self.filter.api_set_state(topic, message)
