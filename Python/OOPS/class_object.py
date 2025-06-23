class Animal:
    name="dog"
    def sound(self):
        print("bho bho")

#creating object 
dog=Animal()
print(dog.name)
dog.sound()

class Dog:
    species="Cannie"

    def __init__(self,name, age):
        self.name=name
        self.age= age

dog1=Dog("bella",4)
print(dog1.name)
print(dog1.species)
