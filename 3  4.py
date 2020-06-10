import math

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

    def distanceFromPoint(self, otherP):
        dx = (otherP.getX() - self.x)
        dy = (otherP.getY() - self.y)
        return math.sqrt(dy**2 + dx**2)
    def slope_from_origin(self):
        if self.x == 0:
           return None
        else:
           return self.y / self.x
    def get_line_to(self,q):
        self.x =q.self.x - self.x
        self.y = q.self.y - self.y
p = Point(3, 3)
q = Point(6, 7)
print(p.slope_from_origin())
print(p.get_line_to(q))
