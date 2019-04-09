# -*- coding: utf-8 -*-
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

tests_require = [
    'pytest',
    'pytest-cache',
    'pytest-cov',
    'pytest-benchmark',
    'tox',
    'tox-pyenv',
    'pylint'
]


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


VERSION = open('VERSION').read().strip()

setup(
    name="pybind",
    version=VERSION,
    description="Fast computation extensions for osiris framework",
    long_description="\n\n".join([open("README.rst").read()]),
    license='GPL 3.0',
    author="Dimitar Petrov",
    author_email="petrov.dimp@gmail.com",
    url="https://pybind.readthedocs.org",
    setup_requires=["cffi>=1.0.0"],
    cffi_modules=["pybind/cnufft/cnufft_build.py:ffibuilder"],
    install_requires=["cffi>=1.0.0", "numpy>=1.16", "numba>=0.43.1"],
    include_package_data=True,
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GPL 3.0 License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython'],
    extras_require={'test': tests_require},
    cmdclass={'test': PyTest})
