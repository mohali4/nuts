        

class Model:

    def __get_models( *a ):
        from . import models
        from .models import model_name_pattern as pattern
        model_names = models.__dict__.keys()
        valid_models = []
        import re
        for name in model_names :
            if pattern.match(name):
                valid_models.append((pattern.find(name), models.__dict__[name]))
        return valid_models


    def __new__(cls,*args):
        models = []
        for name, model in cls.__get_models():
            if name in args or '*' in args:
                models.append(model)
        class model(*models) : ...
        return model
        
