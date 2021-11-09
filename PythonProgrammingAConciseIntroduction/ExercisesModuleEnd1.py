# - ExercisesModuleEnd1.py *- coding: utf-8 -*-
""" Find and correct all the errors in the following Python functions.
    To run one, click in the cell (between two lines) and type Ctrl-Enter for
    Windows or Command-Return for a Mac.  Then enter the name of the function
    into the IPython console.  For example, to run the first one enter
    print_phrase() and press return.
"""
""" 
Exercise 1 
"""
#%%
def print_phrase()
    phrase = "Now is the time
    print (phrase)
    
"""
def print_phrase():
    phrase = "Noew is the time"
    print(phrase)
print_phrase()

def print_phrase2():
    phrase = "Now is the time"
    return phrase
print(print_phrase2())


def print_phrase3(phrase3):
#    phrase = 
    return phrase3
m = print_phrase3("Now is the time")
print(m)
"""
#%%
""" 
Exercise 2
"""
#%%
def favorite_sport(favorite):
    sport = "favorite"
    .print("Your favorite sport is",sport)
    
"""
def favorite_sport(favorite):
    sport = "Favorite"
    print("My favorite sport is ",favorite)
favorite_sport("Cricate")


def favorite_sport(favorite):
    sport = "Favorite"
    print("My",sport,"sport is ",favorite)
favorite_sport("Cricate")
"""
#%%
""" 
Exercise 3 
"""
#%%
def username(yourname):
    prnt("Your name is",youname)
    
"""
def username(yourname):
    print("Your name is ",yourname)
username("Imam Ahasan")


def username(yourname):
    print("Your name is ",yourname)
username(yourname = input("Please enter your name: "))


def username(yourname):
    return ("Your name is ",yourname)
username(yourname = input("Please enter your name: "))
"""
#%%
"""
Exercise 4
"""
#%%
def compare_numbers(x,y):
    if x = y:
        print("they are equal")
    else
        print(x, "and", y, 'are not equal')

"""

def compare_numbers(x, y):
    if x == y:
        print("They are equal")
    else:
        print(x, "and", y, "are not equal")
compare_numbers(7,9)
"""
#%%
        """
Exercise 5
"""
#%%
def count_by_5():
    """ Count from 5 to 100 in steps of 5 """
    """ 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 """
    print 'Counting from 5 through 100 in steps of 5'
    ct = 5
    while ct < 100:
        print(ct, end = " ")
        ct = ct + 5

"""
#%%
def count_by_5():
    print("Counting from 5 through 100 in  steps of 5")
    ct = 5
    while ct < 101:
        print(ct, end=" ")
        ct += 5
    print()
count_by_5()

def count_by_5():
    print("Counting from 5 through 100 in  steps of 5")
    for ct in range(5, 101, 5):
        print(ct, end=" ")
    print()
    
count_by_5()
#%%
"""
#%%