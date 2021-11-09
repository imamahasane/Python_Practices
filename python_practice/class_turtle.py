# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:16:08 2019

@author: Imam Ahasan
"""

import turtle

tom = turtle.Turtle()

tom.circle(100)
print(tom)

print(type(tom))

nonte = turtle.Turtle()
fonte = turtle.Turtle()

nonte.shape("circle")
fonte.shape("square")

nonte.left(30)
nonte.forward(100)
fonte.backward(50)
