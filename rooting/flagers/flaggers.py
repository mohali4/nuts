from dataclasses import is_dataclass
from nuts.modeling import nuts_base_model as __base_model
from nuts.rooting.paths import classic_path as __classic_path , base_path  , place_in_path 
#from nuts.config import function



class __base_flagger(__base_model) :


    def path_placement (self, path):
        return place_in_path(path)

    def __init__ (self,root_path,root_model,**wargs):
        self.set_flag(root_path)
        self.root_model = root_model
        super().__init__(**wargs)
    
    def set_flag(self,__path):
        self.root_path = self.path_placement(__path) # type:base_path
        return self
    
    def decorate (self, _func):
        self.root_model(self.root_path, _func)
        return _func
    
    
    def __call__ (self, item):
        if isinstance(item, str):
            return self.fork(item)
        elif hasattr(item,'__call__'):
            return self.decorate(item)

    def __str__(self):
        return str(self.root_path)

    def fork(self, path):
        return self.copy().set_root_path(path) #type: ignore


class classic_flagger (__base_flagger):
    
    def __init__ (self,*args,**wargs):
        self.classic_cashe = True
        super().__init__(*args,**wargs)

    @property
    def is_classic (self):
        if self.classic_cashe :
            if is_classic(self) :
                return True
            self.classic_cashe = False
        return False


    def fork (self,path):
        new_path = self.root_path+path if self.is_classic and is_classic(path) else path
        return super().fork(new_path)





def is_classic(path):
    if __classic_path.can_I_match(path.__str__()):
        return True
    return False


'''

you are one of my best friends...hope that until the end of your life...
one behalf of someone who likes PHP
thanks

It was my best friend last message...

'''


