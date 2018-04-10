#!/usr/bin/python3
for a in reversed(range(ord("a"), ord("z") + 1)):
    if a % 2 != 0:
        a = a - 32
    print("{:c}".format(a), end="")
