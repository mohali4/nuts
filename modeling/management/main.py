from nuts.modeling.protos import nuts_base_model as __base_model

class List (list, __base_model):
    def filter (self,key):
        res = self.copy()
        for condidate in self:
            if not key(condidate):
                res.remove(condidate)
        return res

    def find (self, key):
        for cond in self:
            if key(cond):
                return cond
        raise Exception(f"Does not Exist.")

    def append_if_not_exists (self,item):
        if not item in self :
            self.append(item)
    def __eq__ (self,o):
        i = self.copy()
        o = List(o)
        for _o in o :
            if not _o in i :
                return False
            else:
                o.remove(_o)
        if len (o) == 0 :
            return True
        return False


class finder :
    def __init__ (self,key,items):
        self.__members_getter = items
        self.__default_precedency_finder = key
    @property
    def __members (self):
        return self.__members_getter()

    def precedency(self, item, *args, key=False, **wargs):
        if key :
            ...
        elif self.__default_precedency_finder:
            key = self.__default_precedency_finder
        else:
            raise Exception(f"Please set default_key or feel the key arg.")
        return key(item, *args, **wargs) #type: ignore
    def find (self, *args, **wargs):
        condidates = list()
        for condidate in self.__members:
            try: 
                precedency = self.precedency(condidate, *args, **wargs)
            except :
                precedency = False
            if precedency is True :
                return condidate
            elif precedency is not False :
                condidates.append((precedency,condidate))
        if condidates.__len__() == 0:
            raise Exception(f"Could not find a match for {(args,wargs)} in {[member.__name__ for member in self.__members]}")
        condidates.sort(key=lambda item:item[0])
        return condidates[-1][1]    



class manager (__base_model):



    def __init__ (self, default_key=False ,members=[]):    
        self.__members = List(members)
        self.__default_precedency_finder = default_key
        self.__finders = {}

    def __iter__ (self):
        return self.__members.__iter__()

    def append_decorator (self, item):
        self.__members.append(item)
        return item

    def find(self, item, *args, key=False, **wargs):
        if key :
            ...
        elif self.__default_precedency_finder :
            key = self.__default_precedency_finder
        else:
            raise Exception(f"Please set default_key or feel the key arg.")
        return self.get_finder(key).find(item,*args,key=key,**wargs)


    def precedency (self, item, *args, key=False, **wargs):
        if key :
            ...
        elif self.__default_precedency_finder :
            key = self.__default_precedency_finder
        else:
            raise Exception(f"Please set default_key or feel the key arg.")
        return self.get_finder(key).precedency(item,*args,key=key,**wargs)

    def get_finder (self,key) -> finder :

        def get_members ():
            return self.__members

        __finder =  self.__finders.get(key,False)
        if __finder == False :
            self.__finders[key] = finder(key,get_members)
            return self.get_finder(key)
        return __finder    #type: ignore
