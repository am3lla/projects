#!/usr/bin/env python3

from abc import abstractmethod, ABC

#interface: all methods are abstract 
class BMW(ABC):
   
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
    
    @abstractmethod
    def drive(self):
        pass

class ThreeSeries(BMW):
    
    def __init__(self, make, model, year, cruiseControlEnabled):
        #BMW.__init__(self, make, model, year
        super().__init__(make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled
    
    def display(self):
        print(f"cruiseControlEnabled: {self.cruiseControlEnabled}")

    def start(self):
        print("Button Start")
    
    def stop(self):
        print("Button Stop")

    def drive(self):
        print("ThreeSeries is being driven")


class FiveSeries(BMW):
    
    def __init__(self, make, model, year, pakingAssistEnabled):
        #BMW__init__(self, make, model, year)
        super().__init__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled
    
    def drive(self):
        print("FiveSeries is being friven")

ts = ThreeSeries("BMW", "328i", 2018, True)
print(f"Car details:: make: {ts.make}, model: {ts.model}, year: {ts.year}, cruiseControlEnables: {ts.cruiseControlEnabled}")

ts.start()
ts.display()
ts.stop()
