from arc import Arc
from line import Line


def generateRoads(datapoints):
    roads = []

    # Create arcs
    Arc.instantiateAllArcs(datapoints)

    s = 0
    lastIndex = len(Arc.all) - 1
    for i in range(lastIndex):
        arc = Arc.all[i]
        # add arc
        if arc.curvature != 0:
            arc.s = s
            roads.append(arc)
        else:
            straightLine = Line.createLine(arc.xStart, arc.yStart, arc.hdg, arc.length, s)
            roads.append(straightLine)
        s += arc.length

        # add straight line if needed
        nextArc = Arc.all[i + 1]
        if arc.xEnd != nextArc.xStart or arc.yEnd != nextArc.yStart:
            straightLine = Line.createLine(arc.xEnd, arc.yEnd, nextArc.hdg, 0, s, nextArc.xStart, nextArc.yStart)
            roads.append(straightLine)
            s += straightLine.length

    # last arc/straight line to add
    arc = Arc.all[lastIndex]
    if arc.curvature != 0:
        arc.s = s
        roads.append(arc)
    else:
        straightLine = Line.createLine(arc.xStart, arc.yStart, arc.hdg, arc.length, s)
        roads.append(straightLine)
    s += arc.length

    nextArc = Arc.all[0]
    if arc.xEnd != nextArc.xStart or arc.yEnd != nextArc.yStart:
        straightLine = Line.createLine(arc.xEnd, arc.yEnd, nextArc.hdg, 0, s, nextArc.xStart, nextArc.yStart)
        roads.append(straightLine)
        s += straightLine.length

    return roads, s
