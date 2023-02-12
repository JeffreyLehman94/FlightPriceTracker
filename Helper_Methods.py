import json
import datetime


def pprint(JSON_TEXT):
    print(json.dumps(JSON_TEXT,indent=2))

def saveAllData(JSON_TEXT):
    f = open("test", "w")
    f.write(json.dumps(JSON_TEXT,indent=2))

def getCheapestFlight(JSON_TEXT):
    return int(JSON_TEXT['content']['stats']['itineraries']['stops']['direct']['total']['minPrice']['amount'])