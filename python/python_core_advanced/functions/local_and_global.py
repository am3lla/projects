#!/usr/bin/env python

def display():
    #this is a local variable
    y = 678
    print(y)
    x = 456
    print(x)
    print(globals()['x'])

#this is a global variable
x = 123

print(x)
display()

z = display
z()
