from nuts.modeling import nuts_base_model
from json import dumps as python_json_dumps
class value (nuts_base_model,dict):
    def __init__ (self,*args,**wargs):
        dict.__init__ (self,*args,**wargs)
        self['__nuts__'] = True
    def encode (self,encoder=python_json_dumps):
        return encoder(self)

    def __str__ (self):
        return self.encode()


def root(path) :
    return value(root=path)
