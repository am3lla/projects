#!/usr/bin/env python3

class Car:

    def __init__(self, make, year):
        self.make = make
        self.yeat = year
    
    class Engine:

        def __init__(self, number):
            self.number = number
        
        def start(self):
            print("Engine started")

c = Car("BMW", 2017)
e = c.Engine(100)
e.start()
