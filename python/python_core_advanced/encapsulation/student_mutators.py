#!/usr/bin/env python3

class Student:
    
    def set_id(self, id):
        self.id = id
    def get_id(self):
        return self.id
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name

s = Student()
s.set_id(123)
s.set_name("John")

print(f"Student details:: id: {s.get_id()}, name: {s.get_name()}")

class Patient:
    def set_id(self, id):
        self.id = id
    def get_id(self):
        return self.id
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def set_ssn(self, ssn):
        self.ssn = ssn
    def get_ssn(self):
        return self.ssn

p = Patient()
p.set_id(1)
p.set_name("John")
p.set_ssn("AB-10040-99")

print(f"Patient details:: id: {p.get_id()}, name: {p.get_name()}, ssn: {p.get_ssn()}")
