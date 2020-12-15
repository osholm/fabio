# coding: utf-8
# /*##########################################################################
# Copyright (C) 2016 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ############################################################################*/

__authors__ = ["V. Valls"]
__license__ = "MIT"
__date__ = "14/12/2020"

import os
import numpy
from numpy.distutils.misc_util import Configuration


def configuration(parent_package='', top_path=None):
    config = Configuration('ext', parent_package, top_path)

    config.add_extension(
        name="cf_io",
        sources=["cf_io.pyx", os.path.join("src", "columnfile.c")],
        include_dirs=["include", numpy.get_include()],
        language='c')

    config.add_extension(
        name="byte_offset",
        sources=["byte_offset.pyx"],
        include_dirs=[numpy.get_include()],
        language='c')

    config.add_extension(
        name="mar345_IO",
        sources=["mar345_IO.pyx", os.path.join("src", "ccp4_pack.c")],
        include_dirs=["include", numpy.get_include()],
        language='c')

    config.add_extension(
        name="_cif",
        sources=["_cif.pyx"],
        language='c')

    config.add_extension(
        name="_agi_bitfield",
        sources=["_agi_bitfield.pyx"],
        language='c')

    config.add_extension(
        name="dense",
        sources=["dense.pyx"],
        include_dirs=[numpy.get_include()],
        language='c')

    return config


if __name__ == "__main__":
    from numpy.distutils.core import setup
    setup(configuration=configuration)
