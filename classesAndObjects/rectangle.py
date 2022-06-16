#Class to create rectangle objects

from point import Point

class Rectangle:
    def __init__(self,posn,w,h): #Initialize rectangle at POSN, with width W and height h
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        self.width += delta_width
        self.height += delta_height
    
    def move(self, dx, dy):
        self.corner.x += dx
        self.corner.y += dy
    
    def area(self):
        return self.width*self.height
    
    def perimeter(self):
        return (self.width+self.height)*2
    
    def flip(self):
        w = self.width
        h = self.height
        self.width = h
        self.height = w

box = Rectangle(Point(0,0),100,200)
bomb = Rectangle(Point(100,80),5,10)
print("box: ",box)
print("bomb: ",bomb)

r = Rectangle(Point(0,0),10,5)
print(r.area())


