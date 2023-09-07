#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("0")
        sys.exit(0)
    
    try:
        result = sum(int(arg) for arg in sys.argv[1:])
        print("{}".format(result))
    except ValueError:
        print("Error: Some arguments are not integers.")
        sys.exit(1)
