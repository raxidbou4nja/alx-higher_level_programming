#!/usr/bin/python3
import sys

def main():
    if len(sys.argv) <= 1:
        print("0")
        return
    
    try:
        result = sum(int(arg) for arg in sys.argv[1:])
        print("{}".format(result))
    except ValueError:
        print("Error: Some arguments are not integers.")

if __name__ == "__main__":
    main()
