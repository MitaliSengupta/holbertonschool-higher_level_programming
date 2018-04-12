#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)
    a, b = int(argv[1]), int(argv[3])
    operator = argv[2]
    math = {"+": add, "-": sub, "x": mul, "/": div}
    if operator not in math:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, operator, b, math[operator](a, b)))
