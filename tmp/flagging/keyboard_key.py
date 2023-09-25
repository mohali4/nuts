from nuts.keyboard.models import key
from json import loads
k = key('name',{'root':'root1'})
k.name='mane'
try:
    loads(k.encode())['mane']
except:
    raise Exception('Keys broken :|')
print('Keys is correct :)')