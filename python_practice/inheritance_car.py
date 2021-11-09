class Car(Vehicle):
    """Car class"""
    
    def change_gear(self, gear_name):
        """Method for changing gear"""
        print(self.name, "is changing gear to", gear_name)
        
if __name__ == "__main__":
    c = Car("Unick 791 pro", "Zxprobd", "Blue")
    c.drive()
    c.brake()
    c.change_gear("P")