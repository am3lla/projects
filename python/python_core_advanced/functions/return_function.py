#!/usr/bin/env python3

def display():
    def message():
        return "Hello"
    return message

message = display()
print(f"{message()} again!")
