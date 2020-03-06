#!/usr/bin/env python3

class Product:
    
    def __init__(self):
        self.name = 'iphone'
        self.description = 'It''s awesome'
        self.price = 700
    
    def display(self):
        print(f"name: {p.name}, description: {p.description}, price: {p.price}")

p = Product()

print(f"Product details:: name: {p.name}, description: {p.description}, price: {p.price}")
p.display()

q = Product()
print(f"Product details:: name: {q.name}, description: {q.description}, price: {q.price}")
q.display()
