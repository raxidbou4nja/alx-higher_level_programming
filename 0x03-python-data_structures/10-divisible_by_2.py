#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []

    for number in my_list:
        is_divisible = number % 2 == 0

        result.append(is_divisible)

    return result
