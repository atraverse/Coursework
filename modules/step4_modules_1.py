'''
Розробити (адаптувати) клас для реалізації необхідної
структури даних
'''
import json, requests
from datetime import date
from place import coordinates

class Main():
    url = 'https://api.foursquare.com/v2/venues/explore'
    def __init__(self):
        self.inputer = str(input("Enter city: "))
        self.inp_type = str(input("Enter place: "))
        self.inp_lim = int(input("Enter limits: "))
        self.city_co = coordinates(self.inputer)
        self.v = str(date.today()).replace('-', '')
        self.data = None
    def param(self):
        params = dict(
            client_id='X20YVWGASUAPPA5NEH1VYXZRFLAHOCUOFT3GZGHPWFLHBYWY',
            client_secret='55JTNXW11JA3UF4JYTH0AXLM1F32ARQSZI0DJKMVZQSEMFPD',
            v=str(v1),
            ll=city_co,
            query=inp_type,
            limit=1
        )
        resp = requests.get(url=url, params=params)
        self.data = json.loads(resp.text)
    def write_to_json(self):
        with open("data_file.json", "w") as write_file:
            json.dump(self.data, write_file)

