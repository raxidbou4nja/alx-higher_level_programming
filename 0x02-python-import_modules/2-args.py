#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = len(sys.argv)
    if args <= 1:
        print("{} arguments.".format(args - 1))
    elif args == 2:
        print("{} argument:".format(args - 1))
    else:
        print("{} arguments:".format(args - 1))
    
    for index, argument in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(index, argument))
