""" Ce script permet de récupérer le "pageid" d'une recherche dans Wikipedia """
import requests

session = requests.Session()

URL = "https://fr.wikipedia.org/w/api.php"

PARAMS = {"action": "query", "list": "search", "srsearch": "napoleon", "format": "json"}

response = session.get(url=URL, params=PARAMS)

data = response.json()

title = data['query']['search'][0]['title']
pageid = data['query']['search'][0]['pageid']

print("Dans Wikipedia, le 'pageid' de '{}' est {}".format(title, pageid))