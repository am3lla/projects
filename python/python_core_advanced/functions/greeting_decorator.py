#!/usr/bin/env python3

def greeting_decorator(function):
    def inner(n):
        return f"Hello {function(n)}!, how are you?"
    return inner

@greeting_decorator
def hello(name):
    return name

print(hello("Andreas"))
