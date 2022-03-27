from arcStartPt import arcPos, getLen
from arcFinder import finder

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

    # get arcs
    arcPositionsHeading = arcPos(datapoints)
    arcStarts = [(element[0][0], element[0][1]) for element in arcPositionsHeading] 
    arcEnds = [(element[1][0], element[1][1]) for element in arcPositionsHeading] 
    arcHeadings = [element[2] for element in arcPositionsHeading]

    # generate arc length and curvature
    arcLengthCurvature = list(map(finder, arcStarts, datapoints, arcEnds))

    s = 0
    lastIndex = len(datapoints) - 1
    # determine if straight lines are needed and add to road list
    for i in range(lastIndex):
        # add arc
        if arcLengthCurvature[i][1] != 0:
            roads.append(generateArc(s, arcStarts[i][0], arcStarts[i][1], arcHeadings[i], arcLengthCurvature[i][0], arcLengthCurvature[i][1]))
        else:
            roads.append(generateStraight(s, arcStarts[i][0], arcStarts[i][1], arcHeadings[i], arcLengthCurvature[i][0]))
        s += arcLengthCurvature[i][0]
        # add straight line if needed
        if arcEnds[i] != arcStarts[i + 1]:
            straightLength = getLen(arcEnds[i], arcStarts[i + 1])
            roads.append(generateStraight(s, arcEnds[i][0], arcEnds[i][1], arcHeadings[i + 1], straightLength))
            s += straightLength
    
    # last arc/straight line to add
    if arcLengthCurvature[lastIndex][1] != 0:
        roads.append(generateArc(s, arcStarts[lastIndex][0], arcStarts[lastIndex][1], arcHeadings[lastIndex], arcLengthCurvature[lastIndex][0], arcLengthCurvature[lastIndex][1]))
    else:
        roads.append(generateStraight(s, arcStarts[lastIndex][0], arcStarts[lastIndex][1], arcHeadings[lastIndex], arcLengthCurvature[lastIndex][0]))
    s += arcLengthCurvature[lastIndex][0]
    if (arcEnds[lastIndex] != arcStarts[0]):
        straightLength = getLen(arcEnds[lastIndex], arcStarts[0])
        roads.append(generateStraight(s, arcEnds[lastIndex][0], arcEnds[lastIndex][1], arcHeadings[0], straightLength))
        s += straightLength

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