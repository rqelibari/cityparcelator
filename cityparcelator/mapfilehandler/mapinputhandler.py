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


class MapInputHandler(object):
    """
    Handles the parsing of a file which contains a street network.
    """
    def __init__(self, pInputFilePath, pPointClass = None,
                 pSegmentClass = None):
        """
        Behaviour:
         Init class with file at pInputFilePath and pOutputFilePath.

        Arguments:
         pInputFilePath -- the path to the readable file from which to parse
                           the streets.
         pPointClass -- see self.setPointClass
         pSegmentClass -- see self.setSegmentClass
        """
        self._inputFilePath = pInputFilePath
        self._pointClass = tuple if pPointClass is None else pPointClass
        self._segmentClass = tuple if pSegmentClass is None else pSegmentClass
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

    def parseFile(self):
        raise NotImplementedError("Should be implemented in subclasses.")
