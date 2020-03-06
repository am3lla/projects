#!/usr/bin/env python3

class Student:
    
    major = "CSE"
    
    def __init__(self, role_number, name):
        self.role_number = role_number
        self.name = name

s1 = Student(1, "John")
s2 = Student(2, "Bill")

print(f"Student details:: role_number: {s1.role_number}, name: {s1.name}, major: {s1.major}")
print(f"Student details:: role_number: {s2.role_number}, name: {s2.name}, major: {s2.major}")
