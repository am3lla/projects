#!/usr/bin/env python3

import pickle, student

file_name = "student.dat"

#opens student.dat for binary reading
f = open(file_name, "rb")
obj = pickle.load(f)
obj.display()
