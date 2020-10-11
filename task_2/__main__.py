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

last_num_stem = sl.get_stem(sl.data[len(sl.data) - 1])

stem_entry = sl.generate_hash(stem=last_num_stem)
print(f'Stem entry:\n')
print(stem_entry)
