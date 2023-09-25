
from nuts.engines.management import engines, userId_finder
from nuts.engines.subclasses import _engine_subclass

def get_engine (engine_name):
    global engines
    try :
        return engines.find(engine_name)
    except:
        raise Exception(f'''
I can't find {str(engine_name)}
This is confimed engines :
{str("""
""").join([ item.name for item in engines])}
''')

def engine_from_userID (userID):
    try:
        return userId_finder.find(userID)
    except:
        raise Exception(f'''
Could not find this user ({userID}) engine :(
''')

def find_engine (data):
    if isinstance(data, _engine_subclass) :
        return data.cls
    elif isinstance(data,type) :
        if issubclass(data, _engine_subclass):
            return data
    from nuts.config.patterns import userID_pattern, engineName_pattern
    if userID_pattern.match(data) : #type: ignore
        return engine_from_userID(data)
    elif engineName_pattern.match(data) : #type: ignore
        return get_engine(data)
    raise Exception(f"""Uncorrect engine_find_data ({data})
    
    This is the correct forms:
        1) engineName: [engineName]
        2) userId: [engineId]://[usertoken]

Also check your engine model has been installed or no ?
""")