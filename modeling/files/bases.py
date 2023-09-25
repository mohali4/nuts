from nuts.modeling import nuts_base_model
from .sources import source_manager, base_file_source, local_file_source, web_file_source
from .types import give_type

class base_file(nuts_base_model):

    class image_size:
        def __init__(self, width:int, height:int) -> None:
            self._width = width
            self._height = height

        @classmethod
        def init (cls,arg0,arg1=None,arg2=None):

            def argaments_raise() :
                raise Exception(f"the args: args1:{arg0}, args2:{arg1}, args3:{arg2}; can't be a picture size! ")

            def new (w:int,h:int):
                return cls(w,h)

            if (arg1 is None) and (arg2 is not None):
                arg1 ,arg2 = arg2, arg1

            if (arg1 is None) and (arg2 is None) :
                if isinstance(arg0,str):
                    import re
                    match = re.findall(r"(\d+)[x,X](\d+)",arg0)
                    if match is []:
                        argaments_raise()
                    width, heigth = match[0]
                    return new(int(width), int(heigth))
                elif isinstance(arg0,tuple|list):
                    if len(arg0) == 2:
                        return new(arg0[0], arg0[1])
                argaments_raise()
            elif arg2 is None:
                if (isinstance(arg0,int|str)) and (isinstance(arg1,int|str)):
                    return new(int(arg0),int(arg1))
            
            argaments_raise()

    _resolution_render = image_size.init

    def __init__(self
    , source, name:str=None              #type: ignore
            , size:int=None              #type: ignore
           ,resolution=None
                 , TYPE=None ,*args, **wargs) -> None: #type: ignore
        self.set_name(name)
        self.set_size(size)
        self.set_resolution(resolution)
        self._review = None
        self.set_TYPE(TYPE)
        for name, value in wargs.items():
            self.__dict__[name] = value

    def __new__(cls,source,*_,**__):
        if not isinstance(source,base_file_source):
            raise Exception(f"source arg must be a file_source but {source} is a/an {type(source)}")
        obj = super(base_file,cls).__new__(cls) 
        obj._source = source   # type: ignore
        return obj

    def set_name (self, name):
        self._name = name
    
    def set_size (self, size):
        self._size = size
    
    def set_review (self, review): 
        raise Exception('this function is specific for F objects not bases.')

    def set_resolution(self, size):
        if size:
            self._size = base_file._resolution_render(size)
        else :
            self._size = None 

    def set_TYPE (self, TYPE):
        _type = give_type(TYPE)
        if _type.convert_to_me :
            _type.convert_to_me(self)
        self._type = _type

    def __getattribute__(self, __name: str) :
        if __name[:4] == "set_" or __name[0] == 'S':
            return self.__get_set_attribute(__name)
        elif __name[0] != '_':
            try :
                return eval(f'self._{__name.lower()}')
            except:
                ...
        raise  Exception(f"'{self.__class__.__name__}' object has no attribute '{__name}'")
    
    def save_at (self,path):
        self.source.download(path) #type: ignore
    
    def local (self):
        source = self.source
        if source.type == 'local': #type: ignore
            path = source.file_path #type: ignore
        else:
            from nuts.config import temp_dir
            temp = temp_dir()
            if self._name :
                path = temp/self.name
            else:
                from random import randint
                path = temp/f'file_{randint(80000)}' #type: ignore 
            self.save_at(path)
        return path


    @property
    def name(self):
        if self._name:
            return self._name
        return "NoName"


