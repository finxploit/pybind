# -*- coding: utf-8 -*-
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

tests_require = [
    'pytest',
    'pytest-cache',
    'pytest-cov',
    'pytest-mock'
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


requires = [
    'click>=6.7',
    'pyyaml>=3.12'
]

VERSION = open('VERSION').read().strip()

setup(
    name="osiris-ext",
    version=VERSION,
    description="Fast computation extensions for osiris framework",
    long_description="\n\n".join([open("README.rst").read()]),
    license='GPL 3.0',
    author="Dimitar Petrov",
    author_email="petrov.dimp@gmail.com",
    url="https://osiris-ext.readthedocs.org",
    packages=find_packages(),
    install_requires=requires,
    include_package_data=True,
    entry_points={'console_scripts': [
        'console = osiris-ext.console:main']},
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GPL 3.0 License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython'],
    extras_require={'test': tests_require},
    cmdclass={'test': PyTest})
