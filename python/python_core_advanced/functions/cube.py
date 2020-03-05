#!/usr/bin/env pyhton

def cube(x):
    return x*x*x

print(f"Cube of 2 is {cube(2)}")

cube_lambda = lambda x : x**3

print(f"Cube of 2 is {cube_lambda(2)}")
