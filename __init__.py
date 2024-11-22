import numpy as np
import os

import pyximport
pyximport.install(setup_args={
    'script_args': ["--cython-cplus"],
    'include_dirs': [os.path.realpath(os.path.dirname(__file__)), np.get_include()]
})

from .dbscanpp import DBSCANPP
