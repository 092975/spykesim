##from distutils.core import setup
##from distutils.extension import Extension
##from Cython.Build import cythonize
##import Cython.Compiler.Options
##import numpy
### Cython.Compiler.Options.annotate = True
##
##setup(
##    name = "editsim",
##    ext_modules=cythonize("editsim.pyx"),
##    include_dirs = [numpy.get_include()],
##    extra_compile_args=['-fopenmp'],
##    extra_link_args=['-fopenmp'],
##)
from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy  
setup(
  name = "editsim",
  cmdclass = {"build_ext": build_ext},
  include_dirs = [numpy.get_include()],
  ext_modules =
  [
    Extension("editsim",
              ["editsim.pyx"],
              extra_compile_args = ["-O0", "-fopenmp"],
              extra_link_args=['-fopenmp']
              )
  ]
)

