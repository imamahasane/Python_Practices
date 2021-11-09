# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 17:52:00 2019

@author: Imam Ahasan
"""

class Vehicle:
    """ Base/parent class for all vehicles """
    
    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        
    def drive(self):
        print("Driving", self.manufacturer, self.name)
        
    def turn(self, direction):
        print("Turning", self.name, "to", direction)
        
    def brake(self):
        print(self.name, "is stopping")
        

if __name__ == "__main__":
    v1 = Vehicle("Fusion 110 EX", "Walton", "Black")
    v2 = Vehicle("Softail Delux", "Harley-Davidson", "Blue")
    v3 = Vehicle("Mustang 5.0 GT Coupe", "Ford", "Red")
    
    v1.drive()
    v2.drive()
    v3.drive()
    
    v1.turn("Left")
    v2.turn("Right")
    
    v1.brake()
    v2.brake()
    v3.brake()
    
         
class Car(Vehicle):
    """ Car Class """
    def change_gear(self, gear_name):
        """ Method for changing gear """
        print(self.name, "is changing gear to", gear_name)
        
if __name__ == "__main__":
    c = Car("Mustang 5.0 GT Coupe", "Ford", "Red")
    c.drive()
    c.brake()
    c.change_gear("P")
    
    