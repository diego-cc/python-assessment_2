"""
Project: python-assessment_2
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 08/10/2020 10:34 am
File: utils.py
"""
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
