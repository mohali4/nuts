def size (file):
    return file.source.calc_size()

def resolution (file):
    path = file.local()
    from PIL.Image import open
    img = open(path)
    return img.size