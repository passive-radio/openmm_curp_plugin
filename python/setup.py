from distutils.core import setup
from distutils.extension import Extension
import os
import sys
import platform

openmm_dir = '@OPENMM_DIR@'
curp_plugin_header_dir = '@CURP_PLUGIN_HEADER_DIR@'
curp_plugin_library_dir = '@CURP_PLUGIN_LIBRARY_DIR@'

extra_compile_args = ['-std=c++11']
extra_link_args = []

if platform.system() == 'Darwin':
    extra_compile_args += ['-stdlib=libc++', '-mmacosx-version-min=10.7']
    extra_link_args += ['-stdlib=libc++', '-mmacosx-version-min=10.7', '-Wl', '-rpath', 'openmm_lib_path']

extention =Extension(name='_openmmcurp',
                    sources=['CURPPluginWrapper.cpp'],
                    libraries=['OpenMM', 'OpenMMCURP'],
                    include_dirs=[os.path.join(openmm_dir, 'include'), curp_plugin_header_dir],
                    library_dirs=[os.path.join(openmm_dir, 'lib'), curp_plugin_library_dir],
                    runtime_library_dirs=[os.path.join(openmm_dir, 'lib')],
                    extra_compile_args=extra_compile_args,
                    extra_link_args=extra_link_args
            )

setup(name='openmmcurp',
        version='0.0.1',
        py_modules=['openmmcurp'],
        ext_modules=[extention]
    )
