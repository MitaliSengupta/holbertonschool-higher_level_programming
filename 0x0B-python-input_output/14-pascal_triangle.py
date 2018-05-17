#!/usr/bin/python3
"""
This file defines a function
that creates a pascals triangle
"""


def pascal_triangle(n):
    """
    function defining the logic to
    create pascal's triangle
    """
    if n <= 0:
        return ([])
    if n == 1:
        return [[1]]
    pascal = [[1]]
    for i in range(n - 1):
        pascal.append([x + n for x, n in zip(pascal[-1] + [0],
                                             [0] + pascal[-1])])
    return (pascal)
