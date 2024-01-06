#!/usr/bin/python3
""" Finds Peak values """

def find_peak(list_of_integers):
    """Find the peak in a list of integers."""
    list_length = len(list_of_integers)
    
    if list_length == 0:
        return None
    
    peak_index = binary_search(list_of_integers, 0, list_length - 1)
    
    return list_of_integers[peak_index]

def binary_search(arr, low, high):
    """Recursive binary search to find the peak."""
    if low == high:
        return low
    
    mid = (high - low) // 2 + low
    
    if arr[mid] > arr[mid + 1]:
        return binary_search(arr, low, mid)
    else:
        return binary_search(arr, mid + 1, high)
