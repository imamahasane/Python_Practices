class Teacher:
    def teachers_action(self):
        print("I can teach")


class Engineer:
    def Engineers_action(self):
        print("I can code")


class Youtuber:
    def youtubers_action(self):
        print("I can code and teach")


class Person(Teacher, Engineer, Youtuber):
    def out(self):
        self.teachers_action()
        self.Engineers_action()
        self.youtubers_action()


coder = Person()
coder.out()
