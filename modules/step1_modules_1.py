'''
Навести приклад використання вказаного API за
допомогою програми оболонки.
'''
def main():
    '''
    Using Foursquare Api
    :return: None
    '''
    import json, requests
    url = 'https://api.foursquare.com/v2/venues/explore'

    params = dict(
      client_id='X20YVWGASUAPPA5NEH1VYXZRFLAHOCUOFT3GZGHPWFLHBYWY',
      client_secret='55JTNXW11JA3UF4JYTH0AXLM1F32ARQSZI0DJKMVZQSEMFPD',
      v='20180323',
      ll='40.7243,-74.0018',
      query='coffee',
      limit=1
    )
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file)