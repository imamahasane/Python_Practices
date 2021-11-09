class Vehicle:
    """Base class for all vehicles"""
    
    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        
    def drive(self):
        print("Driving", self.manufacturer, self.name)
        
    def turn(self, direction):
        print("Turning", self.name, "to", direction)
        
    def brake(self):
        print(self.name, "is stopping!")
        
if __name__ == "__main__":
    v1 = Vehicle("Fusion 1170 EX", "Walton", "Black")
    v2 = Vehicle("Unick 791 pro", "Zxprobd", "Blue")
    v3 = Vehicle("Mustang 7.0 GT", "Ford", "Red")
    
    v1.drive()
    v2.drive()
    v3.drive()
    
    v1.turn("left")
    v2.turn("right")
    v3.turn("left")
    
    v1.brake()
    v2.brake()
    v3.brake()