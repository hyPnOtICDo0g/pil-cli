# About

A command-line tool which utilizes the **Python Imaging Library (PIL)** to perform basic image processing.

# Usage

```
usage: pil-cli [-h] [-V] -i INFILE -o OUTFILE [-c MODE] [-n COORDINATES]
               [-s RESOLUTION] [-f FILTER] [-r DEGREE]

Basic Image Manipulation using Pillow.

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit

required arguments:
  -i INFILE, --infile INFILE
                        Input Image or Directory.
  -o OUTFILE, --outfile OUTFILE
                        Output Image or Directory.

image operations:
  -c MODE, --convert MODE
                        Convert to a different color mode. ['GRAY', 'CMYK',
                        'RGB']
  -n COORDINATES, --crop COORDINATES
                        Crop an image based on given coordinates. (separated
                        by ',').
  -s RESOLUTION, --scale RESOLUTION
                        Scale an image to a given resolution.
  -f FILTER, --filter FILTER
                        Filter an image. ['BLUR', 'DETAIL', 'SHARPEN',
                        'EMBOSS', 'EDGE_ENHANCE']
  -r DEGREE, --rotate DEGREE
                        Rotate an image based on a given degree.
```

# Examples

- Convert an (RGB) image to grayscale:
```
pil-cli -i in.jpg -o out.jpg -c GRAY
``` 

- Crop 100x100 pixels (on the top left) from an image:
```
pil-cli -i in.jpg -o out.jpg -n 0,0,100,100
```  

- Scale an image to 100x100:
```
pil-cli -i in.jpg -o out.jpg -s 100x100
```

- Blur an image:
```
pil-cli -i in.jpg -o out.jpg -f BLUR
```

- Rotate an image 90 degrees anticlockwise:
```
pil-cli -i in.jpg -o out.jpg -r 90
```

- Use all above options together:
```
pil-cli -i in.jpg -o out.jpg -s 90x90 -c GRAY -n 0,0,90,90 -f BLUR -r 90
```
> **Note**: The order of arguments provided make no difference to the final image.  
> Operations are performed in the following order: **convert, crop, scale, filter, rotate**


# Dependencies

- Python >=3.8
- [pillow](https://pypi.org/project/Pillow)
- [alive-progress](https://pypi.org/project/alive-progress/)
- [argparse](https://pypi.org/project/argparse)

# Installation

It is advised to install **git** and use the latest version of *pip* before installation, including the essential packages, *setuptools* and *wheel*.  
To ensure these packages are up-to-date, run

```
python3 -m pip install --upgrade pip setuptools wheel
```

To install, run

```
python3 -m pip install --no-cache-dir git+https://github.com/hyPnOtICDo0g/pil-cli.git 
```
