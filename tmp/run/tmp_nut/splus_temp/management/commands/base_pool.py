from nuts.rooting import flag_pool
from nuts.rooting.flagers import classic_flagger
pool = flag_pool()
flag = classic_flagger('.tmp',pool)

@flag('temp1') #type: ignore
def tmp(msg):
    ...