#!/usr/bin/python3
for c in range(ord("A"), ord("Z") + 1):
    if chr(c).lower() is not "e" and chr(c).lower() is not "p":
        print("{}".format(chr(c).lower()), end="")
