#!/usr/bin/env python

print()
print("Hello"*3)
print("All the power is with in you")
print("All the power \n is with in you")

a,b = 10,20
print(a, b)
print(f"{a=} {b=}")
print(a, b, sep="&")
print(a, b, sep="++++")

name, marks = "John", 94.5
print("Name is", name, "Marks are", marks)
print(f"Name is {name} Marks are {marks}")
print("Name is %s, Marks are %f"%(name, marks))
print("Name is %s, Marks are %.2f"%(name, marks))
print("Name is {}, Marks are {}".format(name, marks))
print("Name is {0}, Marks are {1}".format(name, marks))
print("Name is {1}, Marks are {0}".format(name, marks))
