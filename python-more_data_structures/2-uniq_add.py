#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_number = []
    total = 0
    for numbers in my_list:
        if numbers not in my_number:
            my_number.append(numbers)
            total = total + numbers
    return total
