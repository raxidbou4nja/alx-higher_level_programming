#!/usr/bin/python3
"""
Module for matrix multiplication using NumPy.

This module provides a function to multiply two matrices using NumPy.

To use NumPy, make sure it is installed:
    pip3 install numpy==1.15.0

Functions:
    lazy_matrix_mul(m_a, m_b): Multiply two matrices using NumPy.

Exceptions:
    ValueError: Raised if the matrices are not compatible for multiplication.
"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
        m_a (numpy.ndarray): The first matrix.
        m_b (numpy.ndarray): The second matrix.

    Returns:
        numpy.ndarray: The result of matrix multiplication.

    Raises:
        ValueError: If the matrices are not compatible for multiplication.
    """
    return np.dot(m_a, m_b)
