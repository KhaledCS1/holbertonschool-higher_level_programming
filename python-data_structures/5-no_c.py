#!/usr/bin/python3

def no_c(my_string):

    khaled = ""
    for char in my_string:
       if char not in ('c', 'C'):
            khaled = khaled + char
    return khaled
