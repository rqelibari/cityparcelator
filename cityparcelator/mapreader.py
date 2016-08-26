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
    def __init__(self, pInputFilePath, pOutputFilePath):
        """
        Behaviour:
         Init class with file at svgFilePathself. Calls 'parseSVGFile'.

        Arguments:
         pInputFilePath -- the path to the readable file from which to parse
                           the streets.
         pOutputFilePath -- the path where to write paths (modified or new
                            paths).
        """
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug(
                "File to get paths from is {}".format(pInputFilePath))
        self._inputFilePath = pInputFilePath
        self._outputFilePath = pOutputFilePath
        self._pointClass = tuple
        self._segmentClass = tuple
        pass

    def setPointClass(self, pPointClass):
        """
        Behaviour:
        Set the class, which shall be used to represent the endpoints of a
        street. Default is tuple.

        Arguments:
         pPointClass -- A reference to the class which shall represent points.
                        Constructor of the class must take two arguments
                        (x, y).

        Restrictions:
         Paths, parsed before the call will remain unchanged.
        """
        self._pointClass = pPointClass

    def setSegmentClass(self, pSegmentClass):
        """
        Behaviour:
        Set the class, which shall be used to represent the segment of a
        street. Default is tuple.

        Arguments:
         pSegmentClass --  A reference to the class which shall represent line
                           segments. Constructor of the class must take two
                           arguments (startPoint, endPoint), both of type
                           _pointClass (can be set with self.setPointClass).

        Restrictions:
         Segments, parsed before the call will remain unchanged.
        """
        self._segmentClass = pSegmentClass
