
class MyClass:
    """Simple Class"""
    def __init__(self):
        pass
    
    def square(self, x):
        return x**2
    
    @classmethod()
    def cube(self, x):
        return x**3
    
if __name__ == "__main__":
    myclass = MyClass()
    
print(myclass.square(3))
print(myclass.cube(3))
print(MyClass.square(3))
print(MyClass.square(3))
    