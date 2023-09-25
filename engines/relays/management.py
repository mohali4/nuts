from nuts.modeling.management import List
from .relays import base_relay

class relay_manager (List) :
    def __getitem__(self,item) -> base_relay:
        return self.find(lambda x :x.token==item)