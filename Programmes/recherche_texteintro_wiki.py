""" Ce script permet de récupérer la partie 'introduction' dans un article de Wikipedia à partir du 'pageid' """
#!/usr/bin/python3

"""
    opensearch.py
    MediaWiki API Demos
    Demo of `Opensearch` module: Search the wiki and obtain
	results in an OpenSearch (http://www.opensearch.org) format
    MIT License
"""

import requests

S = requests.Session()

URL = "https://fr.wikipedia.org/w/api.php"

# test avec un "pageid" correspondant à la page concernant Napoléon
pageid_value = "676806"

PARAMS = {"action": "query", "pageids": pageid_value, "format": "json", "prop": "extracts", "redirects": "1", "exintro":"", "explaintext":""} 

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA['query']['pages'][pageid_value]['extract'])