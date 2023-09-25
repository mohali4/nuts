from nuts.core.threads import thread_manager
from nuts.modeling import nuts_base_model
from .argaments import generate_argaments
import threading 

class  base_msg_handler(nuts_base_model) :
    threads = thread_manager()
    def __init__ (self, msg, nut):
        self.msg = msg
        self.nut = nut 
        self.id = len(self.cls.threads)
        self.cls.threads.append(self)
        self.thread = threading.Thread(target=self._handle_msg_thread)

    def start (self, *args, **wargs):
        self.thread._args = args #type: ignore
        self.thread._kwargs = wargs #type: ignore
        self.thread.start()       

    
    def finished (self):
        ...

    def _handle_msg_thread (self):
        from nuts.core.root import root
        flag = root(self.msg,self.nut.pools)
        args, wargs = generate_argaments(self.msg)


        try:
            flag.func(self.msg,*args,**wargs)
        except:
            ...

        self.finished()
