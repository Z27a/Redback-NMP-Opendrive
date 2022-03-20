from math import sqrt, tan, pi, acos

""" Tests
(0,0),(0,1),(1,1)
(0,0),(1,0),(1,1)
(0,0),(0,1),(0,2)
(0,0),(0,1),(1,2)
(0,0),(1,1),(2,2)
(1,0),(0,1),(-1,0)
(11.05572809000084,24.47213595499958), (20,20), (20,10)
"""

# points are in tuple form (x,y)

def mag(a, b):
    return sqrt((a[1]-b[1])**2+(a[0]-b[0])**2)

def grad(a, b):
    return (a[1]-b[1])/(a[0]-b[0])

def orient(a, b, c):
    delta = (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    if delta > 0:
        return True
    else:
        return False

def finder(start, point, end):
    """
    start is the starting point
    point is the point that is being curved at
    end is the ending point
    """
    a, b, c = mag(start, point), mag(point, end), mag(start, end)
    angle = pi - acos((a**2 + b**2 - c**2) / (2 * a * b))

    if angle == 0:
        length = mag(start, end)
        curvature = 0
    else:
        len = a
        radius = len/tan(angle/2)
        print(angle)
        print(radius)
        curvature = 1/radius
        length = radius*angle

    if orient(start, point, end):
        return (length, curvature)
    else:
        return (length, -curvature)
