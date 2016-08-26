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
from cityparcelator.mapfilehandler.mapinputhandler import MapInputHandler
from xml.dom.minidom import parse
from svg.path import parse_path
logger = logging.getLogger(__name__)


class MapInputSVGHandler(MapInputHandler):
    FLOAT_PRECISION = 2

    """
    Handles the parsing of a SVG file which contains a street network.
    """
    def parseFile(self):
        """
        Behaviour:
         Parse streets from svg paths. SVG paths will be read using
         xml.dom.minidom.parse and parsed using svg.path

        Exceptions:
         See xml.dom.minidom.parse

        Restrictions:
         Currently there are only SVG files supported.
        """

        doc = parse(self._inputFilePath)
        self.streets = self._getSVGPathsFromMinidom(doc)
        doc.unlink()

    def _getSVGPathsFromMinidom(self, pMinidom):
        paths = []
        for path in pMinidom.getElementsByTagName("path"):
            dAttributeOfPath = path.getAttribute('d')
            parsedPath = parse_path(dAttributeOfPath)
            paths.append(self._castMinidomParsedPath(parsedPath))
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug("Parsed SVG paths are {}".format(paths))
        return paths

    def _castMinidomParsedPath(self, pParsedPath):
        assert len(pParsedPath) == 1, "Path contains only one line."
        FP = self.FLOAT_PRECISION
        SVGSegment = pParsedPath[0]
        startPoint = self._pointClass(Float(SVGSegment.start.real, FP),
                                      Float(SVGSegment.start.imag, FP))
        endPoint = self._pointClass(Float(SVGSegment.end.real, FP),
                                    Float(SVGSegment.end.imag, FP))
        return self._segmentClass(startPoint, endPoint)
