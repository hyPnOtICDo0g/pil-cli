from img import image
from cli import args
from sys import argv
from variables import var
from PIL import Image
from alive_progress import alive_it

class pil_cli:
    def __init__(self, args):
        self.args = args
        self.argsDict = vars(args)

    def main(self):
        try:
            img = image(Image.open(self.args.infile))
            out = self.argsDict['outfile']
            completeList = []

            if out.split('.')[-1].upper() not in var.supportedImageExt: raise ValueError('unsupported file format')
            del self.argsDict['infile'], self.argsDict['outfile']
            img.properties()

            for key, value in alive_it(self.argsDict.items()):
                if self.argsDict[key] is None:
                    continue
                else:
                    getattr(img, key)()
                    completeList.append(key)

            img.imageObj.save(out)
        except Exception as e:
            print(f'{argv[0]}: error:', e)
        else:
            print('ok: ' + ', '.join(completeList))

app = pil_cli(args)
app.main()
