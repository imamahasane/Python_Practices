# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 21:05:06 2020

@author: emama
"""

class Calculator:
    """Do addition, subtraction, multiplication and division."""
    
    def __init__(self, a, b=25):
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
        
class SuperCalculator(Calculator):
    def __init__(self, a):
        self.a = a
    
    def squ(self, a):
        return self.a * self.a
    
    def que(self, a):
        return self.a * self.a * self.a
    
my_cal = SuperCalculator(40)

temp = my_cal.addition()
print(temp)

temp = my_cal.subtraction()
print(temp)

temp = my_cal.multiplication()
print(temp)

temp = my_cal.division()
print(temp)

temp = my_cal.division()
print(temp)

temp = my_cal.squ()
print(temp)

temp = my_cal.que()
print(temp)
