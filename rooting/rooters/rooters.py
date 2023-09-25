from nuts.modeling import nuts_base_model as __base_model
from typing import List as list_t
from ..pools.pools import flag_pool
from ..pools import flag_model


class base_rooter (__base_model):
    def __init__ (self,*pools:flag_pool, **wargs):
        self.pools = pools
        __base_model.__init__(self,**wargs)
       


class default_rooter (base_rooter) :
 
    def __root (self, msg):            
        if msg.user.was_directed :
            flag = self.direct_root(msg.user.direct_path)
        else:
            flag = self.classic_root(msg.path)
        return flag

    def root (self,msg) -> flag_model:
        return self.__root(msg)

    def direct_root (self,path):
        for pool in self.pools :
            try:
                flag = pool.direct_root(path)
                if flag :
                    return flag
            except:
                ...
        raise Exception(f'Could not find {path} in { ", ".join([ str(pool) for pool in self.pools ])}' )
    
    def classic_root (self,path):
        for pool in self.pools :
            try:
                flag = pool.classic_root(path)
                if flag :
                    return flag
            except:
                ...
        raise Exception(f'Could not find {path} in {", ".join([ str(pool) for pool in self.pools ])}')
