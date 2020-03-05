#!/usr/bin/env python3

def custom_generator(x, y):
    while x < y:
        yield x
        x += 1

result = custom_generator(20, 30)

for i in result:
    print(i)
