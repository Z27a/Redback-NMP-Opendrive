from lxml import etree
from roadGenerator import generateRoads
import json

def getInputCoordinates(filename: str):
    '''
    Returns a list of tuples : [(x, y)]
    '''
    
    with open(filename, "r") as f:
        jsonString = f.read()
    inputJson = json.loads(jsonString)
    
    returnList = []
    for coord in inputJson['data']:
        returnList.append(tuple(coord))
        
    return returnList

def createStraightNode(s, x, y, hdg, length):
    geometry = etree.Element("geometry", s=str(s), x=str(x), y=str(y), hdg=str(hdg), length=str(length))
    etree.SubElement(geometry, "line")
    return geometry

def createArcNode(s, x, y, hdg, length, curvature):
    geometry = etree.Element("geometry", s=str(s), x=str(x), y=str(y), hdg=str(hdg), length=str(length))
    etree.SubElement(geometry, "arc", curvature=str(curvature))
    return geometry

def writeToOpenDriveFile(roads, totalLength, openDriveTemplate):
    with open(openDriveTemplate, "r") as f:
        content = f.read()
    root = etree.fromstring(content)
    tree = etree.ElementTree(root)
    roadNode = root.xpath("/OpenDRIVE/road")[0]
    planViewNode = root.xpath("/OpenDRIVE/road/planView")[0]
    for geometry in roads:
        if geometry["type"] == "straight":
            planViewNode.append(createStraightNode(geometry['s'], geometry['x'], geometry['y'], geometry['hdg'], geometry['length']))
        elif geometry["type"] == "arc":
            planViewNode.append(createArcNode(geometry['s'], geometry['x'], geometry['y'], geometry['hdg'], geometry['length'], geometry["curvature"]))

    roadNode.set("length", str(totalLength))
    tree.write("test.xodr", pretty_print=True)

if __name__ == "__main__":
    inputCoordinates = getInputCoordinates("input.json")
    roads = generateRoads(inputCoordinates)
    writeToOpenDriveFile(roads[0], roads[1], "openDriveTemplate.xodr")
