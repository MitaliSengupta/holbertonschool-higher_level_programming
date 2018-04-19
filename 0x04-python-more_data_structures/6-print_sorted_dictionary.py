#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for val in sorted(a_dictionary.keys()):
        print("{}: {}".format(val, a_dictionary[val]))
