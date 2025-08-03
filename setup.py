"""Setup for pymagsac."""
import sys

from setuptools import find_packages

try:
    from skbuild import setup
except ImportError:
    print("Please update pip to pip 10 or greater, or a manually install the PEP 518 requirements in pyproject.toml", file=sys.stderr)
    raise

cmake_args = []
debug = False
cfg = 'Debug' if debug else 'Release'
cmake_args += ['-DCMAKE_BUILD_TYPE=' + cfg]
cmake_args += ['-DCREATE_SAMPLE_PROJECT=OFF']  # <-- Disable the sample project
cmake_args += ['-DCMAKE_POSITION_INDEPENDENT_CODE=ON']  # Ensure PIC for shared libraries

setup(
    name='pymagsac',
    version='0.3.dev0',
    author='Daniel Barath, Dmytro Mishkin',
    author_email='barath.daniel@sztaki.hu',
    description='MAGSAC and MAGSAC++',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    cmake_args=cmake_args,
    cmake_install_dir="src/pymagsac",
    cmake_source_dir=".",  # Specify the source directory
    cmake_minimum_required_version="3.8",
    zip_safe=False,
    install_requires="numpy",
    python_requires=">=3.7",
)
