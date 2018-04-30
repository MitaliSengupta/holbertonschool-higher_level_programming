#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    a = 0
    for b in range(x):
        try:
            print("{:d}".format(my_list[b]), end="")
            a += 1
        except (ValueError, TypeError):
            b += 1
            continue
    print("")
    return (a)
