from nuts.modeling import nuts_base_model


class base_file_source(nuts_base_model):

    _default_stream_blksize = 256
    _type = None

    @classmethod
    def range_that_be_me (cls,source):
        if cls is not base_file_source:
            raise Exception(f'{cls.__name__} should has its can_be_me method')
        return False


    def __init__ (self,default_stream_blksize:int=None,*args,**kwargs):
        if default_stream_blksize is not None :
            if  default_stream_blksize <= 0 :
                raise Exception("default_stream_blksize can not be smaller than 1")
            self._default_stream_blksize = default_stream_blksize

    class stream :
        def __init__ (self,blksize:int=None,*args,**kwargs):
            if blksize is None :
                raise Exception("blksize can not be None")
            self._blksize = blksize

        def __iter__ (self):
            return self.streamSource()

        @property
        def blksize(self):
            return self._blksize

        def _read (self,blksize:int) -> bytes:
            pass
        def _read_all (self)->bytes :
            source = bytes()
            while True:
                sourceWrapp = self._read(self.blksize)
                if not sourceWrapp:
                    break 
                source += sourceWrapp
                return sourceWrapp
        def read(self,blksize=None) -> bytes: 
            if blksize:
                return self._read(blksize)
            else:
                return self._read_all()

        def close (self):
            pass

        def streamSource(self):
            blksize = self.blksize
            if not isinstance(blksize,int):
                raise f"{blksize} is not an integer\n"
            while True:

                try:
                    sourceWrapp = self._read(blksize)
                except : 
                    sourceWrapp = None

                if not sourceWrapp  :
                    del self
                    return

                yield sourceWrapp

        def __del__ (self):
            self.close()
            del self

    @property
    def type (self):
        return self._type

    def open (self,blksize:int=None, *args, **kwargs):
        if not blksize :
            blksize = self._default_stream_blksize
        return self.stream (blksize = blksize, *args, **kwargs)
    
    def download (self,path:str):
        path = str(path)
        with open(path,'wb+') as file :
            for bin in self :
                file.write(bin)
            file.close()

    def calc_size (self) -> int:
        raise Exception("could not calcsource size ...")

    def __iter__ (self):
        return self.open().streamSource()




