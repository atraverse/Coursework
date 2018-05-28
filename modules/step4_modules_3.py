'''
Розробити основний модуль програми для проведення
дослідження. Програма повинна дозволяти проводити
обчислювальні експерименти з різними наборами
вхідних даних.
'''
import json, requests
from datetime import date
from geopy.geocoders import Nominatim

class Coordinate():
    def __init__(self):
        self.geolocator = Nominatim()
    def coordinates(self, city):
        '''
        (list)->(list)
        Return list with coordinates
        '''
        location = self.geolocator.geocode(city)
        lst = [str(location.latitude), str(location.longitude)]
        return str(', '.join(lst))

class Inputer():
    def __init__(self):
        self.city = str(input("Enter city: "))
        self.place_type = str(input("Enter place: "))
        self.inp_lim = int(input("Enter limits: "))

class Main():
    def __init__(self):
        self.city_co = Coordinate().coordinates(Inputer().city)
        self.v = str(date.today()).replace('-', '')
        self.data = None
        self.url = 'https://api.foursquare.com/v2/venues/explore'
    def param(self):
        params = dict(
            client_id='X20YVWGASUAPPA5NEH1VYXZRFLAHOCUOFT3GZGHPWFLHBYWY',
            client_secret='55JTNXW11JA3UF4JYTH0AXLM1F32ARQSZI0DJKMVZQSEMFPD',
            v=str(self.v),
            ll=self.city_co,
            query=Inputer().place_type,
            limit=Inputer().inp_lim
        )
        resp = requests.get(url=self.url, params=params)
        self.data = json.loads(resp.text)
        return self.data
    def write_to_file(self):
        with open("data_file.json", "w") as write_file:
            json.dump(self.data, write_file)