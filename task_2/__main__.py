"""
Project: python-assessment_2
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 08/10/2020 9:55 am
File: __main__.py
"""
import sys

from steam_and_leaf import StemAndLeaf
from utils import parse_data


def init_program():
    parsed_data = parse_data("data/sample_data.txt")

    diagram = StemAndLeaf(data=parsed_data)
    sorted_data = diagram.sort_data()
    diagram.data = sorted_data

    print()
    print('This program handles hashing, searching, sorting and printing stem-and-leaf diagrams.')
    print('The data set being used is available in the data/sample_data.text file.')
    print(
        'You may add your own data set by inserting numbers separated by single spaces, as represented in the text '
        'file.')

    user_input = ''

    while user_input != 'q':
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
            diagram.print()
        elif user_input == '2':
            print('Maximise your terminal window to visualise the table below')
            diagram.print_hashes()
        elif user_input == '3':
            search_query = input('Number to search for: ')
            try:
                parsed_search_query = int(search_query)
                found_entry = diagram.search(parsed_search_query)
                if found_entry:
                    print('Entry found:')
                    print(f'Number: {"".join(map(str, found_entry.data))}')
                    print(f'Hash: {found_entry.hash}')
                else:
                    print(f'{search_query} was not found')
            except ValueError:
                print('Invalid search query. Please enter a valid number and try again.')
        else:
            print('Bye!')
            sys.exit(0)


if __name__ == "__main__":
    init_program()
