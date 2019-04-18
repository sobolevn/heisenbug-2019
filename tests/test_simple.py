# -*- coding: utf-8 -*-

from heisenbug.simple import add


def test_add():
    """With this test we illustrate how we should not write tests."""
    assert add(0, 0) == 0
    assert add(2, 2) == 4

    # TODO: uncomment the following line to solve this case:
    # assert add(3, 5) == 8
