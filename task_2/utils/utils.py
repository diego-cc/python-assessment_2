"""
Project: task_2
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 21/10/2020 7:21 pm
File: utils.py
"""
import math
from typing import List


def parse_data(path: str) -> List[int]:
    """Parses a data file containing numbers (separated by single spaces) into a list.
    Multiple lines are allowed.

    :param path: Path of the file containing data
    :return: List of numbers extracted from the data file
    :raises OSError: If the file cannot be opened or read
    :raises ValueError: If the data cannot be parsed into a list of integers
    """
    try:
        raw_data = open(file=path, mode="r", encoding="utf8", newline="")
        lines = raw_data.readlines()
        parsed_data: List[int] = []

        for line in lines:
            nums = line.split(" ")

            try:
                for num in nums:
                    parsed_data.append(int(num))
            except ValueError as err:
                print("Could not parse data from file\n")
                raise err

        return parsed_data
    except OSError as err:
        print("Could not open data file\n")
        raise err


def get_num_of_digits(num: int) -> int:
    """Calculates the number of digits of `num`

    :param num: Number to be evaluated
    :return: Number of digits of num
    """
    if num > 0:
        num_of_digits = int(math.log10(num)) + 1
    elif num == 0:
        num_of_digits = 1
    else:
        num_of_digits = int(math.log10(-num)) + 2

    return num_of_digits


def get_digit(num: int, pos: int = 0) -> int:
    """Retrieves a digit of `num` at position `pos`

    :param num:
    :param pos:
    :return:
    """
    return num // 10 ** pos % 10


def remove_duplicates(list_with_duplicates: List[int]) -> List[int]:
    """Removes duplicate entries in a list

    :param list_with_duplicates: Original list
    :returns: A new list based on the original one without duplicates
    """
    uniques = []

    for num in list_with_duplicates:
        if num not in uniques:
            uniques.append(num)

    return uniques
