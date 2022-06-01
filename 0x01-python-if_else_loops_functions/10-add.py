#!/usr/bin/python3
def add(a, b):
    if a < 0 and a > b:
        return (b - a)
    elif b < 0 and b > a:
        return (a - b)
    else:
        return (a + b)
