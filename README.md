# ANSIConv

*Version: 1.0.0*

A Python module for converting ANSI coded text and converts it to either plain
text or HTML.

**Documentation:** [http://pythonhosted.org/ansiconv/](http://pythonhosted.org/ansiconv/)

**Test Coverage:** 100%

## Installing

### From PyPI

    $ pip install ansiconv

### From Git

    $ git clone https://bitbucket.org/dhrrgn/ansiconv.git
    $ cd ansiconv
    $ python setup.py install

## Testing

You can run the unit tests by running the following command:

    $ python setup.py test

### Coverage Report

**The coverage report requires `pytest-cov` (`pip install pytest-cov`).**

In the ansicov directory run the following command:

    $ py.test --cov=ansiconv.py --cov-report=term

*The tests are written using `pytest`.*
