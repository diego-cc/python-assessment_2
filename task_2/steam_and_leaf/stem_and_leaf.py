"""
Project: task_2
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 21/10/2020 7:20 pm
File: stem_and_leaf.py
"""
from typing import List, TypedDict, Optional, Dict
from sorting import heap_sort
from utils import get_digit, get_num_of_digits, generate_hash, remove_duplicates


class StemAndLeavesEntry(TypedDict):
    stem: int
    leaves: Optional[List[int]]


class HashEntry(TypedDict):
    hash: str
    salt: bytes
    number: int


class StemAndLeaf:
    """A steam-and-leaf implementation that enables visualisation of data in a diagram"""

    def __init__(self, data: List[int]):
        self.__data = data
        self.__hash_entries = []
        for num in self.__data:
            hash_entry = generate_hash(stem=StemAndLeaf.get_stem(num), leaf=StemAndLeaf.get_leaf(num))
            self.__hash_entries.append(HashEntry(hash=hash_entry[0], salt=hash_entry[1], number=num))

    @property
    def data(self):
        return self.__data

    @property
    def hashes(self):
        return self.__hash_entries

    def sort_data(self, start: int = 0, end: int = -1):
        """
        Sorts this instance's data in-place
        :param start: Starting index from which arr will be sorted (inclusive)
        :param end: Ending index up to which arr will be sorted (exclusive)
        :return: None
        """
        self.__data = heap_sort(self.__data, start, end)

    @staticmethod
    def get_leaf(num: int) -> int:
        """Retrieves the last digit of a number as the leaf

        :param num: Number to be evaluated
        :return: Last digit of num
        """
        return num % 10

    @staticmethod
    def get_stem(num: int) -> List[int]:
        """Returns a list containing all digits of a number except the last one as the stem.
        If it only contains one digit, [0] is returned

        :param num: Number to be evaluated
        :return: List containing digits of num except for the last one
        """
        stem = []
        num_of_digits = get_num_of_digits(num)

        if num_of_digits == 1:
            stem.append(0)
            return stem

        for i in range(num_of_digits - 1, 0, -1):
            stem.append(get_digit(num, i))

        return stem

    def get_all_stems(self) -> List[List[int]]:
        stems = []
        for num in self.__data:
            stem = StemAndLeaf.get_stem(num)
            # avoid duplicates
            if stem not in stems:
                stems.append(stem)
        return stems

    def print(self):
        """Prints a graphical representation of this stem-and-leaf diagram.
        Its data is sorted before printing

        :return:
        """
        self.sort_data()

        print('Stem', flush=False, end="")
        print(' ' * 3 + '|' + ' ' * 3, flush=False, end="")
        print('Leaf')
        print('_' * (len('Stem') + 7 + len('Leaf')))
        print()

        uniques = remove_duplicates(self.__data)

        stems_and_leaves: Dict[int, List[int]] = {}

        for num in uniques:
            stem = StemAndLeaf.get_stem(num)
            numeric_stem = int(''.join(map(str, stem)))
            leaf = StemAndLeaf.get_leaf(num)

            if stem not in stems_and_leaves:
                leaves = [leaf]
                stems_and_leaves[numeric_stem] = leaves
            else:
                stems_and_leaves[numeric_stem].append(leaf)

        for key, value in stems_and_leaves:
            print(key, flush=False, end="")
            print(' ' * 3 + '|' + ' ' * 3, flush=False, end="")
            print(value)
            print()
