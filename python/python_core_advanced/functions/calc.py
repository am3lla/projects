#!/usr/bin/env python3

def calc(a,b):
    w = a + b  
    x = a - b
    y = a * b 
    z = a / b
    return w, x, y, z

calculation_result_tuple = calc(10, 5)

print(f"{calculation_result_tuple}")

for calculation in calculation_result_tuple:
    print(calculation)
