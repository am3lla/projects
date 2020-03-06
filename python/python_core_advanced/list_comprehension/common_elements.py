#!/usr/bin/env python3

a = [2, 4, 6, 8]
b = [1, 2, 3, 4]

c = []

for n in a:
    if n in b:
        c.append(n)

print(c)

d = [n for n in a if n in b]

print(d)
