#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    print("{} + {} = {c}".format(a, b, c=add(a, b)))
    print("{} - {} = {c}".format(a, b, c=sub(a, b)))
    print("{} * {} = {c}".format(a, b, c=mul(a, b)))
    print("{} / {} = {c}".format(a, b, c=div(a, b)))
