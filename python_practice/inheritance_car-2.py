class Vehicle:
    """Base class for all vehicle"""
    
    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        
    def drive(self):
        print("Driving", self.manufacturer, self.name)
        
    def tuen(self, direction):
        print("Turning", self.name, "to", direction)
        
    def brake(self):
        print(self.name, "is stopping")
        
class Car(Vehicle):
    """Car Class"""
    
    def __init__(self, name, manufacturer, color, year):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = 2019
        self.wheels = 4
        
        print("A new car has been created. Name:",self.name)
        print("It has", self.wheels, "wheels")
        print("The car was built in", self.year)
        
    def change_gear(self, gear_name):
        """Method of changing gear"""
            
        print(self.name, "is chinging geat to", gear_name)
        
if __name__ == "__main__":
    c = Car("Mustang 5.9 GTX", "Ford", "red", 2019)
        