"""
    This script uses the 'Wiki Media' API to determine the 'pageid'
    of a wikipedia article and the introduction of that article
"""
# coding: utf-8

import requests
import json


class Wikipedia:
    """
        This class identifies the 'pageid' of a wikipedia article
        and get the introduction of this article in Wikipedia
        thanks to the API 'Wiki Media'
    """

    # creation of a session 
    SESSION = requests.Session()
    # url of the 'Wiki Media' API to build the endpoints
    URL = "https://fr.wikipedia.org/w/api.php"

    @classmethod
    def page_id(cls, spot_name):
        """
            Find the 'pageid' of a wikipedia article of a spot
            As input  : the name of the spot as string
            In return : the 'pageid' of the wikipedia article of the spot as string
        """
        PARAMS = {"action": "query", "list": "search", "srsearch": spot_name, "format": "json"}
        # sent the query to the API 'Wiki Media'
        response = cls.SESSION.get(url=cls.URL, params=PARAMS)
        # get the json content of the response 
        data = response.json()
        title = data['query']['search'][0]['title']
        pageid = data['query']['search'][0]['pageid']
        # return the title and the pageid of the article of wikipedia as strings
        return (title, pageid)
    
    @classmethod
    def intro(cls, pageid):
        """
            Find the introduction of a wikipedia article of a spot
            As input  : the 'pageid' of wikipedia of the spot as string
            In return : the 'pageid' of the wikipedia article of the spot as string
        """
        PARAMS = {"action": "query", "pageids": pageid, "format": "json", "prop": "extracts", "redirects": "1", "exintro":"", "explaintext":""}
        # sent the query to the API 'Wiki Media'
        response = cls.SESSION.get(url=cls.URL, params=PARAMS)
        # get the json content of the response
        introduction = response.json()
        introduction = introduction['query']['pages'][str(pageid)]['extract']
        # return the introduction of the article of wikipedia as string
        return introduction


if __name__ == '__main__':
    # pageid(tour eiffel) = 1359783
    # result = Wikipedia.page_id("bonne mere")
    result = Wikipedia.page_id("Basilique Notre-Dame de la Garde")
    # print(result)
    print("Dans Wikipedia, le 'pageid' de '{}' est {}".format(result[0], result[1]))
    result = Wikipedia.intro(result[1])
    # print()
    print(result)