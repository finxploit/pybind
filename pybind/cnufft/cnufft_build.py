#! /usr/bin/env python

"""
    File name: cnufft_build.py
    Author: Dimitar Petrov
    Date created: 2019/03/28
    Python Version: 3.6
    Description: NuFFT FFI Builder
"""

import os
import subprocess
import cffi


folder = os.path.dirname(os.path.abspath(__file__))
subprocess.call(['make', '-C', f'{folder}'])

ffibuilder = cffi.FFI()

with open(os.path.join(folder, "cnufft.h")) as f:
    ffibuilder.cdef(f.read())

ffibuilder.set_source(
    "pybind.cnufft._cnufft",
    '#include "cnufft.h"',
    libraries=["cnufft", "fnufft"],
    library_dirs=[folder,],
    include_dirs=[folder,],
    extra_link_args=['-Wl,-rpath=$ORIGIN/'],
)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
