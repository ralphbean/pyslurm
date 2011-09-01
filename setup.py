"""

pyslurm: Python interface to slurm

"""

from distutils.core import setup
from distutils.extension import Extension
from distutils.command import clean
from distutils.sysconfig import get_python_lib
from Cython.Distutils import build_ext

import optparse
import os
import re
import sys
import platform
from string import *
from stat import *

def die(msg, parser=None):
    """ Die with a message. """

    print
    print "ERROR:", msg
    print

    if parser:
        parser.print_help()

    sys.exit(1)


class opts(object):
    """ Class to hold developer-specific options for the build.

    Modify to meet your needs.
    """

    # Auth plugin used by slurm.  I.e., `munge` or `none`.
    auth = 'munge'

    # Prefix of slurm install.  I.e., if the libraries are in
    # /opt/slurm/lib/slurm, then specify prefix=/opt/slurm.
    prefix = '/usr/local'


here = os.getcwd()

include_dirs = [
    here + '/include',
    opts.prefix + "/include",
    opts.prefix + "/include/slurm",
]
library_dirs = [
    opts.prefix + "/lib",
    opts.prefix + "/lib/slurm",
]
runtime_library_dirs = library_dirs
libraries = ['slurm']

auth_plugin = "{opts.prefix}/lib/slurm/auth_{opts.auth}.so".format(opts=opts)
extra_objects = [auth_plugin]

if not os.path.exists(auth_plugin):
    die("Could not find {auth_plugin}.".format(auth_plugin=auth_plugin))

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
    name="pyslurm",
    version="0.0.1",
    description=doclines[0],
    long_description="\n".join(doclines[2:]),
    author="Mark Roberts",
    author_email="mark at gingergeeks co uk",
    url="http://www.gingergeeks.co.uk/pyslurm/",
    classifiers=filter(None, classifiers.split("\n")),
    platforms=["Linux"],
    keywords=["Batch Scheduler", "slurm"],
    packages=["pyslurm"],
    ext_modules=[
        Extension("pyslurm.pyslurm", ["pyslurm/pyslurm.pyx"],
                   library_dirs=library_dirs,
                   libraries=libraries,
                   runtime_library_dirs=runtime_library_dirs,
                   extra_objects=extra_objects,
                   include_dirs=include_dirs)
    ],
    cmdclass={"build_ext": build_ext}
)
