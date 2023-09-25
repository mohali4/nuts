
class model_name_pattern:
    pattern = r'([a-z,_]{2,8})_model'
    
    @classmethod
    def match (cls, text):
        import re
        return re.match(cls.pattern,text)

    @classmethod
    def find (cls, text):
        import re
        return re.findall(cls.pattern,text)[0]


class init_model :
    def __init__ (self, *args,**wargs):
        for name , value in wargs.items():
            setattr(self,name,value)



class set_model :

    def __get_set_attribute (self, name:str):
        if name[:4] == 'set_':
            class setter:
                def __init__ (self,_class,name):
                    self.self = _class
                    self.set_name = name
                def set(self,item):
                    exec(f'self.self.{self.set_name}=item')
                    return self.self
            return setter(self,name[4:]).set

    def __getattribute__(self, name: str) :
        try :
            return super().__getattribute__(name)
        except  AttributeError:
            if name [:4] == 'set_':
                try:
                    return self.__get_set_attribute(name)
                except:
                    ...
            return super().__getattribute__(name)


class copy_model :

    def copy(self)  :
        from copy import deepcopy as copy
        return copy(self)


class proto_eq_model :
    def __eq__(self, __o) -> bool:
        return (self.__dict__ == __o.__dict__) and (type(self) == type(__o))

class cls_model :
    @property
    def cls (self):
        return type(self)
