"""

pyslurm: Python interface to slurm

"""

from distutils.core import setup
from distutils.extension import Extension
from distutils.command import clean
from distutils.sysconfig import get_python_lib
from Cython.Distutils import build_ext

import os, re
import sys, platform
from string import *
from stat import *

here = os.getcwd()

include_dirs = [
    here + '/include',
    '/usr/include/slurm',
    '/usr/include',
    '/usr/local/include/slurm',
    '/usr/local/include',
]
library_dirs = [
    '/usr/lib/slurm',
    '/usr/lib'
    '/usr/local/lib/slurm',
    '/usr/local/lib',
]
libraries = ['slurm']
runtime_library_dirs = [
    '/usr/lib/slurm',
    '/usr/lib',
    '/usr/local/lib/slurm',
    '/usr/local/lib',
]
extra_objects = [
    obj for obj in [
        '/usr/lib/slurm/auth_none.so',
        '/usr/local/lib/slurm/auth_none.so',
    ] if os.path.exists(obj)
]

if len(extra_objects) == 0:
    print "Error:  Could not find `slurm/auth_none.so`"
    sys.exit(1)

classifiers = """\
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: GNU General Public License (GPL)
Natural Language :: English
Operating System :: POSIX :: Linux
Programming Language :: Python
Topic :: Software Development :: Libraries :: Python Modules
"""

doclines = __doc__.split("\n")

setup(
    name = "pyslurm",
    version = "0.0.1",
    description = doclines[0],
    long_description = "\n".join(doclines[2:]),
    author = "Mark Roberts",
    author_email = "mark at gingergeeks co uk",
    url = "http://www.gingergeeks.co.uk/pyslurm/",
    classifiers = filter(None, classifiers.split("\n")),
    platforms = ["Linux"],
    keywords = ["Batch Scheduler", "slurm"],
    packages = ["pyslurm"],
    ext_modules = [
        Extension( "pyslurm.pyslurm",["pyslurm/pyslurm.pyx"],
                   library_dirs = library_dirs,
                   libraries = libraries,
                   runtime_library_dirs = runtime_library_dirs,
                   extra_objects = extra_objects,
                   include_dirs = include_dirs)
    ],
    cmdclass = {"build_ext": build_ext}
)

