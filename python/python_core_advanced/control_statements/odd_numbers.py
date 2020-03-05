#!/usr/bin/env python3

a, b  = [int(i) for i in input("Enter min and max value: ").split()] 

x = a if bool( 1 & a) else a + 1

#x = a + 1

#if bool(a & 1):
#  x = a

while x < b:
  print(x)
  x += 2
