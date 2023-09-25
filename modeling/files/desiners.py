from .bases import base_file
from .sources import base_file_source
class f (base_file):
    def __init__(self, source:base_file_source, name: str = None, size: int = None, review=None, resolution=None, TYPE=None, *args, **wargs) -> None:
                
        super().__init__(source, name, size, resolution, TYPE, *args, **wargs)
        self.set_review(review)

    def __new__ (cls,source,*args, **kwargs):

        if not isinstance(source,base_file_source) :
            from .sources.managers import root_source
            source_model = root_source(source)
            source = source_model(source,*args,**kwargs)

        if isinstance(source,cls):
            return source
        obj = super(f,cls).__new__(cls, source, *args, **kwargs)
        return obj

    """
    def create_review(self):
        ...
    def calc_resolution(self):
        ...
    """
    def set_review(self, review):
        if review :
            self._review = f(review)
    

class review_file_model(f):
    def __init__ (self, source, review, *args, **wargs): 
        f.__init__(self, source, review=review,*args,**wargs)

    def __new__(cls, source, review, *args, **wargs):
        if not isinstance(review,base_file):
            raise f"review arg must be a file but {review} is a/an {type(review)}"
        return super().__new__(cls,source, *args, **wargs)


class base_image (f):

    def __init__ (self, source, resolution, *args, **wargs) :
        
        f.__init__(self, source, resolution=resolution, *args, **wargs)


    def __new__(cls, source, resolution, *args, **wargs):

        return super().__new__(cls, source, *args, **wargs)


class Image(review_file_model, f):

    def __init__ (self,source, resolution, review, *args, **wargs):
        f.__init__(self, source, resolution=resolution, TYPE='image', review=review, *args, **wargs)

    def __new__ (cls, source, resolution, review, *args, **wargs):
        return f.__new__(cls, source, *args, **wargs)

