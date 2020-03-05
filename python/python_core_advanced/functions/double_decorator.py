#!/usr/bin/env python3

def decor(function):
    def inner():
        result = function()
        return 2*result
    return inner

def num():
    return 5

resultFunction = decor(num)

print(resultFunction())

@decor
def other_num():
    return 10

print(other_num())
