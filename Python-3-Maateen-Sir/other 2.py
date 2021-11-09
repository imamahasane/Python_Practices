"""
Exercise:
Write a function absolutevalue(num) that computes the absolute value of
a number. You will need to use an 'if' statement. Remember if a number is 
less than zero then you must multiply by -1 to make it greater than zero.
Give output in the form:

The absolute value of -5  is  5


# Test runs
absolutevalue(5)
absolutevalue(-5)
absolutevalue(4-4)


Solution:
"""

def absolutevalue(num):
    if num < 0:
        v = num * -1
        print("The absolute value of", num, "is", v)
        
    return absolutevalue

absolutevalue(-5)


    
    
