from math import sqrt, acos, sin, cos, pi


def arcPos(datapt):
    '''
    x-axis is right, y-axis is up.
    hdg is the angle in rad from the x-axis that the reference line is travelling in.
    I'm assuming positive hdg goes anticlockwise from x-axis
    :param datapt: list of x y coordinates [(1, 2), (3, 4), (5, 6), (7, 8)]
    :return: [((startx, starty), (endx, endy), heading), ...]
    '''

    # tuples of ((startx, starty), (endx, endy), heading)
    arcPosArr = []

    # curve everything except the last point
    for i in range(len(datapt) - 1):
        arcPosArr.append(calcData(datapt[i - 1], datapt[i], datapt[i + 1]))

    # curve last point
    arcPosArr.append(calcData(datapt[-2], datapt[-1], datapt[0]))

    return arcPosArr


def getLen(coord1, coord2):
    # Calculates the distance between two points
    x1, y1 = coord1
    x2, y2 = coord2
    return sqrt(abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2)


def calcData(prev, cur, next):
    '''
    calculates arc position data
    :param prev: previous coordinate
    :param cur: current coord
    :param next: next coord
    :return: ((startx, starty), (endx, endy), heading)
    '''
    lenBef = getLen(prev, cur)
    lenAft = getLen(cur, next)

    minLen = min(lenBef, lenAft) / 2

    x1, y1 = prev
    x2, y2 = cur
    x3, y3 = next

    # line vector between previous and current points
    lineBef = [x2 - x1, y2 - y1]
    # line vector between previous and current points
    lineAft = [x3 - x2, y3 - y2]

    # normalise to unit vector
    lineBef[0] = lineBef[0] / lenBef
    lineBef[1] = lineBef[1] / lenBef
    lineAft[0] = lineAft[0] / lenAft
    lineAft[1] = lineAft[1] / lenAft

    if lineBef[1] < 0:
        heading = acos(lineBef[0] * -1)
        heading += pi
    else:
        heading = acos(lineBef[0])

    startx = cur[0] + cos(heading - pi) * minLen
    starty = cur[1] + sin(heading - pi) * minLen
    endx = cur[0] + lineAft[0] * minLen
    endy = cur[1] + lineAft[1] * minLen

    return (startx, starty), (endx, endy), heading


if __name__ == '__main__':
    data = [(0, 0), (-1, 2), (5, 6), (7, 3)]
    result = arcPos(data)
    print(result)
