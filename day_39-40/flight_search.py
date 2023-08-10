import requests
from datetime import datetime, timedelta
from pprint import pprint
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.locations_endpoint = 'https://api.tequila.kiwi.com/locations/query'
        self.search_endpoint = 'https://api.tequila.kiwi.com/v2/search'
        self.headers = {
            'apikey': '5h64SQLhfX7AnrKgJXlhNPmv8O9I9oA6',
            'accept': 'application/json',
        }
        self.date_from = self.calc_date(1)
        self.date_to = self.calc_date(180)
        self.return_from = self.calc_date(9)
        self.return_to = self.calc_date(29)

    def calc_date(self,days_ahead):
        date = (datetime.now() + timedelta(days=days_ahead)).strftime('%d/%m/%Y')
        return date

    def get_iata(self, city):

        #return 'TESTING'
        params = {
            'term': city,
        }

        response = requests.get(url=self.locations_endpoint, params=params, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        return data['locations'][0]['code']

    def get_cheapest_flight(self, city, price, stop_overs=0):

        params = {
            'fly_from': 'LON',
            'fly_to': city,
            'date_from': self.date_from,
            'date_to': self.date_to,
            'return_from': self.return_from,
            'return_to': self.return_to,
            'curr': 'GBP',
            'price_to': price,
            'max_stopovers': stop_overs
        }

        response = requests.get(url=self.search_endpoint, params=params, headers=self.headers)
        response.raise_for_status()
        data = response.json()

        pprint((data['route'][0]["cityTo"]))
        return
        # return data['data'][0]['conversion']['GBP'], data['data'][0]['cityCodeFrom'],\
        #     data['data'][0]['flyFrom'], data['data'][0]['cityCodeTo'],\
        #     data['data'][0]['flyTo'], data['data'][0]['route'][0]['utc_departure'].split('T')[0],\
        #     data['data'][0]['route'][1]['utc_departure'].split('T')[0],\
        #     data['data'][0]['max_stopovers'],data['data'][0]['via_city']










