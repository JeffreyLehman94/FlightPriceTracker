from Request_Methods import *
from Helper_Methods import *
import datetime
import datedelta

d = datetime.date(2023, 8, 1)
d += 1 * datedelta.WEEK

SESSION_ID = getSession_ID(d.year,d.month,d.day)
JSON_DATA = getFlightPrices(SESSION_ID)
saveAllData(JSON_DATA)