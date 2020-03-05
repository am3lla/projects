#!/usr/bin/env python3

def display(name):
    def message():
        return "Hello"
    return f"{message()} {name}"

print(f'{display("Andreas")}')
