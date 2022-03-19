from math import sqrt, acos, sin, cos, pi

def arcStart(datapt):
    # datapoints could be [(1, 2), (3, 4), (5, 6), (7, 8)]
    # need to return x, y, hdg
    # x-axis is right, y-axis is up.
    # hdg is the angle in rad from the x-axis that the reference line is travelling in. Positive hdg points towards up??

    # tuples of (x,y,hdg)
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
    lenBefore = getLen(prev, cur)
    lenAfter = getLen(cur, next)

    minLen = min(lenBefore, lenAfter) / 2

    x1, y1 = prev
    x2, y2 = cur

    # line vector
    line = [x2 - x1, y2 - y1]

    # normalise to unit vector
    line[0] = line[0] / lenBefore
    line[1] = line[1] / lenBefore

    if line[1] < 0:
        heading = acos(line[0] * -1)
        heading += pi
    else:
        heading = acos(line[0])

    midx = cur[0] + cos(heading - pi) * minLen
    midy = cur[1] + sin(heading - pi) * minLen

    return midx, midy, heading


# if __name__ == '__main__':
#     data = [(0, 0), (-1, 2), (5, 6), (7, 3)]
#     result = arcStart(data)
#     print(result)
