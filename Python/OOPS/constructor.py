class Car:
    def __init__(self,brand, year):
        self.brand=brand
        self.year=year

    def display(self):
        print(f"Brand : {self.brand}, Year:{self.year}")

my_car=Car("Toyota","1990")
my_car.display()

my_car2=Car("Maruti" ,"1890")
my_car2.display()

