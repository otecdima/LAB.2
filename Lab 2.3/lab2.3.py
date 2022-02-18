"""LAB 2.3"""
import requests
from geopy.geocoders import Nominatim
import folium
from flask import Flask, render_template, url_for, request

def get_information_from_keys(username):
    """
    Return dictionary with information about friends in twitter.
    """
    key = 'AAAAAAAAAAAAAAAAAAAAABcXZQEAAAAAFitawJoUzroZoiCP41R0%2F\
yXXPHc%3DvATE65kkopZn2sQBHIXT5bCRF1v61uESR5ZGGDfR94pOiEldUd'
    headers = {'Authorization': f'Bearer {key}'}
    params = {'screen_name': username, 'count': 200}

    response = requests.get('https://api.twitter.com/1.1/friends/list.json',
                            headers=headers,
                            params=params)
    return response.json()

def get_location(info):
    """
    Return list with the username of a friend as the first element,\
    and tuple of coordinates as second one
    """
    if info['users'] == []:
        return False
    list_for_coord = []
    for element in info['users']:
        if element["location"] == '':
            continue
        try:
            location = Nominatim(user_agent = 'app').geocode(element["location"])
        except:
            continue
        if location == None:
            continue
        list_for_coord.append([element["screen_name"], (location.latitude, location.longitude)])
    return list_for_coord

def building_map(list_with_coor):
    """
    Function builds a map using folium
    """
    map = folium.Map(location=[20, 0], zoom_start=3, control_scale=True)

    markers_group = folium.FeatureGroup(name="Markers")
    map.add_child(markers_group)

    for element in list_with_coor:
        text = element[0]
        text = folium.IFrame(text, width=130, height=50)
        markers_group.add_child(folium.Marker(location=[element[1][0], element[1][1]], \
            popup=folium.Popup(text), icon=folium.Icon(color="red")))

    map.add_child(folium.LayerControl())
    map.save("templates/mapwithfriends.html")

def main(username):
    """
    Manin function with all the previous ones
    """
    info = get_information_from_keys(username)
    list_with_coor = get_location(info)
    if list_with_coor == False:
        return False
    else:
        building_map(list_with_coor)

application = Flask(__name__)
# object is created as "application" from module flask

@application.route("/")
def open_first_page():
    """
    opens a website-page
    """
    return render_template('index.html')

@application.route("/map", methods = ["POST"])
def run_a_site():
    """
    Using of method POST for getting usernames and creating a mao according to that username
    """
    username = request.form['text']
    mainf = main(username)
    if mainf == False:
        return render_template('index.html')
    else:
        return render_template('mapwithfriends.html')

application.config['TEMPLATES_AUTO_RELOAD'] = True

@application.after_request
def add_header(response):
    """
    Prevents saving created map in the cache and help us to create a new map
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response
