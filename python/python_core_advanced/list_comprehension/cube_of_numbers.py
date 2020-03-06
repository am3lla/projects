#!/usr/bin/env python3

lst = []

for i in range(1, 11):
    lst.append(i**3)

print(lst)

list_of_cubes = [x**3 for x in range(1, 11)]

print(list_of_cubes)
