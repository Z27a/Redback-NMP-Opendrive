import os
import json

def getInputCoordinates(filename: str):
    '''
    Returns a list of tuples (x, y)
    '''
    
    with open(filename, "r") as f:
        jsonString = f.read()
    inputJson = json.loads(jsonString)
    
    returnList = []
    for coord in inputJson['data']:
        returnList.append(tuple(coord))
        
    return returnList
    

if __name__ == "__main__":
    inputCoordinates = getInputCoordinates("input.json")
