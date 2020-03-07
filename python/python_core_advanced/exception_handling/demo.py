#!/usr/bin/env python3

import logging

logging.basicConfig(filename = "demo.log", level = logging.DEBUG)

try:
    f = open("my_file.txt", "w")
    a, b = [int(x) for x in input("Enter two numbers separated by space: ").split()]
    logging.debug("Division in progress")
    c = a / b
    #print(f"{a} / {b} is {c}")
    f.write(f"{a} / {b} is {c}") 
except ZeroDivisionError:
    print("Divison by zero not allowed")
    print("Use a non zero number")
    logging.error("Division by zero")
else:
    print("You have entered a non zero number")
finally:
    f.close()
    print("File closed")

print("Code after dividing")
