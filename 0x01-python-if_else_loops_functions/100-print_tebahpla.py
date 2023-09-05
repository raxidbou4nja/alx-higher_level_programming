#!/usr/bin/python3
for ascii_value in range(ord('Z'), ord('A') - 1, -1):
    char_to_print = chr(ascii_value)
    if ascii_value % 2 == 0:
        char_to_print = char_to_print.lower()
    print(char_to_print, end="")
