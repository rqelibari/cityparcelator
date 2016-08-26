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
import click
from cityparcelator.mapfilehandler.mapfilehandler import MapFileHandler


@click.command()
@click.option('--variance', '-v', help='Variance of subdivision.',
              default=.5, type=float)
@click.option('--max', '-M', help='Max sidelength in meters subdivision box.',
              default=55, type=float)
@click.option('--min', '-m',
              help='Min sidelength in meters of subdivision box.', default=10,
              type=float)
@click.argument('svgfile', type=click.Path(exists=True))
@click.argument('outfile', type=click.Path(), default="output.svg")
def cli(svgfile, outfile, variance, min, max):
    """Read SVG file and generate parcels."""
    mp = MapFileHandler(svgfile, outfile)
    pass
