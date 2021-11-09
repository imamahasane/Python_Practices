# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:52:40 2019

@author: ASUS
"""

newEngland = [["Massachusetts",6692824],["Connecticut",3596080],
              ["Maine",1328302],["New Hampshire",1323459],
              ["Rhode Island",1051511],["Vermont",626630]]
              
def report2(state_data):
    print("Population          State")
    for i in range(0,len(state_data)):
        print(state_data[i][1], "        ", state_data[i][0])
        
report2(newEngland)