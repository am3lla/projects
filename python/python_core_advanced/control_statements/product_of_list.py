#!/usr/bin/env python3

lst = [1, 2, 3, 4, 5]

x = lst[0]

for i in lst[1:]:
    x *= i

print(f"Product is {x}")
