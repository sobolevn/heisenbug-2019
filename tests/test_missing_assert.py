# -*- coding: utf-8 -*-

import pytest

from heisenbug.missing_assert import negate


@pytest.mark.parametrize('given, expected', [
    (-1, 1),
    (0, 0),
    (0.5, -0.5),
])
def test_negate(given, expected):
    """Please, do not forget to uncomment assert later."""
    function_result = negate(given)
    print(function_result)  # noqa: T001

    # TODO: uncomment this line after my experiments:
    # assert function_result == expected
