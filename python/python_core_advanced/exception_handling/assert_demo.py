#!/usr/bin/env python3

try:

    n = int( input("Enter an even number: ") )
    assert not bool(1 & n), "You have entered an invalid input or odd number"

except AssertionError as assertionError:
    print(assertionError)

print("After the assertion")
