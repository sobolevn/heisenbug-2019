# -*- coding: utf-8 -*-

import pytest

from heisenbug.constants import BAD_FUNCTION_NAMES, is_bad_function_name


@pytest.mark.parametrize('function_name', BAD_FUNCTION_NAMES)
def test_is_bad_function_name(function_name):
    """Ensures that bad function names cannot be used."""
    assert is_bad_function_name(function_name) is True


def test_is_good_function_name():
    """Ensures that good function names can be used."""
    assert is_bad_function_name('good_name') is False


# TODO: solve the constant case!
# @pytest.mark.parametrize('function_name', [
#     'dir', 'vars', 'locals', 'globals',
# ])
# def test_correct_way(function_name):
#     """That's how it should be!"""
#     assert is_bad_function_name(function_name) is True
