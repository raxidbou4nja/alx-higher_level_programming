#!/usr/bin/python3
def lookup(obj):
    att_and_methods = dir(obj)
    filtered = [item for item in att_and_methods if not item.startswith('_')]
    return (filtered)
