from nuts.engines.relays import base_relay
from .modeling import Client

class splus_relay (base_relay):
    def __init__ (self,*args, **wargs):
        super().__init__(*args, **wargs)
        self.C = Client(self.token)
        self._connection = None 
    @property
    def connected(self):
        if self._connection :
            return True
        return False


    def connect(self):
        if not self.connected:
            self._connection = self.C.get_messages()
    
    def disconnect(self):
        del self._connection
        self._connection = None
    
    def listen_on_message (self):
        self.connect ()
        return self._connection.__next__() #type: ignore
    
    def __iter__(self):
        self.connect()
        return self._connection




        