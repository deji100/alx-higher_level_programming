#!/usr/bin/python3
for x in range(0, 100):
    if x == 99:
        print(x, end="")
    else:
        print(f"{x:02}", end=", ")
