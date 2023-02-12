import json
import requests
from requests.structures import CaseInsensitiveDict

def getSession_ID(year,month,day):
    url = "https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create"
    headers = CaseInsensitiveDict()
    headers["x-api-key"] = "prtl6749387986743898559646983194"
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    data = ' {"query":{"market":"US","locale":"en-GB","currency":"USD","query_legs":[{"origin_place_id":{"iata":"PHL"},"destination_place_id":{"iata":"SJU"},"date":{"year":%i,"month":%i,"day":%i}},{"origin_place_id":{"iata":"SJU"},"destination_place_id":{"iata":"PHL"},"date":{"year":2023,"month":8,"day":%i}}],"adults":1,"cabin_class":"CABIN_CLASS_ECONOMY"}}' \
           % (year,month,day,day+7)
    resp = requests.post(url, headers=headers, data=data)
    json_data = resp.json()
    return json_data['sessionToken']

def getFlightPrices(SESSION_ID):
    url = "https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/poll/%s" % (SESSION_ID)
    headers = CaseInsensitiveDict()
    headers["x-api-key"] = "prtl6749387986743898559646983194"
    headers["Content-Length"] = "0"
    return requests.post(url, headers=headers).json()