'''
Навести приклад використання відповідного пакету
модулів зі стандартної бібліотеки для роботи з даними,
які будуть отримані з мережі Інтернет.
'''
import json, requests
from datetime import date
from place import coordinates
url = 'https://api.foursquare.com/v2/venues/explore'

inputer = str(input("Enter city: "))
inp_type = str(input("Enter place: "))
inp_lim = int(input("Enter limits: "))
city_co = coordinates(inputer)
v = str(date.today())
v1 = v.replace('-', '')

params = dict(
  client_id='X20YVWGASUAPPA5NEH1VYXZRFLAHOCUOFT3GZGHPWFLHBYWY',
  client_secret='55JTNXW11JA3UF4JYTH0AXLM1F32ARQSZI0DJKMVZQSEMFPD',
  v=str(v1),
  ll=city_co,
  query=inp_type,
  limit=1
)
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

a = data["response"]
b= a['headerLocation']
print(a)
print(b)
