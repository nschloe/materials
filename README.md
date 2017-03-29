# materials

[![Build Status](https://travis-ci.org/nschloe/materials.svg?branch=master)](https://travis-ci.org/nschloe/materials)
[![codecov](https://codecov.io/gh/nschloe/materials/branch/master/graph/badge.svg)](https://codecov.io/gh/nschloe/materials)
[![Code Health](https://landscape.io/github/nschloe/materials/master/landscape.png)](https://landscape.io/github/nschloe/materials/master)
[![PyPi Version](https://img.shields.io/pypi/v/materials.svg)](https://pypi.python.org/pypi/materials)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/materials.svg?style=social&label=Star&maxAge=2592000)](https://github.com/nschloe/materials)


### Installation

materials is [available from the Python Package
Index](https://pypi.python.org/pypi/materials/), so simply type
```
pip install -U materials
```
to install or upgrade.

### Testing

To run the materials unit tests, check out this repository and type
```
pytest
```

### Distribution

To create a new release

1. bump the `__version__` number,

2. publish to PyPi and GitHub:
    ```
    make publish
    ```

### License

materials is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
