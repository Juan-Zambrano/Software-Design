

import math

class Point (object):
    # constructor
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y
    # get distance
    def dist (self, other):
        return math.hypot (self.x - other.x, self.y - other.y)
    # get a string representation of a Point object
    def __str__ (self):
        return '(' + str(self.x) + ", " + str(self.y) + ")"
    # test for equality
    def __eq__ (self,other):
        tol = 1.0e-16
        return ((abs (self.x - other.x) < tol) and (abs(self.y - other.y) < tol))
class Circle (object):
    # constructor
    def __init__ (self, x = 0, y = 0,radius = 1):
        self.radius = radius
        self.center = Point (x, y)
    # compute cirumference
    def circumference (self):
        return 2.0*(self.radius)*(math.pi)
    # compute area
    def area (self):
        return math.pi*(self.radius)*(self.radius)
    # determine if point is strictly inside circle
    def point_inside (self,p):
        return (self.center.dist(p) < self.radius)
    # determine if a circle is strictly inside this circle
    def circle_inside (self, c):
        distance = self.center.dist (c.center)
        return (distance + c.radius) < self.radius
    # determine if a circle c intersects this circle (non-zero area of overlap)
    def does_intersect (self, c):
        difference = abs(self.radius - c.radius)
        distance = self.center.dist(c.center)
        return (((self.radius + c.radius) > distance) and (difference < distance))
    # determine the smallest circle that circumscribes a rectangle
    # the circle goes through all the vertices of the rectangle
    def circle_circumscribes (self, r):
        x = (r.ul.x + r.lr.x) / 2
        y = (r.ul.y + r.lr.y) / 2
        self.center = Point(x, y)
        self.radius = self.center.dist(r.ul)
        return
    # string representation of a circle
    def __str__ (self):
        return str(self.center) + " : " + str(round(self.radius,2))
    # test for equality of radius
    def __eq__ (self, other):
      tol = 1.0e-16
      return ((abs(self.radius - other.radius) < tol) and (abs(self.radius - other.radius) < tol))

class Rectangle(object):
    #constructor
    def __init__(self, ul_x=0, ul_y=1, lr_x=1, lr_y=0):
        if ((ul_x < lr_x) and (ul_y > lr_y)):
            self.ul = Point(ul_x, ul_y)
            self.lr = Point(lr_x, lr_y)
        else:
            self.ul = Point(0, 1)
            self.lr = Point(1, 0)
    # determine length of Rectangle (distance along the x axis)
    def length(self):
        return abs(self.lr.x - self.ul.x)
    # determine width of Rectangle (distance along the y axis)
    def width(self):
        return abs(self.ul.y - self.lr.y)
    # determine the perimeter
    def perimeter(self):
        return (2*self.length()) + (2*self.width())
    # determine the area
    def area(self):
        return self.length()*self.width()
    # determine if a point is strictly inside the Rectangle
    def point_inside(self,p):
        check_along_x = (self.ul.x < p.x) and (p.x < self.lr.x)
        check_along_y = (self.lr.y < p.y) and (p.y < self.ul.y)
        return (check_along_x and check_along_y)
    # determine if another Rectangle is strictly inside this Rectangle
    def rectangle_inside(self, r):
        if (self.ul.x > r.ul.x) or (self.ul.y < r.ul.x):
            return False
        elif (self.lr.x < r.lr.x) or (self.ul.y < r.ul.y):
            return False
        elif (self.lr.x < r.lr.x) or (self.lr.y > r.lr.y):
            return False
        elif (self.ul.x > r.ul.x) or (self.lr.y > r.lr.y):
            return False
        else:
            return True
    # determine if two Rectangles overlap (non-zero area of overlap)
    def does_intersect(self, other):
        if (other.lr.y > self.ul.y):
            return False
        elif (other.ul.x > self.lr.x):
            return False
        elif (other.ul.y < self.lr.y):
            return False
        elif (other.lr.x < self.ul.x):
            return False
        else:
            return True
    # determine the smallest rectangle that circumscribes a circle
    # sides of the rectangle are tangents to circle c
    def rect_circumscribe(self, c):
        ul_x = c.center.x - c.radius
        ul_y = c.center.y + c.radius
        lr_x = c.center.x + c.radius
        lr_y = c.center.y - c.radius
        self.ul = Point(ul_x, ul_y)
        self.lr = Point(lr_x, lr_y)
    # give string representation of a rectangle
    def __str__(self):
        return str(self.ul) + " : " + str(self.lr)
    # determine if two rectangles have the same length and width
    def __eq__(self, other):
         tol = 1.0e-16
         return ((abs(self.width() - other.width()) < tol) and (abs(self.length() - other.length()) < tol))

