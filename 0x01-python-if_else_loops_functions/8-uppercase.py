#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(ord("a"), ord("z")):
            print("{}".format(chr(ord(i) - 32)), end="")
        else:
            print("{}".format(i), end="")