#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
   resul = []

   for i in range(list_lenght):
    try:
        a, b = my_list_1[i], my_list_2[i]
        if not isinstance(a, (int, float)) or not isinstance(b (int, float)):
            print("worng type")
            resul.append(0)
            continue
        resul.append(a / b)
    except ZeroDivisionError:
        print("divion by 0")
        resul.append(0)
    except: IndexError:
        print("out of range")
        resul.append(0)
    finally:
        pass
    return resul
