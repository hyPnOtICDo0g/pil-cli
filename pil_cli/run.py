from sys import argv
from PIL import Image
from .modules.variables import var
from .modules.img import image
from .modules.cli import args
from alive_progress import alive_it

class pil_cli:
    def __init__(self, args):
        self.args = args
        # create an argument dict using the arguments provided
        self.argsDict = vars(args)

    def main(self):
        try:
            completeList = []
            img = image(Image.open(self.args.infile))
            out = self.argsDict['outfile']

            # check if an input image is unsupported
            if out.split('.')[-1].upper() not in var.supportedImageExt: raise ValueError('unsupported file format')
            del self.argsDict['infile'], self.argsDict['outfile']
            img.properties()

            # iterate the argument dict and call the required function
            for key, value in alive_it(self.argsDict.items()):
                if value is not None:
                    getattr(img, key)()
                    completeList.append(key)

            img.imageObj.save(out)
        except Exception as e:
            print(f'{var.prog}: error:', e)
        else:
            print('ok: ' + ', '.join(completeList))

def main():
    app = pil_cli(args)
    app.main()
