"""
    This script uses the 'Wiki Media' API to determine the 'pageid'
    of a wikipedia article and the introduction of that article
"""
# coding: utf-8
import requests


class Wikipedia:
    """
        This class identifies the 'pageid' of a wikipedia article
        and get the introduction of this article in Wikipedia
        thanks to the API 'Wiki Media'
    """

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
        response = requests.get(url=cls.URL, params=PARAMS)
        # get the json content of the response
        data = response.json()

        if data['query']['searchinfo']['totalhits']:
            title = data['query']['search'][0]['title']
            pageid = data['query']['search'][0]['pageid']
        else:
            title = "ZERO_RESULTS"
            pageid = "ZERO_RESULTS"
        # return the title and the pageid of the article of wikipedia as strings
        return (title, pageid)

    @classmethod
    def intro(cls, pageid):
        """
            Find the introduction of a wikipedia article of a spot
            As input  : the 'pageid' of wikipedia of the spot as string
            In return : the 'pageid' of the wikipedia article of the spot as string
        """
        PARAMS = {"action": "query", "pageids": pageid,
                  "format": "json",
                  "prop": "extracts",
                  "redirects": "1",
                  "exintro": "",
                  "explaintext": ""
                 }
        if pageid == "ZERO_RESULTS":
            intro = "ZERO_RESULTS"
        else:
            # sent the query to the API 'Wiki Media'
            response = requests.get(url=cls.URL, params=PARAMS)
            # get the json content of the response
            introduction = response.json()
            intro = introduction['query']['pages'][str(pageid)]['extract']
        # return the introduction of the article of wikipedia as string
        return intro


if __name__ == '__main__':
    pass
