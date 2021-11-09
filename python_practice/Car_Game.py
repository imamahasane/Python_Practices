# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:15:37 2019

@author: Imam Ahasan
"""

class CarGame:
    def __init__(self, n, m, c, y, cc):
        self.name = n
        self.manufacturer = m
        self.color = c
        self.year = y
        self.cc = cc
        
    def start(self):
        print("Brand Name: ",self.name)
        print("Manufacturer:",self.manufacturer)
        print("Color:", self.color)
        print("Year:", self.year)
        print("CC :: ",self.cc)
        print("Starting The Engine")
        
    def brake(self):
        print("This system brake is always redy.")
        
    def drive(self):
        print("This system is alltime 100% ok for driving.")
        
    def turn(self):
        print("This system is allredy ok for write and left turn.")
        
    def charge_gear(self):
        print("If to be think the driver Gear Change.So ok try correct way.")
        
my_game = CarGame("Lamborghini", " luxury sports cars", "White", 2018, 6498)
my_game.start()
my_game.brake()
my_game.drive()
my_game.turn()
my_game.charge_gear()
