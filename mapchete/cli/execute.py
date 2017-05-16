#!/usr/bin/env python
"""Command line utility to execute a Mapchete process."""

import os
from multiprocessing import cpu_count

import mapchete


def main(args=None):
    """Execute a Mapchete process."""
    parsed = args

    if parsed.input_file and not (
        os.path.isfile(parsed.input_file) or os.path.isdir(parsed.input_file)
    ):
        raise IOError("input_file not found")

    multi = parsed.multi if parsed.multi else cpu_count()
    mode = "overwrite" if parsed.overwrite else "continue"
    if parsed.zoom:
        zoom = parsed.zoom
    elif parsed.tile:
        zoom = parsed.tile[0]
    else:
        zoom = None

    # initialize and run process
    with mapchete.open(
        parsed.mapchete_file, bounds=parsed.bounds, mode=mode,
        zoom=zoom, single_input_file=parsed.input_file, debug=parsed.debug
    ) as mp:
        mp.batch_process(
            tile=parsed.tile, multi=multi, quiet=parsed.quiet,
            debug=parsed.debug)
