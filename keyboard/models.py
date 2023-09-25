from .bases import base_key, base_keyboard, base_row
from nuts.modeling import nuts_base_model
from .values import root
"""
{
    'name1':'value1', # key1
    'name2':'value2'  # key2
    ...
}
"""

class key(base_key):
    def __init__(self,name,value,*args,**wargs):
        super().__init__(name,value)

class row(base_row):
    def __init__(self,dic:dict,*args,**wargs):
        nuts_base_model.__init__(self,**wargs)
        for name, value in dic.items():
            self.append(key(name,value))




class keyboard (base_keyboard):
    def __new__ (cls,*args,**wargs):
        obj = base_keyboard.__new__(cls)
        return obj
    def __init__  (self,*args,**wargs):
        if len(args):
            if len(args) == 1:
                if isinstance(args[0],list|tuple):
                    rows = args[0]
                else:
                    rows = [args[0]]
            else:
                rows = args
        else: 
            rows = []    

        for _row in rows:
            self.append(row(_row))
    @property
    def rows(self) :
        return self
    
    def row (self,num):
        return self[num]


class  KB (keyboard): ...

#KB(
# {'5':root('.5'),'s':root('f')},
# {'f':root(.g.h)}
# )
