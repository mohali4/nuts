from .bases import base_file_type
from .manager import its_type

@its_type
class File_Type (base_file_type):
    name = 'File'
    show = 'File'

@its_type
class Image_Type (base_file_type):
    name = 'Image'
    show = 'Iamge'
    @classmethod
    def convet_to_me (cls,file_model):
        if not issubclass(cls,Image_Type):
            raise
        if not file_model.review :
            from nuts.modeling.files.handle.image.resolution import create_review
            try: rev = create_review(file_model)
            except: rev = None
            file_model.set_review(rev)
        if not file_model.resolution :
            from nuts.modeling.files.handle.image.information import resolution
            try: res = resolution(file_model)
            except: res = None
            file_model.set_resolution(res)


@its_type
class Video_Type (base_file_type):
    name = 'Video'
    show = 'Video'
    @classmethod
    def convet_to_me (cls,file_model):
        if not file_model.review :
            from nuts.modeling.files.handle.video.resolution import create_review
            try: rev = create_review(file_model)
            except: rev = None
            file_model.set_review(rev)
        if not file_model.resolution :
            from nuts.modeling.files.handle.video.information import resolution
            try: res = resolution(file_model)
            except: res = None
            file_model.set_resolution(res)


