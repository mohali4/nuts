from django.db import models
from .manager import user_manager
from nuts.fields import cache_field
from nuts.modeling import Model
from .subclasses import user_subclass

class base_user (models.Model,user_subclass):

    objects = user_manager()

    id = models.TextField(primary_key=True)
    cache = cache_field()

    class root_manager () :
        def __init__ (self,user,**options):
            self.user = user
            Model('init').__init__(self,**options) #type: ignore


        @property
        def is_direct (self):
            direct = self.user.cache.get (self.__direct_cache_name,None)
            if direct :
                return True
            return False


        def write_direct(self,path,save):
            self.user.cache[self.__direct_cache_name] = path.__str__()
            if save : self.user.save()
            
        def read_direct (self):
            return self.user.cache[self.__direct_cache_name]

        def remove_direct(self,save):
            if self.is_direct:
                del self.user.cache[self.__direct_cache_name]
            if save : self.user.save()
    

        @property 
        def __direct_cache_name (self):
            return '__direct__root__'

    def __init__(self,*args,**wargs):
        models.Model.__init__(self,*args,**wargs)
        self.r_m = self.root_manager(self)

    def __new__(cls,*args, **wargs):
        return models.Model.__new__(cls, *args, **wargs)

    def direct(self,path,save=True):
        self.r_m.write_direct(path,save)
    
    def undirect(self,save=True):
        self.r_m.remove_direct(save)
    
    @property
    def was_directed(self):
        return self.r_m.is_direct

    @property
    def direct_path (self):
        self.r_m.read_direct()
        