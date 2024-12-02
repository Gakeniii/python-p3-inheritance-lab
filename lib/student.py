#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []
    
    def learn(self, added_know):
        self.knowledge.append(added_know)

student = Student("jfdj", "djfhiu")
student.learn("EUGH, EEUUGGHH!!")

print(student.knowledge)