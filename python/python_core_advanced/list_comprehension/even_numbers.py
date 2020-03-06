#!/usr/bin/env python3

lst = []

for n in range(1, 21):
    if not bool(1 & n):
        lst.append(n)

print(lst)

even_lst = [n for n in range(1, 21) if not bool(1 & n)]

print(even_lst)
