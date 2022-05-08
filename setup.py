import os
from glob import glob

from distutils.core import setup

try:
    from Cython.Distutils.extension import Extension
    from Cython.Distutils import build_ext
except ImportError:
    from setuptools import Extension
    USING_CYTHON = False
else:
    USING_CYTHON = True

ext = 'pyx' if USING_CYTHON else 'c'
sources = glob('src/pystml/*.%s' % (ext,))
extensions = [
    Extension(source.split('.')[0].replace(os.path.sep, '.'),
              sources=[source],
    )
for source in sources]
cmdclass = {'build_ext': build_ext} if USING_CYTHON else {}

setup(ext_modules=extensions, cmdclass=cmdclass)