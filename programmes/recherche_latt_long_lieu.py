# coding: utf-8

"""
    Ce script permet de récupérer les lattitudes et longitudes
    d'un lieu grâce à une requête avec Googleplace
"""

import requests

# --------------------------------------------------------------
element_a_rechercher = "tour eiffel"
# --------------------------------------------------------------


session = requests.Session()

URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"

PARAMS = {"input": element_a_rechercher, "inputtype": "textquery", "fields": "formatted_address,name", "key": "AIzaSyAaICGdTIFPs_4qaw3g6FvdM5Gh2ZnoU9M"}

# PARAMS = {"action": "query", "list": "search", "srsearch": element_a_rechercher, "format": "json"}

response = session.get(url=URL, params=PARAMS)

data = response.json()

address = data['candidates'][0]['formatted_address']
name = data['candidates'][0]['name']

# print("Data :", data["candidates"][0])

# print("Name :", name, " et adresse :", address)

print("Dans Google, l'adresse de '{}' est {}".format(name, address))