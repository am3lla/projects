#!/usr/bin/env python

s = input()
print(s)
s = input("Enter your name: ")
print(s)
i = int(input("Enter an integer value:"))
print(f" {i=} {type(i)=}")
list = [x for x in input("Enter three numbers separated by space: ").split()]
print(list)
list2 = [x for x in input("Enter three numbers separated by comma: ").split(',')]
print(list2)
