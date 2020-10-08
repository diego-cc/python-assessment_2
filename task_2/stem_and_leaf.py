"""
Project: python-assessment_2
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 08/10/2020 10:23 am
File: stem_and_leaf.py
"""
from typing import List
from task_2.heap_sort import heap_sort
from task_2.utils import get_last_digit


class SteamAndLeaf:
    """A steam-and-leaf implementation that enables visualisation of data in a diagram"""

    def __init__(self, data: List[int]):
        self.__data = data

    @property
    def data(self):
        return self.__data

    def sort_data(self, start: int = 0, end: int = -1):
        """
        Sorts this instance's data in-place
        :param start: Starting index from which arr will be sorted (inclusive)
        :param end: Ending index up to which arr will be sorted (exclusive)
        :return: None
        """
        self.__data = heap_sort(self.__data, start, end)

    @staticmethod
    def get_leaf(self, num: int):
        return num % 10

    def print_diagram(self):
        self.sort_data()

        # organise numbers by stems and leaves
        for num in self.__data:
            print(get_last_digit(num))
