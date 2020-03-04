#!/usr/bin/env python

def display(name):
    def message():
        return "Hello"
    return f"{message()} {name}"

print(f'{display("Andreas")}')
