# Benefits of Inheritance
# 1. Code Reuse 
# 2. xtensibility 
# 3. Readability 

class Father:
    def skills(self):
        print("Programming, gardening")

class Mother:
    def skills(self):
        print("art, Cooking.")


class Child(Father, Mother):
    def __init__(self):
        pass

    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Sport.")


a = Child()
a.skills()
