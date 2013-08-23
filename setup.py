import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name="ansiconv",
    version="1.0.0",
    author="Dan Horrigan",
    author_email="dan@dhorrigan.com",
    url="https://bitbucket.org/dhrrgn/ansiconv",
    description="Converts ANSI coded text and converts it to either plain text or to HTML.",
    long_description="See documentation at http://pythonhosted.org/ansiconv/",
    license='MIT',
    py_modules=['ansiconv'],
    tests_require=['pytest'],
    test_suite='test.test_ansiconv',
    cmdclass={
        'test': PyTest
    },
    extras_require={
        'testing': ['pytest'],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
    ],
)
