#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(ord("a"), ord("z") + 1):
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
