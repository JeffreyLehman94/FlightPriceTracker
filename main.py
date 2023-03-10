from Request_Methods import *
from Helper_Methods import *
import datetime
from datetime import timedelta
import time

d = datetime.date(2023, 8, 1)
DESTINATION = 'SEA'
for x in range(360):
    print(d)
    SESSION_ID = getSession_ID(d.year, d.month, d.day, DESTINATION)
    JSON_DATA = getFlightPrices(SESSION_ID)
    try:
        PRICE = int(getCheapestFlight(JSON_DATA))
        saveAllData(JSON_DATA, d, PRICE, DESTINATION)
        d = d + timedelta(days=1)
    except:
        print('try again')
        x -= 1
    time.sleep(2)
