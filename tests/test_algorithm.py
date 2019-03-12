# -*- coding: utf-8 -*-

import pytest

from heisenbug.algorithm import bubble_sort


@pytest.mark.parametrize('parameter, expected_result', [
    ([0, 5, 3, 2, 2], [0, 2, 2, 3, 5]),
    ([-2, -5, -45], [-45, -5, -2]),
    ([-23, 0, 6, -4, 34], [-23, -4, 0, 6, 34]),
    ([], []),
])
def test_bubble_sort(parameter, expected_result):
    """With this test we illustrate how we should not write tests."""
    assert bubble_sort(parameter) == expected_result
