import json, requests
from place import coordinates
from place import map
from datetime import date
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template')

def data_n():
    today = date.today()
    v = str(today).replace('-', '')
    return(v)

def forsq_json(loc):
    url = 'https://api.foursquare.com/v2/venues/explore'
    data_now = data_n()
    loc_type = 'restaurant'
    params = dict(
        client_id='X20YVWGASUAPPA5NEH1VYXZRFLAHOCUOFT3GZGHPWFLHBYWY',
        client_secret='55JTNXW11JA3UF4JYTH0AXLM1F32ARQSZI0DJKMVZQSEMFPD',
        v=data_now,
        ll=loc,
        query=loc_type,
        limit=1)

    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)

    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file)

    return data

def main(city):
    coordinate = coordinates(city)
    new_str_co = str(coordinate[0])+', '+str(coordinate[1])
    data = forsq_json(new_str_co)
    lst_name = data["response"]['groups'][0]['items'][0]['venue']['name']
    lst_loc = [[data["response"]['groups'][0]['items'][0]['venue']['location']['lat'], data["response"]['groups'][0]\
        ['items'][0]['venue']['location']['lng']]]
    map(lst_name, lst_loc[0], coordinate)
    #print(str(lst_name), lst_loc[0], coordinate)


@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    city = request.form['city']
    main(city)
    return render_template('result.html')

if __name__=="__main__":
    app.run()
    #print(main('Lviv'))




