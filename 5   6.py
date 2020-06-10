class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def __str__(self):
        return str(self.x) + "," + str(self.y)
    def find_circle(p1,p2,p3):
        h1 = find_PBi(p1,p2)
        h2 = find_PBi(p2,p3)
        c=find_intersect(h1,h2)
        return (c,c.distanceFromPoint(h1))

p = Point(7, 6)
print(p)
p.move(5, 10)
print(p)
