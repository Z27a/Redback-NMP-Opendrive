from math import atan, sqrt, tan, pi

""" Tests
(0,0),(0,1),(1,1)
(0,0),(1,0),(1,1)
(0,0),(0,1),(0,2)
(0,0),(0,1),(1,2)
(0,0),(1,1),(2,2)
(1,0),(0,1),(-1,0)
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
    if point[0] == start[0]:
        m1 = None
    else:
        m1 = grad(start, point)
    
    if end[0] == point[0]:
        m2 = None
    else:
        m2 = grad(end, point)

    if m1 == m2:
        angle = 0
    elif m1 == None:
        if m2 == 0:
            angle = pi/2
        else:
            angle = pi - atan(abs(1/m2))
    elif m2 == None:
        if m1 == 0:
            angle = pi/2
        else:
            angle = pi - atan(abs(1/m1))
    elif m1*m2 == -1:
        angle = pi/2
    else:
        angle = pi - atan(abs((m1-m2)/(1+m1*m2)))

    if angle == 0:
        length = mag(start, end)
        curvature = 0
    else:
        len = mag(start, point)
        radius = len/tan(angle/2)
        curvature = 1/radius
        length = radius*angle

    if orient(start, point, end):
        return (length, curvature)
    else:
        return (length, -curvature)
