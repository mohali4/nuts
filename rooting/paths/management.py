from nuts.modeling.management import manager
from .bases import base_path

_precedency = "__precedency_____4d5f45df"

def __can_match_to_this_path(path_model,path):
    precedency = path_model.can_I_match(path)
    if precedency is True :
        precedency = path_model.__dict__.get(_precedency,None)
        if precedency == None: precedency = True
    return precedency
__path_manager = manager(__can_match_to_this_path) #type: ignore


def Im_path (arg):
    def set (model ,num):
        setattr (model, _precedency, num)
        __path_manager.append_decorator(model)
        return model
    if isinstance(arg,int|bool):
        class setter:
            def __init__ (self,num):
                self.num = num
            def __call__ (self,cls):
                return set(cls, self.num)
        return setter(arg)
    else :
        return set(arg, None)


def find_path_model(*args, **wargs)->type :
    return __path_manager.find(*args, **wargs)

def place_in_path (__path):
    if isinstance(__path,base_path):
        return __path
    return find_path_model(__path)(__path)