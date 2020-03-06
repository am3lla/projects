#!/usr/bin/env python3

a = [n for n in range(1, 6)]
b = [n for n in range(6, 11)]

c = []

for i in range(0, len(a)):
    c.append( a[i] * b[i] )

print(c)

d = [ a[n] * b[n] for n in range(len(a))]

print(d)
