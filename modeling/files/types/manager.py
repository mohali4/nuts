from .bases import base_file_type
global types
class type_manager (list):
    def filter (self,key) :
        resolve = type(self)()
        for item in self:
            if key(item):
                resolve.append(item)
        return resolve
    def append(self,item,*a,**k):
        if len(self.filter(lambda t:t.name==item.name)) :
            raise Exception(f"you can't add a file_type named {item.name} again.")
        super().append(item,*a,**k)
        return self


types = type_manager()

def its_type (cls):
    global types
    if not issubclass(cls,base_file_type):
        raise Exception(f"{cls.__name__} should be {base_file_type.__name__}. but it's not.")
    types.append(cls)
    return cls

def give_type (name) -> base_file_type:
    global types
    q = types.filter(lambda t:t.name==name)
    if not len (q) :
        raise Exception(f"the type {name} does not exist.")
    return q[0]
