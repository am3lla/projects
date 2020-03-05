#!/usr/bin/env python3

lst = [3, 5, 6, 9, 12, 15, 18]

print(f"list: {lst}")

for i in lst:
    if 5 == i:
        break
    print(i)

lst = [3, 6, 9, 5, 12, 15, 18]

print(f"list: {lst}")

for i in lst:
    if 5 == i:
        break
    print(i)
