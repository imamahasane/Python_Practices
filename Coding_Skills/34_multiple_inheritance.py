# Benefits of Inheritance
# 1. Code Reuse 
# 2. xtensibility 
# 3. Readability 

class Father:
    def program(self):
        print("I enjoy Computer Programming.")

class Mother:
    def cooking(self):
        print("I enjoy Cooking.")


class Child(Father, Mother):
    def __init__(self):
        pass

    def sports(self):
        print("I enjoy Sport.")


a = Child()
a.program()
a.cooking()
a.sports()
