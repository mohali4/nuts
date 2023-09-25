

class base_pattern(str) :
    description = "Enter your model description here."
    pattern = r"[E,e]{1}nter\wyour\wr(e[g,x]){2}\wpat{2}ern\where{1}.?" # Just was a jok :)

    def __change_argaments(cls_self,*args,**wargs): #type: ignore
        if 'pattern' in wargs:
            args[0] = wargs['pattern'] #type: ignore
        wargs = {}
        return args, wargs
    
    
    def __init__(self,*args,**wargs):
        self.over = wargs.get('over',False)
        args, wargs = self.__change_argaments(*args,**wargs)
        str.__init__(*args, **wargs)
    
    def __new__(cls,*args,**wargs):
        args, wargs = cls.__change_argaments(*args,**wargs)
        return str.__new__(cls,*args,**wargs)

    @classmethod
    def __str__(cls):
        return cls.pattern
    
    def match (self,string:str,over=False):
        import re
        if over or self.over :
            pattern = f'^{str(self)}$'
        else:
            pattern = str(self)
        return re.match(pattern,string)

    def find (self,string:str,over=False):
        import re
        if over or self.over :
            pattern = f'^{str(self)}$'
        else:
            pattern = str(self)
        return re.findall(pattern,string)[0]

def pattern_decorate (pattern_model:type)->base_pattern:
    if not issubclass(pattern_model,base_pattern) :
        raise Exception(f'{pattern_model.__name__} is not instance pattern')
    pattern = pattern_model(str(pattern_model))
    
    
    return pattern

