

from .bases import base_file_source
from .managers import its_file_source as Im_file_source

@Im_file_source
class local_file_source(base_file_source):
    _default_stream_blksize = 250
    _type = 'local'

    @classmethod
    def range_that_be_me(cls, source):
        if not isinstance(source,str|bytes):
            return False
        if isinstance(source,bytes):
            source = source.decode()
        
        import re
        import os
        from pathlib import Path
        if re.match(r"file:///.+",source) is not None:
            source = re.findall(r"file:///(.+)",source)[0]
        try:
            path = Path(source).__str__()
            r = os.path.isfile(path)
            if not isinstance(r,bool) :  return False
            if r:  return 100
            else:  return False
        except:
            return False
    def __init__ (self,file_path,*args, **kwargs):
        super().__init__(*args,**kwargs)
        self.file_path = file_path
 
    class stream(base_file_source.stream):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.file_path = kwargs['file_path']
            self._filelike = None

        @property
        def filelike(self):
            if not self._filelike :
                self._filelike = open(self.file_path,'rb')
            return self._filelike

        def _read(self,blksize:int)->bytes:
            filelike = self.filelike
            data = filelike.read(blksize)
            return data

        def _read_all(self) -> bytes:
            filelike = self.filelike
            return filelike.read()

        def close(self):
            self.filelike.close()
            self._filelike = None
            super().close()

        def read(self,blksize=None) -> bytes:
            if blksize:
                data = self._read(blksize)
                if not data :
                    self.close()
                    return data
                return data
            else:
                return self._read_all()

    def open (self,blksize:int=None):
        if not blksize :
            blksize = self._default_stream_blksize
        return self.stream(file_path=self.file_path,blksize=blksize)

    def calc_size (self):
        try:
            import os
            return int(os.path.getsize(self.file_path))
        except:
            raise Exception(f"could not calc the filesize, check this path: '{self.file_path}'")

@Im_file_source
class web_file_source(base_file_source):
    _type = 'web'

    @classmethod
    def range_that_be_me(cls, source):
        num = 95
        if not isinstance(source,str):
            return False
        import re
        if (re.match(r"^https?:\/\/.+",source) or re.match(r"^ftps?:\/\/.+",source)):
            url = re.findall(r'tps?:\/\/(.+)',source)[0]
            num += 5
        else:
            url = source
        if re.match(r"([A-Za-z0-9\-\_]*\.?)+(\/[A-Za-z0-9\.\-\_\~\!\$\&\'\(\)\*\+\,\;\=\:\@\?]+)+[\/]?",url) is not None :
            return num
        else:
            return False


    def __init__ (self,link,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._url = link


    @property
    def link(self):
        return self._url

    class stream(base_file_source.stream):
        def __init__ (self, file_link, *args, **kwargs):
            super().__init__(*args,**kwargs)
            self._file_link = file_link
            self._httpHandler = None
            self._streamResponse = None
            self._streamHandler = None

        @property
        def file_link(self):
            return self._file_link

        @property
        def httpHandler(self):
            if self._httpHandler is None:
                import urllib3
                self._httpHandler = urllib3.PoolManager()
            return self._httpHandler

        @property
        def streamResponse(self):
            if self._streamResponse is None :
                self._streamResponse = self.httpHandler.request('get',self.file_link,preload_content=False)
            return self._streamResponse
        
        @property
        def streamHandler(self):
            if self._streamHandler is None: 
                self._streamHandler = self.streamResponse.stream(1).__iter__()
            return self._streamHandler


        def _read(self,blksize:int)->bytes:
            data = b''
            for _ in range(blksize):
                data += self.streamHandler.__next__()
            return data

        def _read_all(self) -> bytes:
            return self.streamResponse.read()

        def close(self):
            if self._streamResponse is not None:
                self._streamResponse.close()
                self._streamResponse = None
            if self._streamHandler is not None :
                self._streamHandler.close()
                self._streamHandler = None
            super().close()


    def open (self,blksize:int=None):
        if not blksize :
            blksize = self._default_stream_blksize
        return self.stream(file_link=self.link,blksize=blksize)


    def calc_size(self):
        http = self.open().httpHandler
        try:
            x = http.request('head',self.link)
            size = x.headers.get('Content-Length',False)
        except:
            size = False

        if size : return size
        raise Exception("this server does not support the size serving before download.")

web_file_source.__init__

@Im_file_source
class readed_file_source(base_file_source):

    _type = 'bytes'

    @classmethod
    def range_that_be_me(cls, source):
        if isinstance(source,bytes):
            return 7
        elif isinstance(source,str):
            return 3
        else:
            return False

    def __init__ (self, bin, *args, **kwargs):
        self._bin = bin
        self.size = len(bin)
        super().__init__(*args,**kwargs)

    @property
    def bin(self):
        return self._bin

    class stream(base_file_source.stream):
        def __init__ (self,bin,*args, **kwargs):
            self._bin = bin
            self.size = len(bin)
            self.readed = 0
            super().__init__(*args,**kwargs)
        def _read(self, blksize: int) -> bytes:
            try :
                b = self._bin[self.readed:self.readed+blksize]
                self.readed += blksize
                return b
            except:
                return self._read_all()
        def _read_all(self) -> bytes:
            try:
                b = self._bin[self.readed:]
                self.readed = self.size-1
                return b
            except:
                return None

    def open(self, blksize: int = None, *args, **kwargs):
        return super().open(bin=self._bin, blksize=blksize, *args, **kwargs)
    
    def calc_size(self) -> int:
        return self.size

