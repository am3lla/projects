#/usr/bin/env python

n = int( input( "Enter a number to generate a Multiplication Table: ") )

for i in range(1, 11):
    print(f"{n} x {i:>2} = {n*i:>2}")
