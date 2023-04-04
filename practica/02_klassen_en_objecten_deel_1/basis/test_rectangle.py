from rectangle_objects import Rectangle, Box, Triangle

rectangle = Rectangle(4,5)

print(rectangle.getArea())


rectangle2 = Rectangle(10, 12, 'red')

print(rectangle2.getColor())

box = Box(4,4,2)

box.getArea()

print(box.getArea())

box.color = 'green'

box2 = Box(3,3,3)
box2.getAreaBox()
print('oppervlakte', box.getAreaBox())

print(box.color)
print(box.getColor())

tri = Triangle(3,3,3)
tri.getArea()
print(tri.getArea())