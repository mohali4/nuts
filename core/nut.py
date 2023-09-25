import threading
from nuts.modeling import nuts_base_model, List
from nuts.bots import bot
from nuts.rooting import flag_pool
from nuts.rooting.globals import pool as global_pool

from ..engines.management import engines
from .handle import base_msg_handler

class base_nut (nuts_base_model):
    handler = base_msg_handler

    def __init__ (self,bot:bot, *pools:flag_pool):

        self.bot = bot
        self.pools = List(pools)
        self.pools.append_if_not_exists(global_pool)

    @property
    def threads (self):
        return  self.handler.threads

    def handle (self,msg):
        thread_num = self.threads.len
        handler = self.handler(msg, self)
        handler.start()

    def __call__ (self,*args,**wargs):
        return self.run(*args,**wargs)


    def run (self):
        from nuts.config.log import recieve_message
        while True :
            try :
                msg = self.bot.listen_on_message()
                recieve_message()
                self.handle(msg)


            except :
                pass

