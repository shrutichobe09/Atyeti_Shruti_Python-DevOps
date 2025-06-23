#encapsulation restrict access to certain part of object like variable or methods

#private variable in python 

class MyClass:
    def __init__(self):
        self.__secret = 42  # Private variable

    def get_secret(self):
        return self.__secret  # Accessed via public method

obj = MyClass()
print(obj.get_secret())  
# print(obj.__secret)    # AttributeError

