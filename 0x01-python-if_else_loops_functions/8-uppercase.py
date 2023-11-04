#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if len(str) - 1 == i.index():
            print("{}".format(i))
        if ord(i) in range(ord("a"), ord("z") + 1):
            print("{}".format(chr(ord(i) - 32)), end="")
        else:
            print("{}".format(i), end="")
