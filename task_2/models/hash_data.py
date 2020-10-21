"""
Project: task_2
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 21/10/2020 7:18 pm
File: hash_data.py
"""
from typing import List


class HashData:
    def __init__(self, data: List[int], hash_str: str, salt: bytes):
        self.__data = data
        self.__hash = hash_str
        self.__salt = salt

    @property
    def data(self):
        return self.__data

    @property
    def hash(self):
        return self.__hash

    @property
    def salt(self):
        return self.__salt

    def __str__(self):
        return f'{self.data} {self.hash} {self.salt}'
