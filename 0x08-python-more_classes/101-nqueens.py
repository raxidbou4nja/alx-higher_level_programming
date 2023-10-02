#!/usr/bin/python3
"""
This is the "nqueens" module.

This module solves the N-Queens puzzle, finding all possible solutions
including translations and reflections.

The algorithm uses virtual backtracking without recursion, starting to slow
down visibly for N > 8, and successfully processes up to N = 11 but may be
terminated if used for N > 11. While recursion could provide a lighter-weight
process, it's not yet apparent to the author how to retain a record of which
solutions are already derived with that method.

Attributes:
    N (int): The base number of queens, and the length of the board's side in
    piece positions.
    candidates (list): A list of successful solutions for a given number of
    columns checked.

"""

from sys import argv

# Check command-line arguments
if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)

if not argv[1].isdigit():
    print('N must be a number')
    exit(1)

N = int(argv[1])

if N < 4:
    print('N must be at least 4')
    exit(1)

def board_column_gen(board=[]):
    """
    Add a column of zeroes to the right of a board about to be tested for
    queen arrangements in that column.

    Args:
        board (list): A 2D list of integers, only as wide as needed to test
        the rightmost column for queen conflicts.

    Returns:
        list: The modified 2D list.

    """
    if len(board):
        for row in board:
            row.append(0)
    else:
        for row in range(N):
            board.append([0])
    return board

def add_queen(board, row, col):
    """
    Set a queen, represented as 1, to the coordinates given in the board.

    Args:
        board (list): A 2D list of integers, only as wide as needed to test
        the rightmost column for queen conflicts.
        row (int): The first dimension index.
        col (int): The second dimension index.

    """
    board[row][col] = 1

def new_queen_safe(board, row, col):
    """
    Check that a new queen placed in the rightmost column of the board has no
    conflicts with other queens to the left and diagonally up-left and
    down-left.

    Args:
        board (list): A 2D list of integers, only as wide as needed to test
        the rightmost column for queen conflicts.
        row (int): The first dimension index.
        col (int): The second dimension index.

    Returns:
        bool: True if no left side conflicts are found for the new queen,
        False if a conflict is found.

    """
    x = row
    y = col

    for i in range(1, N):
        if (y - i) >= 0:
            # Check up-left diagonal
            if (x - i) >= 0:
                if board[x - i][y - i]:
                    return False
            # Check left
            if board[x][y - i]:
                return False
            # Check down-left diagonal
            if (x + i) < N:
                if board[x + i][y - i]:
                    return False
    return True

def coordinate_format(candidates):
    """
    Convert a board (matrix of 1s and 0s) into a series of row/column indices
    for each queen/1.

    Args:
        candidates (list): A list of all successful solutions for the amount
        of columns last checked.

    Returns:
        list: The list of coordinates.

    """
    holberton = []
    for x, attempt in enumerate(candidates):
        holberton.append([])
        for i, row in enumerate(attempt):
            holberton[x].append([])
            for j, col in enumerate(row):
                if col:
                    holberton[x][i].append(i)
                    holberton[x][i].append(j)
    return holberton

# Initialize candidates list with the first column of 0s
candidates = []
candidates.append(board_column_gen())

# Process column by column, testing the rightmost
for col in range(N):
    # Start a new generation of the candidate list for every round of testing
    new_candidates = []
    # Test each candidate from the previous round, at the current column
    for matrix in candidates:
        # For every row in that candidate's rightmost column
        for row in range(N):
            # Check if there are any conflicts in placing a queen at those coordinates
            if new_queen_safe(matrix, row, col):
                # No conflicts, so create a "child" (copy) of that candidate
                temp = [line[:] for line in matrix]
                # Place a queen in that position
                add_queen(temp, row, col)
                # Unless you're in the last round of testing,
                if col < N - 1:
                    # Add a new column of 0s on the right for the next round
                    board_column_gen(temp)
                # Add that new candidate to this round's list of successes
                new_candidates.append(temp)
    # When finished with the round, discard the "parent" candidates
    candidates = new_candidates

# Format results to match assignment output
for item in coordinate_format(candidates):
    print(item)
