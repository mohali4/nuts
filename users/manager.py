from django.db.models.manager import Manager as django_manager
from nuts.engines.find import find_engine


class user_manager(django_manager):
    def create(self, *args, **kwargs):
        
        return super().create(*args,**kwargs)
    
    @classmethod
    def __change_argaments(cls_self,*args,**wargs): #type: ignore
        return args, wargs
    
    
    def __init__(self,*args,**wargs):
        args, wargs = self.__change_argaments(*args,**wargs)
        super().__init__(*args, **wargs)
    
    def __new__(cls,*args,**wargs):
        args, wargs = cls.__change_argaments(*args,**wargs)
        return django_manager.__new__(cls,*args,**wargs)
