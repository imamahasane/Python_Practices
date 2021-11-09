# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 11:43:26 2019

@author: ASUS
"""

#!/bin/python3

import math
import os
import random
import re
import sys

"""
tip=float(meal_cost*(tip_percent/100)) 
tax=float(meal_cost*(tax_percent/100)) 
tc=float(meal_cost+tip+tax) 
print(round(tc))
"""

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip=float(meal_cost*(tip_percent/100)) 
    tax=float(meal_cost*(tax_percent/100)) 
    print(round(float(meal_cost+tip+tax)))
if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
