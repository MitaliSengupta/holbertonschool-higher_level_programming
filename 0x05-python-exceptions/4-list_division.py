#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    a = 0
    new = [0 for a in range(list_length)]
    while a < list_length:
        try:
            new[a] = my_list_1[a] / my_list_2[a]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            a += 1
    return (new)
