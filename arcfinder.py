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
def finder(start, point, end):
    """
    start is the starting point
    point is the point that is being curved at
    end is the ending point
    """
    if point[0] == start[0]:
        m1 = None
    else:
        m1 = (point[1]-start[1])/(point[0]-start[0])
    
    if end[0] == point[0]:
        m2 = None
    else:
        m2 = (end[1]-point[1])/(end[0]-point[0])

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
        length = sqrt((end[1]-start[1])**2+(end[0]-start[0])**2)
        curvature = 0
    else:
        len = sqrt((point[1]-start[1])**2+(point[0]-start[0])**2)
        radius = len/tan(angle/2)
        curvature = 1/radius
        length = radius*angle

    return (length, curvature)