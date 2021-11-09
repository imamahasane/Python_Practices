# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 05:55:58 2019

@author: Imam Ahasan
"""

if __name__ == "__main__":
    n = int(input())
    l = []
    score = []
    for i in range(n):
        name = input()
        grade = float(input())
        l += [[name, grade]]
        score += [grade]
    m = sorted(set(score))
    print(m[1])
        
    print(l)
    so = sorted(set(l))
    print(so)
    

            