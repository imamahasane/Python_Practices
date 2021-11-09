"""
The following function uses an 'if' statement. Note that the indention marks
the scope of the 'if', 'elif', 'else' actions.
def area(type_, x):
        Computes the area of a square or circle. 
        type_ must be the string "circle or the string "square" 
        We use type_ here, because type is a Python keyword. 
    if type_ == "circle":
        area = 3.14*x**2
        print(area)
    elif type_ == "square":
        area = x**2
        print(area)
    else:
        print("I don't know that one.")
       
"""

def area(type_, x):

    if type_ == "circle":
        area = 3.14*x**2
        print(area)
    elif type_ == "square":
        area = x**2
        print(area)
    else:
        print("I don't know that one.")
        
    return area

#if __name__ == "__main__":
#    a = input("Please choose your type: ")
#    b = int(input("Please inter any integer number: "))
#    area(a, b)
a = input("Please choose your type: ")
b = int(input("Please inter any integer number: "))
area(a, b)