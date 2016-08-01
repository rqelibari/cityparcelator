# Cityparcelator
Cityparcelator is a python 3 engine, which generates building parcels on a SVG street map using a blocksubdivision algorithm.
The street map must be a SVG file with `<path>`-elements. The script will write a new SVG file with new `<polygon>`-elements, which represent the different bulding parcels/blocks inside the streetmap.

# How to use
Clone the repository, open a Termial and `cd` into it. Then run:

    # pip install .
    # cityparcelator ./input.svg ./output.svg

More information is following during the development.
