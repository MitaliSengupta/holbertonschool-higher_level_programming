#!/usr/bin/python3.4
if __name__ == "__main__":
    from hidden_4 import *
    for s in dir():
        if s[:2] != "__":
            print("{}".format(s))
