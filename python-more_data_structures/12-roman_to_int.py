#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman_value = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result, my_value = 0, 0

    for i in reversed(roman_string):
        value = roman_value.get(i, 0)
        if value < my_value:
            result -= value
        else:
            result += value
        my_value = value
    return result
