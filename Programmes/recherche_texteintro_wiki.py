# coding: utf-8

"""
    Ce script permet de récupérer la partie 'introduction'
    dans un article de Wikipedia à partir du 'pageid'
"""
#!/usr/bin/python3

import requests

# ------------------------------------------------------------
# test avec un "pageid = 676806" correspondant à la page concernant Napoléon  (pour la "tour eiffel", pageid = 1359783)
pageid_value = "676806"
# https://fr.wikipedia.org/w/api.php?action=query&pageids=676806&format=json&prop=extracts&redirects=1&exintro&explaintext
# ------------------------------------------------------------

S = requests.Session()

URL = "https://fr.wikipedia.org/w/api.php"

PARAMS = {"action": "query", "pageids": pageid_value, "format": "json", "prop": "extracts", "redirects": "1", "exintro":"", "explaintext":""} 

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA['query']['pages'][pageid_value]['extract'])