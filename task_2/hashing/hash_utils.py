"""
Project: task_2
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 22/10/2020 10:36 am
File: hash_utils.py
"""
from typing import List
from models import HashData
from hashlib import blake2b
import os


def generate_hash(stem: List[int], leaf: int, salt: bytes = None, save_to_file: bool = False,
                  hash_lookup_path: str = "data/hash_lookup.txt") -> (
        str, bytes):
    """Hashes a number based on its stem (all digits of a number except for the last one) and leaf (last digit).

    If a number contains only one digit, its stem is [0] and its leaf is the number itself.

    A salt is used to avoid collisions, which can either be passed to this function or randomly generated.

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
