from arc import Arc
from line import Line


def generateRoads(datapoints):
    # initialise road points
    # for straight  {
    #               "type": "straight", 
    #               "s": s,
    #               "x": xStart, 
    #               "y": yStart, 
    #               "hdg": heading, 
    #               "length": length
    #               }
    # for arc       {
    #               "type": "arc",
    #               "s": s, 
    #               "x": xStart, 
    #               "y": yStart, 
    #               "hdg": heading, 
    #               "length": length
    #               "curvature"
    #               }
    roads = []

    # Create arcs
    Arc.instantiateAllArcs(datapoints)

    s = 0
    lastIndex = len(Arc.all) - 1
    for i in range(lastIndex):
        arc = Arc.all[i]
        # add arc
        if arc.curvature != 0:
            roads.append(generateArc(s, arc.xStart, arc.yStart, arc.hdg, arc.length, arc.curvature))
        else:
            roads.append(generateStraight(s, arc.xStart, arc.yStart, arc.hdg, arc.length))
        s += arc.length

        # add straight line if needed
        nextArc = Arc.all[i + 1]
        if arc.xEnd != nextArc.xStart or arc.yEnd != nextArc.yStart:
            straightLine = Line.createLine(arc.xEnd, arc.yEnd, nextArc.xStart, nextArc.yStart, nextArc.hdg)
            roads.append(
                generateStraight(s, straightLine.xStart, straightLine.yStart, straightLine.hdg, straightLine.length))
            s += straightLine.length

    # last arc/straight line to add
    arc = Arc.all[lastIndex]
    if arc.curvature != 0:
        roads.append(generateArc(s, arc.xStart, arc.yStart, arc.hdg, arc.length, arc.curvature))
    else:
        roads.append(generateStraight(s, arc.xStart, arc.yStart, arc.hdg, arc.length))
    s += arc.length

    nextArc = Arc.all[0]
    if arc.xEnd != nextArc.xStart or arc.yEnd != nextArc.yStart:
        straightLine = Line.createLine(arc.xEnd, arc.yEnd, nextArc.xStart, nextArc.yStart, nextArc.hdg)
        roads.append(
            generateStraight(s, straightLine.xStart, straightLine.yStart, straightLine.hdg, straightLine.length))
        s += straightLine.length

    return roads, s


def generateStraight(s, x, y, hdg, length):
    return {
        "type": "straight",
        "s": s,
        "x": x,
        "y": y,
        "hdg": hdg,
        "length": length
    }


def generateArc(s, x, y, hdg, length, curvature):
    return {
        "type": "arc",
        "s": s,
        "x": x,
        "y": y,
        "hdg": hdg,
        "length": length,
        "curvature": curvature
    }
