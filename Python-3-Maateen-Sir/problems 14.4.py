# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 23:00:06 2020

@author: emama
"""

def is_prime(n):
    if n <= 1:
        raise ValueError("The number must be greater or equal then 1.")
        
    elif n <= 3:
        return True
    
    elif (n % 2) == 0 or (n % 3) == 0:
        return False
    
    else:
        i = 5
        while(i * i) <= n:
            if (n % i) == 0 or (n % i+2) == 0:
                return
            i += 1
            
    return True

number = int(input("Please enter your input: "))

if is_prime(number):
    print(number, "is a prime number")

else:
    print(number, "is a composite number")
    