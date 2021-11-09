# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 03:52:46 2020

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
        
my_cal = Calculator()

temp = my_cal.addition(12, 78)
print(temp)

temp = my_cal.subtraction(50, 23)
print(temp)

temp = my_cal.multiplication(9, 19)
print(temp)

temp = my_cal.division(400, 5)
print(temp)

temp = my_cal.division(43, 0)
print(temp)
