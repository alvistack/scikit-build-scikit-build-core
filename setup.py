from setuptools import setup

setup(
    name='scikit-build-core',
    version='0.12.1',
    description='Build backend for CMake based projects',
    author_email='Henry Schreiner <henryfs@princeton.edu>',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: Free Threading :: 4 - Resilient',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Build Tools',
        'Typing :: Typed',
    ],
    install_requires=[
        'exceptiongroup>=1.0; python_version < "3.11"',
        'importlib-resources>=1.3; python_version < "3.9"',
        'packaging>=23.2',
        'pathspec>=0.10.1',
        'tomli>=1.2.2; python_version < "3.11"',
        'typing-extensions>=4; python_version < "3.11"',
    ],
    extras_require={
        'wheel-free-setuptools': [
            'setuptools>=70.1; python_version >= "3.8"',
        ],
        'wheels': [
            'cmake',
            'ninja; sys_platform != "win32"',
        ],
    },
    entry_points={
        'distutils.commands': [
            'build_cmake = scikit_build_core.setuptools.build_cmake:BuildCMake',
        ],
        'distutils.setup_keywords': [
            'cmake_args = scikit_build_core.setuptools.build_cmake:cmake_args',
            'cmake_install_target = scikit_build_core.setuptools.build_cmake:cmake_install_target',
            'cmake_source_dir = scikit_build_core.setuptools.build_cmake:cmake_source_dir',
        ],
        'hatch': [
            'scikit-build = scikit_build_core.hatch.hooks',
        ],
        'setuptools.finalize_distribution_options': [
            'scikit_build_entry = scikit_build_core.setuptools.build_cmake:finalize_distribution_options',
        ],
        'validate_pyproject.tool_schema': [
            'scikit-build = scikit_build_core.settings.skbuild_schema:get_skbuild_schema',
        ],
    },
    packages=[
        'scikit_build_core',
        'scikit_build_core._compat',
        'scikit_build_core._compat.importlib',
        'scikit_build_core._vendor.pyproject_metadata',
        'scikit_build_core.ast',
        'scikit_build_core.build',
        'scikit_build_core.builder',
        'scikit_build_core.file_api',
        'scikit_build_core.file_api.model',
        'scikit_build_core.hatch',
        'scikit_build_core.metadata',
        'scikit_build_core.resources',
        'scikit_build_core.resources.find_python',
        'scikit_build_core.settings',
        'scikit_build_core.setuptools',
    ],
    package_dir={'': 'src'},
    include_package_data=True,
)
