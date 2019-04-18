# -*- coding: utf-8 -*-

from typing import List


def bubble_sort(array: List[int]) -> List[int]:
    """
    Pure implementation of bubble sort algorithm in Python.

    Args:
        array: Some mutable ordered array with heterogeneous
            integers as items inside.

    Returns:
        The same array ordered by ascending.

    """
    length = len(array)
    for first in range(length - 1):
        for second in range(length - 1 - first):
            if array[second] > array[second + 1]:
                array[second], array[second + 1] = (  # noqa: Z446
                    array[second + 1],
                    array[second],
                )
    return array
