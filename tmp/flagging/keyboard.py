from nuts.keyboard import KB, root
kb = KB({'name1':root('root1'),'name2':root('root2')},{'name3':root('root3')})
from json import dumps, loads
if not loads(kb.encode()) == [[{'name1':root('root1')},{'name2':root('root2')}],[{'name3':root('root3')}]]:
    raise Exception('Keyboard dumps broke :|')
print ('Keybord encoding works perfect :)')