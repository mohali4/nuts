from typing import List as list_t
from nuts.rooting.pools import flag_pool
from nuts.modeling.messeges import reqMSG
from nuts.rooting.flagers.models import flag_model


def root (msg:reqMSG,pools:list_t[flag_pool]) -> flag_model:
    rooter = msg.user.get_rooter_model()
    flag = rooter.root(msg) #type: ignore
    return flag
    
