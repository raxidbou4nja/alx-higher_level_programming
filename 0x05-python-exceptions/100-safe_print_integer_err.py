#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    try:
        integer_value = int(value)
        print("{:d}".format(integer_value))
        return True
    except ValueError as err:
        print("Exception: {}".format(err), file=stderr)
        return False
