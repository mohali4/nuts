
from nuts.modeling.messeges.model import reqMSG
from .subclasses import _engine_subclass
from .relays import base_relay
from .relays.management import relay_manager

class base_engine(_engine_subclass) :

    relay_model = base_relay

    def __init__ (self, *args, **wargs):
        
        self.relays = relay_manager()

        super().__init__(*args, **wargs)


    def relay (self,token) -> base_relay :
        try:
            return self.relays[token]
        except:
            self.relays.append(self.relay_model(token))
        return self.relay(token)


    @property
    def name(self):
        if type(self) == base_engine :
            return "__base__"
        raise Exception(f'You should to create name for your engine_model!')

    @property
    def id(self):
        return self.name


    @classmethod   
    def is_that_me (cls, name:str):
        if not isinstance(name, str):
            raise Exception(f"I want str because name arg, not {str(type(name))}.")
        if name == cls.name:
            return True
        return False


    @property
    def prefix (self):
        raise Exception(f'Set prefix for your engine model ( {type(self),__name__} ).')


    def keyboard_dump(self, kb):
        from json import dumps
        return dumps(kb)


    def Is_this_my_user (self, __userID):
        import re
        matchs = re.findall(f'^({self.prefix})://.+$',__userID)
        if len(matchs) != 1 :
            if len(matchs) == 0 :
                return False
            raise Exception(f'Uncorrect userID')
        return True


    def calc_userID (self, __userID) -> str :
        return f'{self.prefix}://{__userID}'


    def __convert_msg_to_nuts(self,msg) -> reqMSG:
        return msg


    def __listen_on_messege (self,token):
        return self.relay(token).listen_on_message()

    def listen_on_messege (self,token) -> reqMSG:
        return self.__convert_msg_to_nuts(self.__listen_on_messege(token))


