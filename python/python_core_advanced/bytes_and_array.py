#! /usr/bin/env python

lst = [20,30,40,234]
print(f" {lst= } { type(lst)= }")

b = bytes(lst)
print(f" { b= } { type(b)= }")

b1 = bytearray(lst)
print(f" { b1= } { type(b1)= }")
