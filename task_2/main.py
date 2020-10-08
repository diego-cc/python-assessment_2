"""
Project: python-assessment_2
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 08/10/2020 9:55 am
File: main.py
"""
from task_2.utils import parse_data
from task_2.stem_and_leaf import SteamAndLeaf

parsed_data = parse_data("data/sample_data.txt")
sl = SteamAndLeaf(parsed_data)

sl.sort_data()
print(sl.data)

sl.print_diagram()
