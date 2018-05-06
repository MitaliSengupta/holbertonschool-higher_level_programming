#!/usr/bin/python3
"""
This module defines function to divide two list int a matrix
"""


def matrix_divided(matrix, div):
        """
        Divides list and Raises TypeError
        """
        if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
        elif div is 0:
                raise ZeroDivisionError("division by zero")
        typeErr = "matrix must be a matrix (list of lists) of integers/floats"
        sizeErr = "Each row of the matrix must have the same size"
        new = []
        if matrix is None or len(matrix) is 0 or len(matrix[0]) is 0:
                raise TypeError(typeErr)
        old = len(matrix[0])
        for count, y in enumerate(matrix):
                if not isinstance(y, list):
                        raise TypeError(typeErr)
                if len(y) != old:
                        raise TypeError(sizeErr)
                old = len(y)
                new.append(y[:])
                for a, item in enumerate(y):
                        if not isinstance(item, (int, float)):
                                raise TypeError(typeErr)
                        new[count][a] = round(item / div, 2)
        else:
                return (new)
