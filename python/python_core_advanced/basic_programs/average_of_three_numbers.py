#!/usr/bin/env python3

a, b, c = [int(x) for x in input("Enter three integer numbers: ").split()]
average = (a + b + c)/3
print(f"Average of {a=} {b=} {c=} is {average}")
