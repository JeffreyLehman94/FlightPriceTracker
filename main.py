from Request_Methods import *
from Helper_Methods import *
import datetime
from datetime import timedelta
import time

d = datetime.date(2023, 8, 1)

for x in range(360):
        print(d)
        SESSION_ID = getSession_ID(d.year, d.month, d.day)
        JSON_DATA = getFlightPrices(SESSION_ID)
        PRICE = int(getCheapestFlight(JSON_DATA))
        saveAllData(JSON_DATA, d, PRICE)
        d = d + timedelta(days = 1)
        time.sleep(2)
    # except:
    #     print("Error on day %s" % d)
    #     d = d + timedelta(days=1)
    #     time.sleep(2)
