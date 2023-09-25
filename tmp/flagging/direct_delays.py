
last, import_time, first, secound, direct =[], [], [], [], []

def check():
    from time import time
    class f: 
        @property
        def now (self):
            return time()
    n= f()

    def calc():
        nonlocal clock
        c = n.now - clock
        clock = n.now
        return c

    clock = n.now
    from nuts.rooting.globals import flag as direct
    import_time.append(calc())

    direct('.a')
    first.append(calc())
    
    direct('.v')
    secound.append(calc())
    
    direct('.g')('.b')('.b') #type:ignore
    last.append(calc())

from sys import argv
num = int(argv[0]) if len(argv) else 1
for _ in range(num):check()

print(f'''
    Test resualt:
    __________________________

    import :    {sum(import_time)/num  }
    first  :    {sum(first)/num        }
    secound:    {sum(secound)/num      }
    last   :    {sum(last)/num         }

    ''')

