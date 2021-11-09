
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 15:55:49 2019

@author: Imam Ahasan
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def getName(self):
        print("Your name is "+ self.name)
        
    def getAge(self):
        print("Your age is "+ self.age)
        
pcOpject = Person("Imam", "55")

pcOpject.getName()
pcOpject.getAge()