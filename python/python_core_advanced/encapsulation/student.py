#!/usr/bin/env python3

class Student:

    def __init__(self):
        self.__id = 123
        self.__name = "John"
    
    def display(self): 
        print(f"Student details:: id: {self.__id}, name: {self.__name}")

s = Student()
s.display()

print(s._Student__id)
