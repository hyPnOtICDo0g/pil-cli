from sys import argv
from .cli import args
from PIL import Image, ImageFilter

class image:
    def __init__(self, img):
        self.imageObj = img

    def properties(self):
        print(
            f'Properties ({self.imageObj.filename}):\n'
            f'resolution: {self.imageObj.format} | mode: {self.imageObj.mode}\n'
            f'size: {self.imageObj.width}x{self.imageObj.height} | palette: {self.imageObj.palette} | format: {self.imageObj.format}\n'
        )

    def convert(self):
        # handle `GRAY` separately as it is invoked using `L` as a parameter
        if args.convert == 'GRAY':
            self.imageObj = self.imageObj.convert('L')
        else:
            self.imageObj = self.imageObj.convert(args.convert)

    def scale(self):
        try:
            # str -> tuple with two integer values
            size = tuple(map(int, args.scale.split('x', 1)))
            if len(size) > 2: raise ValueError
        except ValueError:
            print(f'{argv[0]}: error: invalid resolution (\'{args.scale}\')')
            exit(1)
        else:
            # a, b = size[0] / size[1], self.imageObj.size[0] / self.imageObj.size[1]
            # print(f'{argv[0]}: warning: image being upscaled') if a < b else pass
            self.imageObj = self.imageObj.resize(size, Image.ANTIALIAS)

    def filter(self):
        self.imageObj = self.imageObj.filter(getattr(ImageFilter, args.filter))

    def rotate(self):
        self.imageObj = self.imageObj.rotate(args.rotate, expand=True)

    def crop(self):
        try:
            coordinates = tuple(map(int, args.crop.split(',', 4)))
            if len(coordinates) > 4: raise ValueError
        except ValueError:
            print(f'{argv[0]}: error: invalid coordinates \'{args.crop}\'')
            exit(1)
        else:
            self.imageObj = self.imageObj.crop(coordinates)
