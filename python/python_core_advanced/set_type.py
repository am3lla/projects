#!/usr/bin/env python

s = {10,20,30,"XYZ"}
print(f"{ s= } { type(s)= }")

s.update([88,99])
print(f"{ s= } { type(s)= }")

s.remove(30)
print(f" { s= } ")

print(f"{ len(s)= }")

f = frozenset(s)
print(f"{ f= } { type(f)= }")

#f.update([15,25,35])
#f.remove(10)

