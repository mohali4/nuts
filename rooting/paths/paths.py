from .bases import base_path
from .management import Im_path
from nuts.config.patterns import Pattern #type: ignore


@Im_path
class classic_path (base_path):

    pattern = Pattern(r"(\.[0-9,a-z,A-Z]+)", over=True) #type: ignore

    @classmethod
    def can_I_match(cls, path):
        base_check = super().can_I_match(path)
        if base_check:
            if len(path) == 0 :
                return 10
            if path[0] == '.':
                return True
        return base_check

    def __add__ (self,another):
        import re
        another = re.findall(r'\.?(.*)',str(another))[0]
        new_model = self.copy()  #type: ignore
        return new_model.set_path(f'{str(self)}.{another}') # type: ignore
        



@Im_path
class direct_path (base_path):

    pattern= Pattern(r"#[a-z,A-Z,0-9,_,\-]+", over=True) #type: ignore



@Im_path(5)
class re_path (base_path):

    pattern= Pattern(r".*")  # type: ignore

    def __init__ (self,path_pattern,*args,**wargs):
        self.path_pattern = path_pattern
        from nuts.modeling import nuts_base_model as __base
        __base.__init__(self,*args,**wargs)

    @property
    def path (self):
        return self.path_pattern
    
    def can_root_to_me(self, path):
        import re
        if re.match(self.path_pattern,path):
            return True
        return False


from .management import find_path_model

def path (__path):
    try: 
        path_model = find_path_model(__path)
    except:
        raise Exception(f"Couldn't find {__path} path_model.")
    
    return path_model(__path)
