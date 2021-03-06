from distutils.core import setup
from Cython.Build import cythonize
import numpy as np


setup(
    name="Conehead",
    ext_modules=cythonize('conehead/dda_3d_c.pyx'),  # accepts a glob pattern
    include_dirs=[np.get_include()]
)
