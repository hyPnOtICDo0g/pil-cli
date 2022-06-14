from sys import argv
from os import path

class variables:
    def __init__(self):
        self.supportedImageExt = ['BMP', 'ICO', 'JPEG', 'JPG', 'JFIF', 'PNG', 'PPM', 'WebP']

        self.imageModes = ['GRAY', 'CMYK', 'RGB']

        self.imageFilters = ['BLUR', 'DETAIL', 'SHARPEN', 'EMBOSS', 'EDGE_ENHANCE']

        self.prog = path.basename(argv[0])

var = variables()
