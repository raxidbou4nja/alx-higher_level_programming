#!/usr/bin/python3
def print_last_digit(number):
    last_digit = int(number % 10)
    print("{}".format(last_digit), end='')
    return last_digit
