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


class MapFileHandler(object):
    """
    Reads a roadmap of a city (currently as a SVG file) and represents it as
    a networkx graph.
    """
    def __init__(self, pInputFilePath, pOutputFilePath):
        """
        Behaviour:
         Init class with file at pInputFilePath and pOutputFilePath.

        Arguments:
         pInputFilePath -- the path to the readable file from which to parse
                           the streets.
         pOutputFilePath -- the path where to write paths (modified or new
                            paths).
        """
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug(
                "File to get paths from is {}".format(pInputFilePath))
            logger.debug(
                "File to write paths to is {}".format(pOutputFilePath))

        self._inputFilePath = pInputFilePath
        self._outputFilePath = pOutputFilePath
        self._inputHandler = self._getInputFileHandler()
        pass

    def setPointClass(self, pPointClass):
        """
        See MapInputHandler.setPointClass.
        """
        pass

    def setSegmentClass(self, pSegmentClass):
        """
        See MapInputHandler.setSegmentClass.
        """
        pass

    def _getInputFileHandler(self):
        """
        Behaviour:
         Decides which input handler class to return by file type of
         'self._inputFilePath'.

        Return value:
         - MapInputHandler -- returns a input handler class

        Restrictions:
         Currently it returns only MapInputSVG.
        """
        pass



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


class MapOutputHandler(object):
    """
    Handles the writing of a street network with blocks to a file.
    """
    def __init__(self, pOutputFilePath):
        """
        Behaviour:
         Init class with pOutputFilePath.

        Arguments:
         pOutputFilePath -- the path where to write paths (modified or new
                            paths).
        """
        self._outputFilePath = pOutputFilePath
        pass
