from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("hello_world",  ["hello_world.py"]),
    Extension("what_time_is_it",  ["what_time_is_it.py"]),
    #   ... all your modules that need be compiled ...
]

setup(
    name = 'Cython Basics',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)