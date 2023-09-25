from nuts.modeling import List
from threading import Thread

class thread_manager (dict) :
    
    @property
    def len (self):
        return len(self)

    def append (self,item,name=None):
        if not name :
            name = self.len + 1
        self[name] = item
    
    def remove (self,name):
        del self[name]
