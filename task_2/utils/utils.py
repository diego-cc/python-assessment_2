"""
Project: task_2
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 21/10/2020 7:21 pm
File: utils.py
"""
import math
from typing import List
from models import HashData
from hashlib import blake2b
import os


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


def generate_hash(stem: List[int], leaf: int, salt: bytes = None, save_to_file: bool = False,
                  hash_lookup_path: str = "data/hash_lookup.txt") -> (
        str, bytes):
    """Hashes a number based on its stem (all digits of a number except for the last one) and leaf (last digit).
    If a number contains only one digit, its stem is [0] and its leaf is the number itself.
    A random salt is used to avoid collisions.

    The hashing algorithm used is BLAKE2b.

    :param stem: Stem of the number represented as a list of digits
    :param leaf: Last digit of a number
    :param salt: Optional salt to be used (a random one will be created if not passed)
    :param save_to_file: If set to true, the new hash / salt entry will be written to the provided `hash_lookup_path`
    :param hash_lookup_path: Path to write the hash and salt to a text file
    :return: Hash and salt generated as a tuple (respectively)

    """
    if not salt:
        # generate salt
        salt = os.urandom(blake2b.SALT_SIZE)

    # add leaf as the last element of the stem list to be hashed afterwards
    stem.append(leaf)

    # generate hash
    h = blake2b(bytearray(stem), salt=salt)
    hash_str = h.hexdigest()

    hash_entry = HashData(data=stem, hash_str=hash_str, salt=salt)

    # write to file
    if save_to_file:
        with open(file=hash_lookup_path, encoding="utf8", mode="a+") as stem_lookup_file:
            stem_lookup_file.write(str(hash_entry))
            stem_lookup_file.write('\n')
            print(f'Hashed and wrote {hash_entry.data} to {hash_lookup_path}')

    return hash_str, salt


def remove_duplicates(list_with_duplicates: List[int]) -> List[int]:
    uniques = []

    for num in list_with_duplicates:
        if num not in uniques:
            uniques.append(num)

    return uniques
