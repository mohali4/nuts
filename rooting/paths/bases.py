
from nuts.modeling import nuts_base_model as __base_model


class base_path (__base_model) :
    def __init__(self,path:str,*args,**wargs):
        self.path = path
        super().__init__(*args,**wargs)

    def can_root_to_me (self,path):
        if path == self.path:
            return True
        return False
    
    def __str__ (self):
        return self.path

    @classmethod
    def pattern(cls) -> str:
        if 1<2 :
            raise Exception(f"Can not use this pattern in base_path you need to create a pattern val for your class ({cls.__name__})")
        return ''

    @classmethod
    def can_I_match (cls, __path:str):
        __path = str(__path)
        import re 
        pattern = cls.pattern if isinstance(cls.pattern,str) else cls.pattern.decode() if  isinstance(cls.pattern,bytes) else str(cls.pattern)
        if re.match(pattern ,__path):
            return True
        return False
    
    def Can_it_root (self, path):
        if path == self.path :
            return True
        return False
"""    
    def __new__(cls,arg0,*args,**wargs):
        if isinstance(arg0,base_path):
            obj = arg0.copy()
        else:
            obj = super(base_path,cls).__new__(cls)
        return obj
"""
