"""
Project: task_2
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 21/10/2020 7:20 pm
File: stem_and_leaf.py
"""
from typing import List, TypedDict, Optional, Dict, Union
from sorting import heap_sort
from utils import get_digit, get_num_of_digits, remove_duplicates
from hashing import generate_hash
from collections import defaultdict
from models import HashData


class StemAndLeavesEntry(TypedDict):
    stem: int
    leaves: Optional[List[int]]


class StemAndLeaf:
    """A steam-and-leaf implementation that hashes entries"""

    def __init__(self, data: List[int]):
        self.__data = data
        self.__hash_entries = self.hash_all_entries()

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data: List[int]):
        self.__data = new_data

    @property
    def hash_entries(self):
        return self.__hash_entries

    @hash_entries.setter
    def hash_entries(self, hashes: List[HashData]):
        self.__hash_entries = hashes

    def hash_all_entries(self) -> List[HashData]:
        hash_entries = []
        for num in self.__data:
            hash_entry = generate_hash(num=num)
            hash_entries.append(
                HashData(hash_str=hash_entry[0], salt=hash_entry[1], data=num, key=hash_entry[2]))
        return hash_entries

    def sort_data(self, start: int = 0, end: int = -1) -> List[int]:
        """
        Sorts this instance's data without modifying the original one

        :param start: Starting index from which arr will be sorted (inclusive)
        :param end: Ending index up to which arr will be sorted (exclusive)
        :return: None
        """
        return heap_sort(self.__data, start, end)

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

        If it only contains one digit, [0] is returned.

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
        """Retrieves all stems of `data`, leaving out duplicates

        :returns: List of stems
        """
        stems = []
        for num in self.__data:
            stem = StemAndLeaf.get_stem(num)
            # avoid duplicates
            if stem not in stems:
                stems.append(stem)
        return stems

    def search(self, value: int) -> Union[HashData, None]:
        """Searches for an entry in `data` by hashing `value` and comparing it to existing entries.

        A binary search could also be performed here, but hashes are used instead for demonstration purposes.

        :param value: Value to search for in `data`
        :returns: HashData entry from `hash_entries` or None (if not found)

        """
        for index, entry in enumerate(self.__hash_entries):
            value_hash_entry = generate_hash(num=value, salt=entry.salt, key=entry.key)
            if value_hash_entry[0] == entry.hash:
                # hashes match
                return entry
        return None

    def print(self):
        """Prints a graphical representation of this stem-and-leaf diagram, leaving out duplicates.

        Its data must be sorted before printing.
        """

        print()
        print("{:<15} {:<15}".format('Stem', 'Leaves'))
        print('_' * (30 + len('Stem') + len('Leaves')))
        print()

        uniques = remove_duplicates(self.__data)

        stems_and_leaves: Dict[int, List[int]] = defaultdict(list)

        for num in uniques:
            stem = StemAndLeaf.get_stem(num)
            leaf = StemAndLeaf.get_leaf(num)
            numeric_stem = int(''.join(map(str, stem)))

            stems_and_leaves[numeric_stem].append(leaf)

        for key, value in stems_and_leaves.items():
            print("{:<15} {:<15}".format(key, ' '.join(map(str, value))))

    def print_hashes(self):
        """Prints all hash and salt pairs of each entry in the data available

        Includes ALL entries as-is, unsorted and unfiltered.
        """
        print()
        print("{:<15} {:<15} {:<60}".format('Stem', 'Leaf', 'Hash'))
        print('_' * (30 + len('Stem') + len('Leaf') + len('Hash') + len(self.__hash_entries[0].hash)))
        print()

        for index, entry in enumerate(self.__hash_entries):
            leaf = StemAndLeaf.get_leaf(entry.data)
            stem = StemAndLeaf.get_stem(entry.data)
            hash_str = entry.hash

            print("{:<15} {:<15} {:<60}".format(''.join(map(str, stem)), leaf, hash_str))
