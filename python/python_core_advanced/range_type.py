#! /usr/bin/env python

def print_range(r):
  for i in r:
    print(i, end=" ")
  print("")

print("range from 0 to 4")
r = range(5)
print_range(r)
print("range from 1 to 5")
r = range(1,6)
print_range(r)
print("range from 1 to 15 with step 3")
r = range(1, 15, 3)
print_range(r)
