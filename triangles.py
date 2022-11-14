# Points contain x- and y-coordinate
# Instantiated by Point(x, y)
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return f"Point: ({self.x},{self.y})"
    
  def __str__(self):
    return f"({self.x},{self.y})"

# Triangles contain three vertex points p1, p2, p3
# Instantiate by Triangle(p1, p2, p3)
#             with three Point objects
class Triangle:
  def __init__(self, p1, p2, p3):
    self.p1 = p1
    self.p2 = p2
    self.p3 = p3
    
  def __repr__(self):
    return f"Triangle: {self.p1}, {self.p2}, {self.p3}"


def input_Point():
  raw_point = input("Input the point in the form (x,y)\n")
  raw_point = raw_point.replace('(','')
  raw_point = raw_point.replace(')','')
  raw_point = raw_point.replace(' ','')
  point = raw_point.split(',')
  return Point(float(point[0]), float(point[1]))

def input_Triangle():
  print("Input the first vertex of the triangle: ")
  p1 = input_Point()
  print("Input the second vertex of the triangle: ")
  p2 = input_Point()
  print("Input the third vertex of the triangle: ")
  p3 = input_Point()
  return Triangle(p1, p2, p3)


# New global functions
def distance(p1, p2):
  return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2) ** 0.5

def perimeter(t):
  return distance(t.p1, t.p2) + distance(t.p1, t.p3) + distance(t.p2, t.p3)

def area(t):
  l1 = distance(t.p1, t.p2)
  l2 = distance(t.p1, t.p3)
  l3 = distance(t.p2, t.p3)
  s = (l1 + l2 + l3) / 2
  return (s * (s-l1) * (s-l2) * (s-l3)) ** 0.5

def centroid(t):
  return Point((t.p1.x + t.p2.x + t.p3.x) / 3, (t.p1.y + t.p2.y + t.p3.y) / 3)


t1 = input_Triangle()

print(t1)
print("The triangle's perimeter is", perimeter(t1))
print("The triangle's area is", area(t1))
print("The triangle's centroid is", centroid(t1))