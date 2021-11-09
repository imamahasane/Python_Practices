# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 20:16:07 2020

@author: emama
"""

class SuperCalculator:
    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def mul(self, a, b):
        return a * b
    
    def div(self, a, b):
        try:
            return a / b
        
        except ZeroDivisionError:
            return "vai thik kra valu din."
    
    def squ(self, a):
        return a * a
    
    def que(self, a):
        return a * a * a
    
my_cal = SuperCalculator()

temp = my_cal.add(45, 40)
print(temp)

temp = my_cal.sub(45, 40)
print(temp)

temp = my_cal.mul(45, 40)
print(temp)

temp = my_cal.div(45, 40)
print(temp)

temp = my_cal.div(45, 0)
print(temp)

temp = my_cal.squ(45)
print(temp)

temp = my_cal.que(45)
print(temp)