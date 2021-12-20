# Benefits of Inheritance
# 1. Code Reuse 
# 2. xtensibility 
# 3. Readability 

class Vehicle:
    def general_usage(self):
        print("general use: transporation")

class Car(Vehicle):
    def __init__(self):
        print("I am Car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        self.general_usage()
        print("specific use: commute to work, vacation with family")

class MotorCycle(Vehicle):
    def __init__(self):
        print("I am Motor Cycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()
        print("specific use: road trip, racing")

a = Car()
a.specific_usage()

b = MotorCycle()
b.specific_usage()


    