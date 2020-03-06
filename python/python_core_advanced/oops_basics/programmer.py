#!/usr/bin/env python3

class Programmer:

    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_salary(self, salary):
        self.salary = salary
    
    def get_salary(self):
        return self.salary
    
    def set_technologies(self, technologies):
        self.technologies = technologies
    
    def get_technologies(self):
        return self.technologies

p1 = Programmer()
p1.set_name("John")
p1.set_salary(1000)
p1.set_technologies(["Java", "Hibernate", "Spring"])

print(f"Programmer details:: name: {p1.get_name()}, technologies: {p1.get_salary()}, salary: {p1.get_salary()}")
