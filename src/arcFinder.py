####### DEPRECATED ########

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

def mag(a, b):
    return sqrt((a[1]-b[1])**2+(a[0]-b[0])**2)

def orient(a, b, c):
    delta = (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    if delta > 0:
        return True
    else:
        return False

def finder(start, point, end):
    a, b, c = mag(start, point), mag(point, end), mag(start, end)
    angle = pi - acos((a**2 + b**2 - c**2) / (2 * a * b))
    curvature = tan(angle/2)/a

    if angle == 0:
        length = mag(start, end)
    else:
        length = a*angle/tan(angle/2)

    if orient(start, point, end):
        return (length, curvature)
    else:
        return (length, -curvature)
