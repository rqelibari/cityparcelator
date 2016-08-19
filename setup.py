#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Cityparcelator


    (c) 2016 Copyright Rezart Qelibari <qelibarr@informatik.uni-freiburg.de>

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
import os
from setuptools import setup, find_packages

srcdir = os.path.dirname(__file__)


def read(fname):
    return open(os.path.join(srcdir, fname)).read()

long_description = ''
if os.path.exists('README.txt'):
    long_description = read('README.txt')

setup(
    name="cityparcelator",
    version='0.1.0',
    author='Rezart Qelibari',
    author_email='qelibarr@informatik.uni-freiburg.de',
    url='https://github.com/rqelibari/cityparcelator',
    description='A building parcel generator, which works on SVG street maps.',
    long_description=long_description,
    download_url='https://github.com/rqelibari/pygonal/archive/master.zip',
    provides=['cityparcelator'],
    license='Apache 2.0',
    packages=find_packages(),
    keywords='city parcel generator',
    install_requires=['click>=6.6'],
    extras_require={'dev': ['pep8>=1.7.0']},
    entry_points='''
        [console_scripts]
        cityparcelator=cityparcelator.scripts.cityparcelator:cli
    ''',
    test_suite="cityparcelator.tests",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Information Technology',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.5',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX'
    ]
)
