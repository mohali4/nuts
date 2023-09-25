
from .bases import base_file_source

global sources
class source_manager (list):
    def filter (self,key) :
        resolve = type(self)()
        for item in self:
            if key(item):
                resolve.append(item)
        return resolve
    def append(self,item,*a,**k):
        super().append(item,*a,**k)
        return self


sources = source_manager()

from typing import Any

def its_file_source (model) -> Any:
    global sources
    if not issubclass(model,base_file_source):
        raise Exception(f"your source model ({model.__name__}) must to be subclass of {base_file_source.__name__}")
    sources.append(model)
    return model


def root_source (source):
    global sources
    router = []
    for condidate in sources :
        try:
            num = condidate.range_that_be_me(source)
        except:
            num = False
        if num is not False :
            if num == 100:
                return condidate
            router.append((condidate,num))
    if router == []:
        raise Exception(f'Could not match the [{source}]')
    router.sort(key=lambda item : item[1])
    return router[-1][0]
     
    
