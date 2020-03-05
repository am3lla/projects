#!/usr/bin/env python3

def average(a, b = 10):
    print(f"Inside average function, a is {a} and b is {b}")
    return (a + b) / 2

print(f"{average(10, 10)}") 
print(f"{average(a = 3)}") 
print(f"{average(a = 7, b = 7)}") 
print(f"{average(b = 3, a = 4)}")
