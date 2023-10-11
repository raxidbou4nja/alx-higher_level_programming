#!/usr/bin/python3
"""
Module for pascal_triangle method.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to n rows and returns
    it as a list of lists.

    Args:
        n (int): The number of rows to generate in the
        triangle.

    Returns:
        list of lists: The Pascal's triangle as a list of
        lists of integers.
    """
    rows = [[1 for j in range(i + 1)] for i in range(n)]

    for row in range(n):
        for i in range(1, row):
            rows[row][i] = rows[row - 1][i - 1] + rows[row - 1][i]

    return rows
