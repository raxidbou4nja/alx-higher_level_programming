#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        number = i * 10 + j
        separator = "\n" if number == 89 else ", "
        if i != j:
            print("{:02d}".format(number), end=separator)
