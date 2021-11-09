# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:20:52 2019

@author: Imam Ahasan
"""

mark_list = []
score_list = []

if __name__ == "__main__":
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        mark_list += [[name, score]]
        
        score_list += [score]
        
    x = sorted(set(score_list))[1]
    
    for n, s in sorted(mark_list):
        if s == x:
            print(n)
    
    