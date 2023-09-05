#!/usr/bin/python3
def uppercase(input_str):
    result_str = ""
    for char in input_str:
        if 'a' <= char <= 'z':
            result_str += chr(ord(char) - ord('a') + ord('A'))
        else:
            result_str += char

    print(result_str)
