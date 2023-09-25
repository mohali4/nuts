from .modeling.protos import nuts_base_model
from nuts.engines import base_engine
from nuts.modeling.messeges import reqMSG
class bot (nuts_base_model):
    def __init__ (self,engine,token,**argv):
        from nuts.engines.find import find_engine
        self.engine = find_engine(engine)(**argv) #type: ignore
        self.token = token
    def listen_on_message(self) -> reqMSG:
        return self.engine.listen_on_messege(self.token) #type: ignore
