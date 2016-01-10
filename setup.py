from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()


setup(

    name = 'QuickVars',
	version = read('VERSION'),
    author = 'Salamander115',
    author_email = 'mjlonghurst15@gmail.com',
    description = 'Python Module that stores variables in a file to allow variable storage after script is terminated',
    long_description = read('README.txt'),
    
	url = 'https://github.com/Salamander115/QuickVars',
    license = 'MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='variables',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
	
)