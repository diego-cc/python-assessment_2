"""
Project: python-assessment_2
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 08/10/2020 1:39 pm
File: __init__.py
"""
from typing import List
from sorting import heap_sort
from utils import get_digit, get_num_of_digits
from models import Stem
from hashlib import blake2b
import os


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
    def get_leaf(num: int) -> int:
        """Retrieves the last digit of a number as the leaf

        :param num: Number to be evaluated
        :return: Last digit of num
        """
        return num % 10

    @staticmethod
    def get_stem(num: int) -> List[int]:
        """Returns a list containing all digits of a number except the last one as the stem.
        If `num` only contains one digit, it returns an empty list

        :param num: Number to be evaluated
        :return: List containing digits of num except for the last one
        """
        stem = []
        num_of_digits = get_num_of_digits(num)

        for i in range(num_of_digits - 1, 0, -1):
            stem.append(get_digit(num, i))

        return stem

    def generate_hash(self, stem: List[int], stem_lookup_path: str = "data/stem_lookup.txt") -> Stem:       
        # generate salt 
        salt = os.urandom(blake2b.SALT_SIZE)

        # generate hash
        h = blake2b(bytearray(stem), salt=salt)
        hash_str = h.hexdigest()

        stem_entry = Stem(data=stem, hash=hash_str, salt=salt)
        # write to file
        with open(file=stem_lookup_path, encoding="utf8", mode="a+") as stem_lookup_file:           
            stem_lookup_file.write(str(stem_entry))
            stem_lookup_file.write('\n')
            print(f'Hashed and wrote {stem_entry.data} to {stem_lookup_path}')

        return stem_entry 

    def print_diagram(self):
        """Prints a graphical representation of this stem-and-leaf diagram

        :return:
        """
        self.sort_data()

        # organise numbers by stems and leaves
        for num in self.__data:
            print(get_digit(num))
