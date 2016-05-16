# -*- coding: utf-8 -*-


#from distutils.core import setup
from setuptools import setup
 
short_desc = "A fitting algorithm based on deep learning" \
             " for dynamics models of complex network"
 
setup(
    name = 'deepfit',
    version = '0.0.1',
    py_modules = [],
    author = 'Daewon Lee',
    author_email = 'daewon4you@gmail.com',
    url = 'https://github.com/dwgoon/deepfit',
    description = short_desc,
    install_requires = ['numpy'],
    license = 'MIT License',
    keywords = ["fitting", "deeplearning", "dynamics"]
)