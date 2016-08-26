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
import logging
logger = logging.getLogger(__name__)


class MapReader(object):
    """
    Reads a roadmap of a city (currently as a SVG file) and represents it as
    a networkx graph.
    """
    def __init__(self, pSvgFilePath, pOutputPath):
        """
        Behaviour:
         Init class with file at svgFilePathself. Calls 'parseSVGFile'.

        Arguments:
         pSvgFilePath -- the path to the readable svg file.
        """
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug(
                "File to get paths from is {}".format(pSvgFilePath))
        pass
