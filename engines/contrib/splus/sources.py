from nuts.modeling.files.sources import web_file_source
from nuts.modeling.files.sources import its_file_source
from .modeling import Client

@its_file_source
class splus_file_source (web_file_source):
    def __init__ (self,token,url,*args,**wargs):
        link = Client(token).get_download_file_url(url)
        web_file_source.__init__(self,link,*args,**wargs)
    
    def range_that_be_me(self, item):
        if isinstance(item ,str):
            raise Exception(f"I just can eat string :| it's {str(type(item))}")

        import re
        match = re.match(r"splus:\/\/[[a-zA-Z0-9_-]{8,85}\/[[a-zA-Z0-9_-]{8,85}",item)
        if match:
            return 100
        return False
        

    class stream (web_file_source.stream):
        pass


