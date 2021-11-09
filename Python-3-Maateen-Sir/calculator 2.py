# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 04:15:07 2020

@author: emama
"""

class Calculator:
    """Do addition, subtraction, multiplication and division."""
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def addition(self):
        return self.a + self.b
    
    def subtraction(self):
        return self.a - self.b
    
    def multiplication(self):
        return self.a * self.b
    
    def division(self):
        try:
            return self.a / self.b
        
        except ZeroDivisionError:
            return "It is impossible to divide by zero."
        
my_cal = Calculator(45, 3)

temp = my_cal.addition()
print(temp)

temp = my_cal.subtraction()
print(temp)

temp = my_cal.multiplication()
print(temp)

temp = my_cal.division()
print(temp)
