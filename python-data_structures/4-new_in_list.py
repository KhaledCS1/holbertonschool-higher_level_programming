#!/usr/bin/python3

# File: 3-print_reversed_list_integer.py

def new_in_list(my_list, idx, element):

    new_list = my_list[:]

    if idx < 0 or idx >= len(my_list):
        return new_list

    new_list[idx] = element

    return new_list
