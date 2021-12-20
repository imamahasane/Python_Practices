class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"There ID is: {self.id} and Name is: {self.name}")


emp = Employee(1, "coder")
emp.display()

del emp.id
try:
    print(emp.id)
except Exception as e:
    print(f"Exception occurd: {e}")