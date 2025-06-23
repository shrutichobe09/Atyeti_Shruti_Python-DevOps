#polymorphism meand many forms - it allow same method name to behave diffrently depending on object
# python support two ways :
#1. inheritance and method overriding
#2. duck typing(dynamic poymorphism)

#inheritance and method  and overriding 

class Shape:
    def draw(self):
        print("drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing circle")


class sqaure(Shape):
    def draw(self):
        print("Drawing sqauare")


class Triangle(Shape):
    def draw(self):
        print("Drawing triangle")

def render_shape(shape):
    shape.draw()

#object of different class
shapes=[Circle(),sqaure(),Triangle()]

for s in shapes:
    render_shape(s)