def main():
  # open the file geom.txt
  with open('geom.txt','r') as in_file:
  # create Point objects P and Q
  # create two Circle objects C and D
  # create two rectangle objects G and H
    p = in_file.readline().strip().split()
    pointP = Point(float(p[0]),float(p[1]))
    q = in_file.readline().strip().split()
    pointQ = Point(float(q[0]),float(q[1]))
    c = in_file.readline().strip().split()
    pointC = Circle(float(c[0]),float(c[1]),float(c[2]))
    d = in_file.readline().strip().split()
    pointD = Circle(float(d[0]),float(d[1]),float(d[2]))
    g = in_file.readline().strip().split()
    pointG = Rectangle(float(g[0]),float(g[1]),float(g[2]),float(g[3]))
    h = in_file.readline().strip().split()
    pointH = Rectangle(float(h[0]),float(h[1]),float(h[2]),float(h[3]))
  # print the coordinates of the points P and Q
  print ("Coordinates of P:", pointP)
  print("Coordinates of Q:", pointQ)
  # find the distance between the points P and Q
  print("Distance between P and Q:", round(pointP.dist(pointQ),2))
  # print C and D
  print("Circle C:", str(pointC))
  print("Circle D:", str(pointD))
  # compute the circumference of C
  print("Circumference of C:", round(pointC.circumference(),2))
  # compute the area of D
  print("Area of D:", round(pointD.area(),2))
  # determine if P is strictly inside C
  if(pointC.point_inside(pointP)):
      print("P is inside C")
  else:
      print("P is not inside C")
  # determine if C is strictly inside D
  if(pointD.circle_inside(pointC)):
      print("C is inside D")
  else:
      print("C is not inside D")
  # determine if C and D intersect (non zero area of intersection)
  if(pointC.does_intersect(pointD)):
  	print("C does intersect D")
  else:
  	print("C does not intersect D")
  # determine if C and D are equal (have the same radius)
  if(pointC == pointD):
  	print("C is equal to D")
  else:
  	print("C is not equal to D")
  # print the two rectangles G and H
  print("Rectangle G:", str(pointG))
  print("Rectangle H:", str(pointH))
  # determine the length of G (distance along x axis)
  print("Length of G:", str(pointG.length()))
  # determine the width of H (distance along y axis)
  print("Width of H:", str(pointH.width()))
  # determine the perimeter of G
  print("Perimeter of G:", str(pointG.perimeter()))
  # determine the area of H
  print("Area of H:", str(pointH.area()))
  # determine if point P is strictly inside rectangle G
  if(pointG.point_inside(pointP)):
  	print("P is inside G")
  else:
  	print("P is not inside G")
  # determine if rectangle G is strictly inside rectangle H
  if(pointG.point_inside(pointP)):
  	print("P is inside G")
  else:
  	print("P is not inside G")
  # determine if rectangles G and H overlap (non-zero area of overlap)
  if(pointG.does_intersect(pointH)):
  	print("G overlaps H")
  else:
  	print("G does not overlap H")
  # find the smallest circle that circumscribes rectangle G
  # goes through the four vertices of the rectangle
  circle = Circle()
  circle.circle_circumscribes(pointG)
  print("Circle that circumscribes G:", str(circle))
  # find the smallest rectangle that circumscribes circle D
  # all four sides of the rectangle are tangents to the circle
  rec = Rectangle()
  rec.rect_circumscribe(pointD)
  print("Rectangle that circumscribes D:", str(rec))
  # determine if the two rectangles have the same length and width
  if(pointG == pointH):
  	print("Rectange G is equal to H")
  else:
  	print("Rectangle G is not equal to H")
  # close the file geom.txt
main()
