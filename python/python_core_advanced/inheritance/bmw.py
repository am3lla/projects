#!/usr/bin/env python3

class BMW:
   
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Starting the car")

    def stop(self):
        print("Stopping the car")

class ThreeSeries(BMW):
    
    def __init__(self, make, model, year, cruiseControlEnabled):
        #BMW.__init__(self, make, model, year
        super().__init__(make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled
    
    def display(self):
        print(f"cruiseControlEnabled: {self.cruiseControlEnabled}")

    def start(self):
        super().start()
        print("Button Start")


class FiveSeries(BMW):
    
    def __init__(self, make, model, year, pakingAssistEnabled):
        #BMW__init__(self, make, model, year)
        super().__init__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled

ts = ThreeSeries("BMW", "328i", 2018, True)
print(f"Car details:: make: {ts.make}, model: {ts.model}, year: {ts.year}, cruiseControlEnables: {ts.cruiseControlEnabled}")

ts.start()
ts.display()
ts.stop()
