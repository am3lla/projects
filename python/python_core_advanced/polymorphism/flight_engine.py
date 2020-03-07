#!/usr/bin/env python3

class Flight:
    
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()

class AirBusEngine:

    def start(self):
        print("AirBusEngine starting...")

class BoingEngine:

    def start(self):
        print("BoingEngine stating...")

abe = AirBusEngine()
be = BoingEngine()

flight1 = Flight(abe)
flight2 = Flight(be)

flight1.start()
flight2.start()
