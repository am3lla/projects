#!/usr/bin/env python3

class ObjectCounter:

    number_of_instances = 0

    def __init__(self):
        ObjectCounter.number_of_instances += 1
    
    @staticmethod
    def display_count():
        print(f"Current number of instances:: {ObjectCounter.number_of_instances}")

oc1 = ObjectCounter()
oc2 = ObjectCounter()

ObjectCounter.display_count()

oc3 = ObjectCounter()

ObjectCounter.display_count()
