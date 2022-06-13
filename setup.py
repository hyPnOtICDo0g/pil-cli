try:
    from setuptools import setup
except ImportError:
    print('`pil-cli` requires \'setuptools\' to continue installation.')
    exit(1)

if __name__ == '__main__':
    setup(
        name = 'pil-cli',
        version = '1.0',
        description = 'Basic Image Manipulation using Pillow.',
        keywords = 'cli tool image-processing pillow',
        python_requires = '>=3.8',
        license = 'MIT',
        install_requires = [
            'pillow',
            'alive-progress',
            'argparse',
        ],
        packages = [
            'pil_cli',
            'pil_cli.modules'
        ],
        entry_points = {
            'console_scripts': [
                'pil-cli = pil_cli.run:entryPoint',
            ]
        },
        classifiers = [
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3 :: Only',
        ],
    )
