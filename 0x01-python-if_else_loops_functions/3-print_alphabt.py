#!/usr/bin/python3
for c in range(ord("A"), ord("Z") + 1):
    if chr(c).lower() != "e" and chr(c).lower() != "q":
        print("{}".format(chr(c).lower()), end="")
