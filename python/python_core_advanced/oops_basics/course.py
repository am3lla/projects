#!/usr/bin/env python3

class Course:

    def __init__(self, name, ratings):
        self.name = name
        self.ratings = ratings

    def average_rating(self):
        return sum(self.ratings)/len(self.ratings)

c1 = Course('Java essentials', [1, 2, 3, 4, 5])

print(f"Course details:: name: {c1.name}, ratings: {c1.ratings}, average_ratings: {c1.average_rating()}")

c2 = Course('Mongo for Java developers', [5, 5, 5, 5])

print(f"Course details:: name: {c2.name}, ratings: {c2.ratings}, average_ratings: {c2.average_rating()}")
