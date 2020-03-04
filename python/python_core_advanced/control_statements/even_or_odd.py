#!/usr/bin/env python

x = int(input("Enter a number: "))

if 0 == x:
  print(f"{x} is zero")
elif 0 == x % 2:
  print(f"{x} is even")
else:
  print(f"{x} is odd")


math_grade, physics_grade, chemistry_grade = [float(mark) for mark in input("Enter math, physics and chemistry grades separated by space: ").split()]

if not (math_grade >= 35 and physics_grade >= 35 and chemistry_grade >= 35):
    print("You have failed at least one exam and wont be graded.")
else:
  average = (math_grade + physics_grade + chemistry_grade) / 3

  grade = 'A'

  if average <= 59:
    grade = 'C'
  elif average <= 69:
    grade = 'B'

  print(f"Your grade is {grade}.")
