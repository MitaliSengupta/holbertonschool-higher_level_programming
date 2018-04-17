#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    dup = my_list[:]
    if idx >= 0 and idx < len(dup):
        dup[idx] = element
    return dup
