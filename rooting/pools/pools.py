from nuts.modeling import nuts_base_model as __base_model , List
from nuts.rooting.paths.bases import base_path as _base_path
from nuts.rooting.paths import direct_path ,classic_path
from nuts.rooting.flagers import flag_model

class flag_pool (List) :
    def __init__ (self,list_model:type=List, flag_model:type=flag_model ):
        self.flag = flag_model

    @property
    def roots (self):
        return self

    def __call__(self,path:_base_path ,func):
        self.roots.append(self.flag(path, func))
    
    def direct_root (self,path):
        roots = self.roots.filter(lambda i : isinstance(i.path,direct_path))
        for root in roots : 
            if root.path.can_root_to_me(path) :
                return root
        raise

    def classic_root (self,path):
        roots = self.roots.filter(lambda i : isinstance(i.path,classic_path))
        for root in roots : 
            if root.path.can_root_to_me(path) :
                return root
        raise

        
