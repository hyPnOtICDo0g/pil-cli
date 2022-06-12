from sys import argv
from variables import var
from argparse import ArgumentParser

class cmd:
    def validateArgs(self, args):
        if(
            (args.infile or args.outfile)
            and not (args.convert
                    or args.scale
                    or args.filter
                    or args.rotate
                    or args.crop)
        ):
            print(f'{argv[0]}: error: requires at least 1 image operation argument but 0 were provided')
            exit(1)

    def parseArgs(self):
        # global flags
        parser = ArgumentParser(description='Basic Image Manipulation using Pillow.')
        parser.add_argument('-V', '--version', action='version', version='%(prog)s 1.0')
        # parser.add_argument('-e', '--extension', help='Output image format.', choices=var.supportedImageExt, default='PNG', metavar='EXT')
        # required arguments
        required = parser.add_argument_group('required arguments')
        required.add_argument('-i', '--infile', help='Input Image or Directory.', required=True)
        required.add_argument('-o', '--outfile', help='Output Image or Directory.', required=True)
        # image operation flags
        imgopr = parser.add_argument_group('image operations')
        imgopr.add_argument('-c', '--convert', help=f'Convert to a different color mode. {var.imageModes}', choices=var.imageModes, metavar='MODE')
        imgopr.add_argument('-n', '--crop', help='Crop an image based on given coordinates. (separated by \',\').', metavar='COORDINATES')
        imgopr.add_argument('-s', '--scale', help='Scale an image to a given resolution.', metavar='RESOLUTION')
        imgopr.add_argument('-f', '--filter', help=f'Filter an image. {var.imageFilters}', choices=var.imageFilters, metavar='FILTER')
        imgopr.add_argument('-r', '--rotate', help='Rotate an image based on a given degree.', type=int,  metavar='DEGREE')
        # imgopr.add_argument('-b', '--base64', help='Create an encoded base64 URL from an image.', metavar='')
        # return parsed arguments
        args = parser.parse_args()
        self.validateArgs(args)
        return args

args = cmd().parseArgs()
