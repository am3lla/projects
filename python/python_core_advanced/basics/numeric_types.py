#!/usr/bin/env python

a, b, c = 13, 100, 66
print(f"{a} {b} {c}")
print(type(a))

a, b, c = 33.5, 25.8, 205.0
print(f"{a} {b} {c}")
print(type(a))

d = 3 + 5j
print(d)
print(type(d))

e = 0B1010
print(e)
print(type(e))

f = 0XFF
print(f)
print(type(f))

o = 0O10
print(o)
print(type(o))

g = True
print(g)
print(type(g))

print(f"value is {a}, {int(a)=}")

h = "22.5"
print(f"{h=} {float(h)=}")

i = 10
print(f"{i=} {bin(i)=} {hex(i)=} {oct(i)=}")
