# -*- coding: utf-8 -*-


BAD_FUNCTION_NAMES = ['dir', 'vars', 'locals', 'globals']


def is_bad_function_name(name: str):
    """Returns if this function should be forbidden to use."""
    return name in BAD_FUNCTION_NAMES
