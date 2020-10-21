"""
Project: task_2
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 21/10/2020 7:18 pm
File: stem.py
"""
from typing import List


class Stem:
    def __init__(self, data: List[int], hash: str, salt: bytes):
        self.__data = data
        self.__hash = hash
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
