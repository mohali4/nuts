
from  nuts.modeling import nuts_base_model
from .values import value as value_model

class base_key (nuts_base_model):
    def __init__ (self,name,value,**wargs):
        self.name = name
        self.value = value_model(value)
        super().__init__(**wargs)
    
    def encode(self):
        return '{'+f'"{self.name}":{self.value.encode()}'+'}'
    
    def __str__ (self):
        return self.encode()


class base_row (nuts_base_model,list):
    def encode (self):
        return f'[{",".join([item.encode() for item in self])}]'
    def __str__ (self):
        return self.encode()


class base_keyboard (nuts_base_model,list):
    def __init__(self,*rows,**wargs):
        for _row in rows :
            self.append(_row)
        nuts_base_model.__init__(**wargs)
    def __new__(cls,*args,**wargs):
        return list.__new__(cls)

    def encode (self):
        return f'[{",".join([item.encode() for item in self])}]'
 
    def __str__ (self):
        return self.encode()
