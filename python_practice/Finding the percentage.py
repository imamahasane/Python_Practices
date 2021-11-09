# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:44:44 2019

@author: Imam Ahasan
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    score_list = student_marks[query_name]
    sum_score = 0
    for j in score_list:
        sum_score +=j
        
    average_percent = (sum_score) /3
    print("%.2f" %average_percent)

