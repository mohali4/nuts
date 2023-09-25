from django.db import models
from typing import Any

class engine_field (models.TextField):
    def get_prep_value(self, engine:Any) -> str:
        return super().get_prep_value(engine.id)
    def to_python(self, engine_name:str) -> Any:
        from nuts.engines.find import find_engine
        return find_engine(engine_name)



from  nuts.models import cache
class cache_field (models.ForeignKey):

    @classmethod
    def __change_argaments (self_cls,*args,**wargs):
        args = [cache, *args]
        wargs['on_delete'] = models.PROTECT
        return args, wargs

    def __init__(self,*args,**wargs):
        args, wargs = self.__change_argaments(*args,**wargs)
        models.ForeignKey.__init__(self,*args,**wargs)

    def __new__ (cls,*args,**wargs):
        args, wargs = cls.__change_argaments(*args,**wargs)
        new = super(cache_field,cls).__new__ #models.ForeignKey.__new__    
        try:
            obj = new(cls,*args,**wargs)
        except:
            obj = new(cls) #type: ignore
        return obj

