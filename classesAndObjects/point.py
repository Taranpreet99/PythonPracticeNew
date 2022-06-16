class Point: 
    def __init__(self, x=0, y = 0):
        self.x = 0
        self.y = 0
    
    def distance_from_origin(self):
        return ((self.x**2) + (self.y**2))**0.5
    
    def print_point(pt):
        print("({0}, {1})".format(pt.x, pt.y))
    
    #Not a good idea to have print method, instead:
    def __str__(self):
        return "({0}, {1})".format(self.x,self.y)

    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)


p = Point(3,4) #Object of type Point
q = Point() #Second point

print(p.x, p.y, q.x, q.y)

p.distance_from_origin()
