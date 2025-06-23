class Duck:
    def qauck(self):
        print("Quack!")

class person:
    def qauck(self):
        print("i am imitating duck")

def make_it_quack(thing):
    thing.qauck()

d= Duck()
p=person()

make_it_quack(d)
make_it_quack(p)


#another example of duck typing
def add(a,b):
    return a+b
    
print(add(5,7))
print(add("a","b"))
print(add("shruti","chobe"))
print(add([1,2,3],[8,7,6]))
