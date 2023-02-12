import json
import datetime


def pprint(JSON_TEXT):
    print(json.dumps(JSON_TEXT,indent=2))

def saveAllData(JSON_TEXT):
    f = open("test", "w")
    f.write(json.dumps(JSON_TEXT,indent=2))

# ctrl + / to block comment
# example of adding a week to a date below
# import datetime
# import datedelta
# d = datetime.date(2023, 1, 1)
# d += 1 * datedelta.WEEK
# print(d)