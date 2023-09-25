class List(list):
    def append (self,*a):
        for item in a :
            super().append(item)
        return self
    def copy(self):
        return type(self)(super().copy())

class base_file_type :
    name = None
    show = None
    convert_to_me = None
