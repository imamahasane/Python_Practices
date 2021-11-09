# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 20:27:03 2020

@author: emama
"""

class Calculator:
    """Do addition, subtraction, multiplication and division."""
    
    def addition(self, a, b):
        return a + b
    
    def subtraction(self, a, b):
        return a - b
    
    def multiplication(self, a, b):
        return a * b
    
    def division(self, a, b):
        try:
            return a / b
        
        except ZeroDivisionError:
            return "It is impossible to divide by zero."
        
class SuperCalculator(Calculator):
    def squ(self, a):
        return a * a
    
    def que(self, a):
        return a * a * a
    
my_cal = SuperCalculator()

temp = my_cal.addition(45, 40)
print(temp)

temp = my_cal.subtraction(45, 40)
print(temp)

temp = my_cal.multiplication(45, 40)
print(temp)

temp = my_cal.division(45, 40)
print(temp)

temp = my_cal.division(45, 0)
print(temp)

temp = my_cal.squ(45)
print(temp)

temp = my_cal.que(45)
print(temp)
