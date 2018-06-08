import folium
from geopy.geocoders import Nominatim
def coordinates(i):
    '''
    (list)->(list)
    Return list with coordinates
    '''
    geolocator = Nominatim()
    location = geolocator.geocode(i)
    lst = [location.latitude, location.longitude]
    return lst

# def point(loc, friends):
#     '''
#     Main function, create HTML file and enter information to it
#     '''
#     lst = loc
#     for i in lst:
#         if type(i) != "list":
#             lst.remove(i)
#     map1 = folium.Map(location=lst, zoom_start=1)
#     people = folium.FeatureGroup(name='Place')
#     for i, j in zip(lst, friends):
#         people.add_child(folium.Marker(location=i, icon=folium.Icon(),
#                                        popup=j))
#
#     map1.add_child(people)
#     map1.add_child(folium.LayerControl())
#     map1.save('template/result.html')

def map(place,loc, coordinate):
    map = folium.Map(location= coordinate, zoom_start=10)
    map.add_child(folium.Marker(location=loc,
                                popup=place,
                                icon=folium.Icon(color='red', icon='info-sign')))
    map.save("template/result.html")

if __name__=='__main__':
    #print(coordinates('New York'))
    lst_loc = [coordinates('Kiev')]
    # print(lst_loc)
    lst_name = [['Kiev']]
    print(coordinates('Lviv'))
    map('Львівська майстерня шоколаду', [49.8411532447315, 24.03317481279373], [49.841952, 24.0315921])