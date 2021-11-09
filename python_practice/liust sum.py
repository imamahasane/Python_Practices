# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 03:55:28 2019

@author: Imam Ahasan
"""

"""
#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    #

if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

"""
def list_sum(l):
    if not l:
        return None
    return sum(l)

if __name__ == "__main__":
    n = int(input())
    l = map(int, input().split())
    
    print(list_sum(l))
