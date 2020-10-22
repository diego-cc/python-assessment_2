"""
Project: task_2
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 21/10/2020 7:19 pm
File: heap_sort.py
"""
from typing import List
from heapq import heappop, heappush


def heap_sort(data: List[int], start: int = 0, end: int = -1) -> List[int]:
    """A basic heapsort implementation using the built-in `heapq` module.

    It takes an unordered list of integers, inserts each number into another list while
    maintaining it as a heap structure then pops each number in order into
    a third list (just like a queue), starting by the smallest one.

    Numbers are sorted in ascending order.

    :param data: List to be sorted
    :param start: Starting index from which data will be sorted (inclusive)
    :param end: Ending index up to which data will be sorted (exclusive)
    :returns: Sorted list
    """
    heap = []

    if end <= -1:
        end = len(data) - 1

    for item in data[start:end]:
        heappush(heap, item)

    ordered_data = []

    while heap:
        ordered_data.append(heappop(heap))

    return ordered_data
