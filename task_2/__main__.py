"""
Project: python-assessment_2
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 08/10/2020 9:55 am
File: __main__.py
"""
import sys

# For some reason, PyCharm complains that the copy module is not found
# It does exist natively in Python though
# See: https://docs.python.org/3/library/copy.html
import copy

from stem_and_leaf import StemAndLeaf
from utils import parse_data


def init():
    parsed_data = parse_data("data/sample_data.txt")

    diagram = StemAndLeaf(data=parsed_data)

    print()
    print('This program handles hashing, searching, sorting and printing stem-and-leaf diagrams.')
    print('The data set being used is available in the data/sample_data.txt file.')
    print(
        'You may add your own data set by inserting numbers separated by single spaces, as represented in the text '
        'file.')

    user_input = 'Here come the inputs...'

    while user_input:
        print()
        print('Choose an option below and press Enter:')
        print('(Leave the input blank or enter anything else to quit the program)')
        print()
        print('1: Print stem-and-leaf diagram using the provided data set')
        print('2: Print all entries represented as stem, leaf and corresponding hash')
        print('3: Search for a number in the provided data set')
        print()
        user_input = input('Option chosen: ')
        print()
        if user_input == '1':
            temp_diagram = copy.deepcopy(diagram)
            temp_diagram.data = temp_diagram.sort_data()
            temp_diagram.hash_entries = temp_diagram.hash_all_entries()

            temp_diagram.print()
        elif user_input == '2':
            print('Maximise your terminal window to visualise the table below')
            diagram.print_hashes()
        elif user_input == '3':
            search_query = input('Number to search for: ')
            try:
                print()
                parsed_search_query = int(search_query)

                found_entry = diagram.search(parsed_search_query)

                if found_entry:
                    print('Entry found:')
                    print(f'Number: {found_entry.data}')
                    print(f'Hash: {found_entry.hash}')
                    print()
                else:
                    print(f'{search_query} was not found')
                    print()
            except ValueError:
                print('Invalid search query. Please enter a valid number and try again.')
        else:
            print('Bye!')
            sys.exit(0)


if __name__ == "__main__":
    init()
