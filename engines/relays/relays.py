from nuts.modeling.protos import nuts_base_model
from .subclasses import relay_subclass

class base_relay (nuts_base_model,relay_subclass):

    def __init__ (self,token):
        self.token = token
    
    def connect (self):
        raise

    def disconnect (self):
        raise

    def reconnect (self):
        if self.connected : self.disconnect()
        self.connect()
    
    @property
    def connected(self):
        raise
    
    def listen_on_message(self):
        raise

    class relay_iterator :
        def __init__ (self,next_func,args=[],wargs={},stone_mode=False):
            self.func = next_func
            self.args = args
            self.wargs = wargs
            self.stone = stone_mode

        def __next__(self):
            try:
                return self.func(*self.args,**self.wargs)
            except:
                if not self.stone :
                    raise StopIteration()
                return self.__next__()

    def __iter__ (self):
        return self.relay_iterator(self.listen_on_message)
    
    