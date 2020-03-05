#!/usr/bin/env python3

dict1 = {1:"john",2:"bill",3:"bob"}
print(f"{ dict1= } { type(dict1)= }")

items = dict1.items()
print(f" {items= } { type(items)= }")

for item in items:
  print(f" { item= } { type(item)= }")
  break

keys = dict1.keys()
print(f" {keys=} {type(keys)=} ")

values = dict1.values()
print(f" {values=} { type(values)= } ")

print(f"{ dict1[3]= }")

del dict1[2]
print(f"{ dict1= } { type(dict1)= }")

countries = ["Colombia","México", "India"]
countries.append("Rusia")
del countries[2]
middle = len(countries)//2
print(countries[:middle] + ["Chile"] + countries[middle:] )
