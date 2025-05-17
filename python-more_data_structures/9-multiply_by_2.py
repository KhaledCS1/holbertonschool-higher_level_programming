#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for i in a_dictionary:
        value = a_dictionary[i]
        value_1 = value * 2
        new_dictionary[i] = value_1
    return new_dictionary
