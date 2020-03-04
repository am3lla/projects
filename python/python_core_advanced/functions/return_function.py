#!/usr/bin/env python

def display():
    def message():
        return "Hello"
    return message

message = display()
print(f"{message()} again!")
