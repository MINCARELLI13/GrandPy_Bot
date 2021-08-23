""" This script test a parser of sentences and 2 python modules
    that make calls to the Google Palce and Wiki Media APIs
"""
# coding: utf-8

import sys
sys.path.append('C:/Users/utilisateur/'
                'Desktop/Formation_OpenClassRoom/'
                'Projet_7/PROJET/GrandPy_Bot/ChatBot/')
import requests

import pytest

from parser_question import Parser
from location_place import Place
from recherche_pageids_wiki import Wikipedia


# ------------------------ TEST OF PARSER_QUESTION MODULE ------------------------------

class TestParser:
    """ Test the parser_question module """

    # a lot of tests :)
    @pytest.mark.parametrize("question, expected_result",[
        ("Salut GrandPy ! Est-ce que tu sais où se trouve la 'bonne mère' ?",
        ['où', 'bonne', 'mère']),
        ("Bonsoir, pourrais-tu me donner l'adresse de la Tour Eiffel, s'il te plaît ?",
        ['adresse', 'Tour', 'Eiffel']),
        ("Coucou Grand Py, saurais-tu m'indiquer l'endroit où je pourrais trouver Openclassrooms ?",
        ['endroit', 'où', 'Openclassrooms'])
    ])
    def test_parsing(self, question, expected_result):
        assert Parser.parsing(question) == expected_result


# ------------------------ MOCK OF GOOGLE PLACE API ------------------------------

class MockResponsePlace:
    """ Imitates the responses following requests made to the
        Google Place API and the transformation into a json object
    """

    # imitates the responses following requests made to the Google Place API
    RESPONSES = {'où bonne mère': ('Basilique Notre-Dame de la Garde',
                                   'Rue Fort du Sanctuaire, 13006 Marseille, France',
                                   43.2839533,
                                   5.3712377
                                  ),
                'adresse Tour Eiffel': ('Tour Eiffel',
                                        'Champ de Mars, 5 Av. Anatole France, 75007 Paris, France',
                                        48.85837009999999,
                                        2.2944813,
                                       ),
                'sähr^pôrzejgùm': ('ZERO_RESULTS',
                                   'ZERO_RESULTS',
                                   'ZERO_RESULTS',
                                   'ZERO_RESULTS'
                                  )
                }

    # imitates the transformation from the responses of Google Place API into a json object
    RESPONSES_JSON = {'où bonne mère':
    {'candidates': [{'formatted_address': 'Rue Fort du Sanctuaire, 13006 Marseille, France',
                     'geometry': {'location': {'lat': 43.2839533, 'lng': 5.3712377}},
                     'name': 'Basilique Notre-Dame de la Garde'}],
     'status': 'OK'},
                 'adresse Tour Eiffel':
    {'candidates': [{'formatted_address': 'Champ de Mars, 5 Av. Anatole France,'
                                          ' 75007 Paris, France',
                     'geometry': {'location': {'lat': 48.85837009999999, 'lng': 2.2944813}},
                     'name': 'Tour Eiffel'}],
     'status': 'OK'},
                 'sähr^pôrzejgùm':
    {'candidates': [{'formatted_address': 'ZERO_RESULTS',
                     'geometry': {'location': {'lat': 'ZERO_RESULTS', 'lng': 'ZERO_RESULTS'}},
                     'name': 'ZERO_RESULTS'}],
     'status': 'OK'}}

    def __init__(self, ask):
        self.ask = ask

    def json(self):
        return self.RESPONSES_JSON[self.ask]

@pytest.mark.parametrize('question, expected_result',[
        ('où bonne mère', MockResponsePlace.RESPONSES['où bonne mère']),
        ('adresse Tour Eiffel', MockResponsePlace.RESPONSES['adresse Tour Eiffel']),
        ('sähr^pôrzejgùm', MockResponsePlace.RESPONSES['sähr^pôrzejgùm'])
    ])
def test_place(monkeypatch, question, expected_result):
    Mock_response_place = MockResponsePlace(question)

    # Any arguments must be passed and mock_return() will always return our
    # mocked object, which only has the .json() method.
    def mock_return(url, params):
        return Mock_response_place

    # replace the request to Google Place API by 'Mock_response_place'
    monkeypatch.setattr(requests, 'get', mock_return)
    assert Place.location(question) ==  expected_result


# ------------------------ MOCKS OF WIKI MEDIA API ------------------------------

class MockResponseWikiPageId:

    # mock json() method returns a specific testing dictionary
    @staticmethod
    def json():
        return {'batchcomplete': '',
                'continue': {'sroffset': 10, 'continue': '-||'},
                             'query': {'searchinfo': {'totalhits': 4318},
                             'search': [{'ns': 0,
                                         'title': 'Tour Eiffel',
                                         'pageid': 1359783,
                                         'size': 139459,
                                         'wordcount': 15149,
                                         'timestamp': '2021-07-29T18:45:51Z'
                                        }]
                                       }
                }

def test_wiki_page_id(monkeypatch):
    """ Test the page_id request """

    def mock_return(url, params):
        return MockResponseWikiPageId()

    # apply the monkeypatch for requests.get to mock_return
    monkeypatch.setattr(requests, "get", mock_return)

    # response.json, which contains the response of requests.get, uses the monkeypatch
    assert Wikipedia.page_id(['Tour Eiffel']) == ('Tour Eiffel', 1359783)


class MockResponseWikiIntroduction:

    @staticmethod
    def json():
        return {'batchcomplete': '',
                'query': {'pages': {'1359783': {
                    'pageid': 1359783,
                    'ns': 0,
                    'title': 'Tour Eiffel',
                    'extract': "La tour Eiffel est une tour de fer puddlé "\
                               "de 324 mètres de hauteur (avec antennes)."\
                }}}}


def test_wiki_introduction(monkeypatch):
    """ Test the introduction request """

    # don't forget arguments to simulate the 'request.get(url, params)'
    def mock_return(url, params):
        return MockResponseWikiIntroduction()

    # apply the monkeypatch for requests.get to mock_return
    monkeypatch.setattr(requests, "get", mock_return)

    # finnaly, test the response to API and the json method
    assert Wikipedia.intro('1359783') == "La tour Eiffel est une tour de fer puddlé "\
                                         "de 324 mètres de hauteur (avec antennes)."\


if __name__ == '__main__':
    pass
