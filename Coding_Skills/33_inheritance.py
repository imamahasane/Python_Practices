# Benefits of Inheritance
# 1. Code Reuse 
# 2. xtensibility 
# 3. Readability 

class Animal:
    def __init__(self, habitat):
        self.habitat = habitat

    def phabitat(self):
        print(self.habitat)

    def sound(self):
        print("Some Animal Sound.")

class Dog(Animal):
    def __init__(self):
        super().__init__("Kennel")

    def sound(self):
        print("wooff woof!")

a = Dog()
a.phabitat()
a.sound()