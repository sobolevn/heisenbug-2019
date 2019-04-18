# Heisenbug 2019

[![wemake.services](https://img.shields.io/badge/%20-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake.services)
[![Build Status](https://travis-ci.org/sobolevn/heisenbug-2019.svg?branch=master)](https://travis-ci.org/sobolevn/heisenbug-2019)
[![Coverage](https://coveralls.io/repos/github/sobolevn/heisenbug-2019/badge.svg?branch=master)](https://coveralls.io/github/sobolevn/heisenbug-2019?branch=master)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/sobolevn/heisenbug-2019)

Demo app that shows how can we effectively use mutation testing.

## Contents

### missing_assert.py

This is a very basic example of test that does not do anything.
Because we have missed that our `assert` is commented out by accident!

```
⠙ 2/2  🎉 0  ⏰ 0  🤔 0  🙁 2
```

To solve this, just uncomment the `assert` in [test_missing_assert.py](https://github.com/sobolevn/heisenbug-2019/blob/master/tests/test_missing_assert.py)

### simple.py

This example is used to illustrate the simplest use-case possible.
We only have one function with a single statement.
This statement will be mutated, our mutation test will catch that.

```
⠼ 1/1  🎉 0  ⏰ 0  🤔 0  🙁 1
```

The solution to this case is available here: [test_simple.py](https://github.com/sobolevn/heisenbug-2019/blob/master/tests/test_simple.py)

### constants.py

Using the same constants for testing and production
does not actually test anything.

```
⠇ 6/6  🎉 2  ⏰ 0  🤔 1  🙁 3
```

Since we will miss cases like this one:

```diff
--- heisenbug/constants.py
+++ heisenbug/constants.py
@@ -1,7 +1,7 @@
 # -*- coding: utf-8 -*-


-BAD_FUNCTION_NAMES = ['dir', 'vars', 'locals', 'globals']
+BAD_FUNCTION_NAMES = ['dir', 'vars', 'locals', 'XXglobalsXX']
```

The tests will move in sync with the production code, following the bugs introduced there!

Solution: duplicate your constants in tests, see [test_constants.py](https://github.com/sobolevn/heisenbug-2019/blob/master/tests/test_constants.py)

### flask_app.py

This example represents a regular `flask` application.
It is configured to swallow exceptions and log them somewhere.

It seems to be fully tested, but has one big mistake inside.

```
⠋ 10/10  🎉 2  ⏰ 0  🤔 0  🙁 8
```

This is the case we are looking for:

```diff
--- heisenbug/flask_app.py
+++ heisenbug/flask_app.py
@@ -18,7 +18,7 @@
 @app.route('/{int:index}')
 def hello(index):
     """View that will fail in production."""
-    return 'Hello, world! {0} faith in you.'.format(1 * index)
+    return 'Hello, world! {0} faith in you.'.format(1 / index)
```

Since we swallow exceptions and test only partial of our output,
we will never be able to find the problem of when input is zero and causes a divide by zero.

Main take-away: high-level integrations tests are not good enough on their own.

Solution: do not use `200` code where something goes wrong,
make sure that you write enough unit-tests for your view logic.

### algorithm.py

This is a simple `bubble_sort` algorithm.

I have taken an example algorithm as is from [`TheAlgorithms/Python`](https://github.com/TheAlgorithms/Python/blob/master/sorts/bubble_sort.py),
which is a very popular `python` library.

This is the result (please, take a not that it has several false positives):

```
⠼ 20/20  🎉 15  ⏰ 0  🤔 0  🙁 5
```

You can see that we even use property-based tests [here](https://github.com/sobolevn/heisenbug-2019/blob/master/tests/test_algorithm.py).

But it still does not save us from the false-positives of mutation testing.

Main take-away: it is really hard to use mutation testing
to test algorithms built with performance and optimisations in mind.

### opensource_disl_case.ipynb

This is a real-world example about
my open-source project called [`docker-image-size-limit`](https://github.com/wemake-services/docker-image-size-limit).

It is a perfectly working app with just 70 lines for simple `python` code.
Fully tested with E2E and unit tests, typed, 100% covered.
And it has [~10 surviving mutants](https://github.com/sobolevn/heisenbug-2019/blob/master/heisenbug/opensource_disl_case.ipynb).

```
⠇ 29/29  🎉 19  ⏰ 0  🤔 2  🙁 8
```

This article shows you exactly what happened and how to solve this case.


## Resources

Here I have collected different resource that you might also be interested in.

### Articles

- https://hackernoon.com/mutmut-a-python-mutation-testing-system-9b9639356c78
- https://nedbatchelder.com/blog/201903/mutmut.html

### Talks

- https://vimeo.com/191364978
- https://vimeo.com/171319754


## License

Content is licensed under [CC BY-NC](https://creativecommons.org/licenses/by-nc/4.0/)
