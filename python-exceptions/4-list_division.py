#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            a, b = my_list_1[i], my_list_2[i]
            if (not isinstance(a, (int, float)) or
                    not isinstance(b, (int, float))):
                print("worng type")
                result.append(0)
                continue
            result.append(a / b)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)

        finally:
            pass
    return result
