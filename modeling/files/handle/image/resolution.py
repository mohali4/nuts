

def create_review (file):
    if isinstance(file,str): path = file
    else: path = file.local()
    from PIL import Image, ImageFile
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    img = Image.open(path)
    rev_size_w , rev_size_h = img.size
    ratio = rev_size_w  / 150
    rev_size_w, rev_size_h = (rev_size_w/ratio), (rev_size_h/ratio)
    rev_img = img.resize((rev_size_w,rev_size_h), Image.ANTIALIAS)
    from nuts.config.dirs import temp
    tmp_dir = temp()
    rev_dir = tmp_dir/f'review.{file.name}'
    rev_img.save(str(rev_dir))
    return rev_dir


