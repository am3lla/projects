#!/usr/bin/env python

import sys

args = sys.argv

print(f"Program name: {args[0]}")

print(f"Number of arguments: {len(args)}")

print(f"Argmuments: ", end = ' ')

for arg in args:
    print(arg, end = ' ')

print()
