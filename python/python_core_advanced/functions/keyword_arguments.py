#!/usr/bin/env python

def average(a, b):
    print(f"Inside average function, a is {a} and b is {b}")
    return (a + b) / 2

print(f"{average(a=10, b=20)}")
print(f"{average(a=20, b=10)}")
print(f"{average(b=10, a=20)}")
