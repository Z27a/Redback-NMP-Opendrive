from math import sqrt, acos, sin, cos, tan, pi


class Arc:
    all = []

    def __init__(self, xStart=0.0, yStart=0.0, xEnd=0.0, yEnd=0.0, hdg=0.0, length=0.0, curvature=0.0,
                 xOriginalPoint=0.0, yOriginalPoint=0.0, s=0.0):
        self.xStart = xStart
        self.yStart = yStart
        self.xEnd = xEnd
        self.yEnd = yEnd
        self.hdg = hdg
        self.length = length
        self.curvature = curvature
        self.xOriginalPoint = xOriginalPoint
        self.yOriginalPoint = yOriginalPoint
        self.s = s
        self.type = "arc"

        Arc.all.append(self)

    @classmethod
    def instantiateAllArcs(cls, dataPoints):
        # create arc for everything except the last point
        for i in range(len(dataPoints) - 1):
            cls.makeArcWithPositionsHeading(dataPoints[i - 1], dataPoints[i], dataPoints[i + 1])

        # create arc for last point
        cls.makeArcWithPositionsHeading(dataPoints[-2], dataPoints[-1], dataPoints[0])

        # add curvature and length to arcs created
        cls.addLengthCurvature()

    @classmethod
    def makeArcWithPositionsHeading(cls, prev, cur, next):
        '''
        :param prev: previous coordinate
        :param cur: current coord
        :param next: next coord
        '''
        lenBef = cls.getLen(prev, cur)
        lenAft = cls.getLen(cur, next)

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

        # calculate heading
        if lineBef[1] < 0:
            heading = acos(lineBef[0] * -1)
            heading += pi
        else:
            heading = acos(lineBef[0])

        # make new arc
        Arc(
            xStart=(cur[0] + cos(heading - pi) * minLen),
            yStart=(cur[1] + sin(heading - pi) * minLen),
            xEnd=(cur[0] + lineAft[0] * minLen),
            yEnd=(cur[1] + lineAft[1] * minLen),
            hdg=heading,
            xOriginalPoint=x2,
            yOriginalPoint=y2
        )

    @classmethod
    def mag(cls, a, b):
        return sqrt((a[1] - b[1]) ** 2 + (a[0] - b[0]) ** 2)

    @classmethod
    def orient(cls, a, b, c):
        delta = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
        if delta > 0:
            return True
        else:
            return False

    @classmethod
    def addLengthCurvature(cls):
        for arc in Arc.all:
            start = [arc.xStart, arc.yStart]
            point = [arc.xOriginalPoint, arc.yOriginalPoint]
            end = [arc.xEnd, arc.yEnd]

            a, b, c = cls.mag(start, point), cls.mag(point, end), cls.mag(start, end)
            angle = pi - acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
            curvature = tan(angle / 2) / a

            if angle == 0:
                length = cls.mag(start, end)
            else:
                length = a * angle / tan(angle / 2)

            arc.length = length

            if cls.orient(start, point, end):
                arc.curvature = curvature
            else:
                arc.curvature = -curvature

    @classmethod
    def getLen(cls, coord1, coord2):
        # Calculates the distance between two points
        x1, y1 = coord1
        x2, y2 = coord2
        return sqrt(abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2)
