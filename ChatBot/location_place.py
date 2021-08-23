"""
   Retrieve the address and the geographic coordinates
   of a spot through a request with the Google Place API
"""

# coding: utf-8

import requests
import os


class Place:
    """ Get the address and geographic coordinates of a spot """

    # url of the 'Google Place' API to build the endpoints
    URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"

    @classmethod
    def location(cls, spot):
        """
            Get the address and geographic coordinates of a 'spot'
            As input  : the 'spot' as string (exple : 'adresse tour Eiffel')
            In return : the address and coordinates of the 'spot'
        """
        PARAMS = {"input": spot,
                  "inputtype": "textquery",
                  "fields": "formatted_address,geometry,name",
                  "key": os.environ['Google_Place_KEY']}
        # "key": "AIzaSyAaICGdTIFPs_4qaw3g6FvdM5Gh2ZnoU9M"
        # sent the query to the API 'Google Place'
        response = requests.get(url=cls.URL, params=PARAMS)
        # get the json content of the response
        data = response.json()
        # if the Google Place API succeeded in identifying the spot
        if data['candidates']:
            address = data['candidates'][0]['formatted_address']
            name = data['candidates'][0]['name']
            latt = data['candidates'][0]['geometry']['location']['lat']
            long = data['candidates'][0]['geometry']['location']['lng']
        else:
            # in case there is no answer
            address = "ZERO_RESULTS"
            name = "ZERO_RESULTS"
            latt = "ZERO_RESULTS"
            long = "ZERO_RESULTS"
        # return the address and geographic coordinates of the 'spot' as strings
        return name, address, latt, long


if __name__ == '__main__':
    pass
    # name, address, latt, long = Place.location("adresse bonne mère")
    # name, address = Place.location('tour eiffel')
    # print("Dans Google, l'adresse de '{}' est {} (longitutde: {}, latitude {}".format(name, address, long, latt))
    # ask = "adresse bonne mère"
    # ask = "adresse Tour Eiffel"
    # ask = "sähr^pôrzejgùm"
    # print(ask, Place.location(ask))
