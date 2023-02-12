import json
import sqlite3
from datetime import date


def pprint(JSON_TEXT):
    print(json.dumps(JSON_TEXT, indent=2))


def saveAllData(JSON_TEXT, FLIGHT_DATE, PRICE):
    date_today = date.today()
    f = open("json_data.txt", "w")
    f.write(json.dumps(JSON_TEXT, indent=2))
    f.close()
    con = sqlite3.connect("prices.db")
    cur = con.cursor()
    try:
        cur.execute("CREATE TABLE prices(Record_Date, Flight_Date, Price)")
    except:
        print('Table already created')
    cur.execute(" INSERT INTO prices VALUES(?, ?, ?)",
                (date_today, FLIGHT_DATE, PRICE/1000))
    con.commit()


def getCheapestFlight(JSON_TEXT):
    return int(JSON_TEXT['content']['stats']['itineraries']['stops']['direct']['total']['minPrice']['amount'])
