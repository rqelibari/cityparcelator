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
