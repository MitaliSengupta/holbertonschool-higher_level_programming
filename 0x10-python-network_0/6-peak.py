#!/usr/bin/python3
"""
function that finds a peak in a list of unsorted
integers
"""


def find_peak(list_of_integers):
    """
    function to find peak
    """
    l = len(list_of_integers)
    if l == 0:
        return
    half = l // 2
    if (half == l - 1 or list_of_integers[half] >=
        list_of_integers[half + 1]) and (half == 0 or list_of_integers[half] >=
                                         list_of_integers[half - 1]):
        return (list_of_integers[half])
    elif half != l - 1 and list_of_integers[half + 1] > list_of_integers[half]:
        return (find_peak(list_of_integers[half + 1:]))
    return (find_peak(list_of_integers[:half]))
