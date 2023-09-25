
from  nuts.modeling.management import manager

@manager #type: ignore
def engines (condidate,name):
    return condidate.is_that_me(name)
its_engine = engines.append_decorator

@engines.get_finder
def userId_finder (condidate,userID):
    return condidate.Is_this_my_user(userID)



