#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return []

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    squared_matrix = []

    for i in range(num_rows):
        squared_row = []
        for j in range(num_cols):
            squared_value = matrix[i][j] ** 2
            squared_row.append(squared_value)
        squared_matrix.append(squared_row)

    return squared_matrix
