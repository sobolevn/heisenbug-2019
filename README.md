# Heisenbug 2019

[![wemake.services](https://img.shields.io/badge/%20-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake.services)
[![Build Status](https://travis-ci.org/sobolevn/heisenbug-2019.svg?branch=master)](https://travis-ci.org/sobolevn/heisenbug-2019)
[![Coverage](https://coveralls.io/repos/github/sobolevn/heisenbug-2019/badge.svg?branch=master)](https://coveralls.io/github/sobolevn/heisenbug-2019?branch=master)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/sobolevn/heisenbug-2019)

Demo app that shows how can we effectively use mutation testing.

## Contents

### simple.py

This example is used to illustrate the simplest use-case possible.
We only have a function with a single statement.
This statement will be mutated, our mutation test will catch that.

### opensource_disl_case.ipynb

This is a real-world example about
my open-source project called [`docker-image-size-limit`](https://github.com/wemake-services/docker-image-size-limit).

It is a perfectly working app with just 70 lines for simple `python` code.
Fully tested with E2E and unit tests, typed, 100% covered.
And it has 10 surviving mutants.

This article shows you exactly what happened and how to solve this case.


## Resources

You might also be interested in:

- https://nedbatchelder.com/blog/201903/mutmut.html


## License

Content is licensed under [CC BY-NC](https://creativecommons.org/licenses/by-nc/4.0/)
