# -*- coding: utf-8 -*-


def bubble_sort(array):
    """
    Pure implementation of bubble sort algorithm in Python.

    Args:
        array: Some mutable ordered array with heterogeneous
            comparable items inside.

    Returns:
        The same array ordered by ascending.

    Examples:

        >>> bubble_sort([0, 5, 3, 2, 2])
        [0, 2, 2, 3, 5]
        >>> bubble_sort([])
        []
        >>> bubble_sort([-2, -5, -45])
        [-45, -5, -2]
        >>> bubble_sort([-23, 0, 6, -4, 34])
        [-23, -4, 0, 6, 34]

    """
    length = len(array)
    for first in range(length - 1):
        swapped = False
        for second in range(length - 1 - first):
            if array[second] > array[second + 1]:
                swapped = True
                array[second], array[second + 1] = (
                    array[second + 1],
                    array[second],
                )
        if not swapped:
            break  # Stop iteration if the array is sorted.
    return array
