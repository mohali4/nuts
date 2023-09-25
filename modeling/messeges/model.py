from nuts.modeling.protos import nuts_base_model
from nuts.users.subclasses import user_subclass

class base_section (nuts_base_model):
    main_body = False

class text_section (base_section):
    class Body(str) :...
        
    def __init__(self,body,*args,main=False,**wargs):
        self._body = self.Body(body)
        self.main_body = main
    
    @property
    def body (self) -> str:
        return self._body

    def __str__ (self):
        return self.body

from re import L
from nuts.modeling.files import f, base_file

class file_section (base_section):
    def __init__ (self,file:f,*args,**wargs):
        if not isinstance(file, base_file):
            file = f(file)
        self._file = file
    
    @property
    def file(self):
        return self._file

class base_messege(list) :
    def __init__(self, *args, **wargs):
        super().__init__(*args, **wargs)
    
    
    @property
    def body (self) -> str:
        q = filter(self, lambda sec: isinstance(sec,text_section)) #type: ignore
        if q == []:
            return ""
        _q = filter(q, lambda sec: sec.main_body) #type: ignore
        if _q != [] :
            return _q[0].body #type: ignore
        return q[0].body #type: ignore

    def __new__ (cls,*args,**wargs):
        arl = len(args)
        if arl == 0 :
            obj = super(cls,base_messege).__new__(cls)
        elif arl == 1 and isinstance(args,list|tuple) :
            obj = super(cls,base_messege).__new__(cls,args[0])
        else:
            obj = super(cls,base_messege).__new__(cls)
            for item in args :
                obj.append(item)
        for sec in obj :
            if not isinstance(sec,base_section):
                #raise Exception(f"{sec} is not an standard secion")
                ...
        return obj
    
        
from nuts.modeling import nuts_base_model
class reqMSG (nuts_base_model):
    def __init__ (self, messege:base_messege, *args, userID:str=None, time:int=None, **wargs): #type: ignore
        if userID is None :
            raise Exception(f"You can't create a messege without its user")
        if not isinstance(messege, base_messege):
            raise Exception(f"Messege is unvalid")
        self.msg = messege
        self.userID = userID
        self.time = time
        super().__init__(*args ,*wargs)

    @property
    def mesege(self):
        return self.msg

    @property
    def user (self) -> user_subclass:
        ...
