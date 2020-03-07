#!/usr/bin/env python3

import pickle, student

file_name = "student.dat"
#opens student.dat for binary writing
f = open(file_name, "wb")
s = student.Student(101, "John", 90)
pickle.dump(s, f)
f.close()
