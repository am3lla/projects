#!/usr/bin/env python

n = int( input("Enter a number: ") )

is_prime = True

for i in (2, n-1):
    if 0 == n % i:
        is_prime = False
        break

print(f"is {n} a prime number {is_prime}")
