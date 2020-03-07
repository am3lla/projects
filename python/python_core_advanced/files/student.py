class Student:

    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score

    def display(self):
        print(f"Student:: id: {self.id}, name: {self.name}, score: {self.score}")
