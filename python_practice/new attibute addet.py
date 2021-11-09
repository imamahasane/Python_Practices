# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 19:44:00 2020

@author: emama
"""

class Car:
    def __init__(self, n, c):
        self.name = n
        self.color = c
        
    def start(self):
        print("Starting the engine.")
        
m_c = Car("ZxproBD", "White")
m_c.start()

m_c.year = 2908

print(m_c.name, m_c.color, m_c.year)