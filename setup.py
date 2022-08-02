#! /usr/bin/env python

from setuptools import setup, find_packages, Command

from distutils.command.build_py import build_py

setup(
    name             = 'homomer_count',
    version          = '1.0.6',
    description      = 'Package for distribution',
    author           = 'msjeon27',
    author_email     = 'msjeon27@cau.ac.kr',
    url              = '',
    download_url     = '',
    install_requires = ['argparse'],
	include_package_data=True,
	packages=find_packages(),
    keywords         = ['HOMOMERCOUNT', 'homomercount'],
    cmdclass         = {'build_py': build_py},
	scripts          = ['scripts/homomer_count'],
    python_requires  = '>=3',
    zip_safe=False,
    classifiers      = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
) 
