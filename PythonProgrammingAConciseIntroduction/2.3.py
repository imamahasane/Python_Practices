# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:49:26 2019

@author: ASUS
"""

newEngland = [["Massachusetts",6692824],["Connecticut",3596080],
              ["Maine",1328302],["New Hampshire",1323459],
              ["Rhode Island",1051511],["Vermont",626630]]
              
def report1(state_data):
    print("Population          State")
    for state_item in state_data:
        print(state_item[1], "        ", state_item[0])
        
report1(newEngland)