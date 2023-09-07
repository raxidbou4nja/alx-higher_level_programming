#!/usr/bin/python3
import hidden_4 as hidden

def main():
    module_attributes = dir(hidden)

    for attribute in module_attributes:
        if not attribute.startswith('_'):
            print(attribute)

if __name__ == "__main__":
    main()
