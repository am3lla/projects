#!/usr/bin/env python3

n = int( input("Enter a number: ") )

i = 0

while i < n + 1:
    i += 1
    if 0 == i % 10:
        continue
    if 100 < i:
        break
    print(i)
