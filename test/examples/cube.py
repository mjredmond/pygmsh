#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Creates a mesh on a cube.
'''
import pygmsh as pg


def generate():
    geom = pg.Geometry()
    geom.add_box(0, 1, 0, 1, 0, 1, 1.0)
    return geom, 1.0


if __name__ == '__main__':
    import meshio
    out = pg.generate_mesh(generate()[0])
    meshio.write('cube.vtu', *out)
