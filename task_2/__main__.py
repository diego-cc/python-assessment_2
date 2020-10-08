"""
Project: python-assessment_2
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 08/10/2020 9:55 am
File: __main__.py
"""
from utils import parse_data
from steam_and_leaf import SteamAndLeaf

parsed_data = parse_data("data/sample_data.txt")
sl = SteamAndLeaf(parsed_data)

sl.sort_data()
print(sl.data)
print(sl.data[30])
print(SteamAndLeaf.get_stem(sl.data[30]))
print(SteamAndLeaf.get_leaf(sl.data[30]))
