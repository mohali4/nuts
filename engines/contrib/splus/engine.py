from nuts.engines import base_engine
from .sources import splus_file_source
from nuts.modeling.messeges import base_messege as messege, text_section, file_section, reqMSG
from .modeling import Client as SPLUSClient
from nuts.modeling.files import base_file,f
from nuts.engines.management import its_engine
from .relay import splus_relay

@its_engine
class splus_engine (base_engine):
    name = 'splus' #type: ignore
    relay_model = splus_relay

    def is_that_me (self, name:str):
        return name.lower() in  ('splus', 'soroush', 'soroush+', 'soroush_plus')
 

    def __init__ (self, *args, **wargs):
        super().__init__(*args, **wargs)

    def __convert_file_to_nuts(self,__file_url):
        return f(splus_file_source(self.token,__file_url)) #type: ignore


    def __convert_msg_to_nuts(self, __msg) -> messege:
        match __msg['TYPE']:
            case 'TEXT:':
                msg = reqMSG(
                    messege(
                        text_section(__msg['body'], main=True),
                    ),
                    userID=self.calc_userID(__msg['from']),
                    time=int(__msg['time']),
                )
            case 'IMAGE':
                msg =reqMSG( 
                messege(
                        text_section(__msg['body'], main=True),
                        file_section(self.__convert_file_to_nuts(__msg['fileUrl'])),
                    ),
                    userID=self.calc_userID(__msg['from']),
                    time=int(__msg['time']),
                )

            case _ :
                msg = __msg
        return super().__convert_msg_to_nuts(msg) #type: ignore

    def __listen_on_messege (self) :
        return super().__listen_on_messege()
    
