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
    def __init__():
        pass
    
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

p1 = input_Point()
c1 = input_Triangle()

print(p1)
print(c1)
