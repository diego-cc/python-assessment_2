"""
Project: task_2
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 21/10/2020 8:19 pm
File: binary_search.py
"""
from math import floor

from typing import List


def binary_search(data: List[int], value: int, start: int = 0, end: int = -1) -> int:
    """An iterative binary search implementation. Data must be sorted before running this function.

    :param data: Initial data set (must be sorted in advance)
    :param value: Number to look for in `data`
    :param start: Optional starting index (inclusive)
    :param end: Optional end index (inclusive)
    :returns: Index of `value` in `data` (or -1 if not found)
    """

    if end == -1:
        end = len(data) - 1

    left = start
    right = end

    while left <= right:
        mid = floor((left + right) / 2)
        if data[mid] < value:
            left = mid + 1
        elif data[mid] > value:
            right = mid - 1
        else:
            return mid
    return -1
