from math import sqrt


class Line:
    all = []

    def __init__(self, xStart=0.0, yStart=0.0, xEnd=0.0, yEnd=0.0, hdg=0.0, length=0.0, s=0.0):
        self.xStart = xStart
        self.yStart = yStart
        self.xEnd = xEnd
        self.yEnd = yEnd
        self.hdg = hdg
        self.length = length
        self.s = s
        self.type = "straight"

        Line.all.append(self)

    @classmethod
    def createLine(cls, xStart, yStart, hdg=0.0, length=0.0, s=0.0, xEnd=0.0, yEnd=0.0):
        if length == 0:
            length = cls.getLen([xStart, yStart], [xEnd, yEnd])

        return Line(
            xStart=xStart,
            yStart=yStart,
            xEnd=xEnd,
            yEnd=yEnd,
            hdg=hdg,
            length=length,
            s=s
        )

    @classmethod
    def getLen(cls, coord1, coord2):
        # Calculates the distance between two points
        x1, y1 = coord1
        x2, y2 = coord2
        return sqrt(abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2)
