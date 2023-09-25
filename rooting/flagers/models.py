from ..paths import base_path 
from nuts.modeling import nuts_base_model

__all__ = [
    'flag_model'
]

class flag_model (nuts_base_model) :
    def __init__ (self, path:base_path, func):
        self.path = path
        self.func = func
