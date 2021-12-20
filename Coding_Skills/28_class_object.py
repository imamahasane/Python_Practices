# Object of Class
    # 1. Properties
    # 2. Methods

class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == "tennis player":
            print(f"{self.name} plays tennis")

        elif self.occupation == "actor":
            print(f"{self.name} shoots a film")

    def speaks(self):
        print(f"{self.name} says how are you?")


class_object = Human("Imam", "tennis player")
class_object.do_work()
class_object.speaks()
    
class_object = Human("Samiul", "actor")
class_object.do_work()
class_object.speaks()
