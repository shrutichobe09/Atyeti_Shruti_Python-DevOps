#multilevel inheritance
class person:
    def __init__(self,name):
        self.name=name
    
    def show(self):
        print(f"My name is {self.name}")

#inherit student class from person
class student(person):
    def studying(self):
        print(f"{self.name} is studying ")

class collegestudent(student):
    collegname="dypiu"
    def attend_lecture(self):
        print(f"{self.name} is attending lecture in {collegestudent.collegname} ")

collegestudent1=collegestudent("shruti")
collegestudent1.show()
collegestudent1.studying()
collegestudent1.attend_lecture()
