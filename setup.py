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

from setuptools import setup, find_packages

setup(
    version='0.1.0',
    name="cityparcelator",
    description='''
        Cityparcelator is a python 3 engine, which generates building parcels
        on a SVG street map using a blocksubdivision algorithm.
    ''',
    url='https://github.com/rqelibari/cityparcelator',
    author='Rezart Qelibari',
    author_email='qelibarr@informatik.uni-freiburg.de',
    license='Apache 2.0',
    packages=find_packages(),
    keywords='city parcel generator',
    install_requires=[],
    extras_require={},
    entry_points='''
        [console_scripts]
        cityparcelator=cityparcelator.scripts.cityparcelator:cli
    ''',
    test_suite="cityparcelator.tests",
    zip_safe=False,
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Information Technology',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.5',
    ]
)
