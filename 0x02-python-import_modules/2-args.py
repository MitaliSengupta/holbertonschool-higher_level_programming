#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv) - 1
    print("{:d} {:s}{:s}".format(num,
                                 "argument" if num <= 2 and num == 1
                                 else "arguments",
                                 "." if num == 0 else ":"))
    for a, s in enumerate(argv):
        if a > 0:
            print("{}: {}".format(a, s))
