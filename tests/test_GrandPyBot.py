# coding: utf-8

import sys
import requests

import pytest

sys.path.append('C:/Users/utilisateur/Desktop/Formation_OpenClassRoom/Projet_7/PROJET/GrandPy_Bot/ChatBot/')
from parser_question import Parser
from location_place import Place
from recherche_pageids_wiki import Wikipedia


class TestParser:

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
    

class MockResponsePlace:

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

    RESPONSES_JSON = {'où bonne mère':
    {'candidates': [{'formatted_address': 'Rue Fort du Sanctuaire, 13006 Marseille, France',
                     'geometry': {'location': {'lat': 43.2839533, 'lng': 5.3712377}},
                     'name': 'Basilique Notre-Dame de la Garde'}],
     'status': 'OK'},
                 'adresse Tour Eiffel':
    {'candidates': [{'formatted_address': 'Champ de Mars, 5 Av. Anatole France, 75007 Paris, France',
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

    Mock_response = MockResponsePlace(question)

    def mock_return(url, params):
        return Mock_response
    
    monkeypatch.setattr(requests, 'get', mock_return)
    assert Place.location(question) ==  expected_result


class MockResponseWikiPageId:

    # mock json() method always returns a specific testing dictionary
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

    # Any arguments may be passed and mock_get() will always return our
    # mocked object, which only has the .json() method.
    def mock_return(url, params):
        return MockResponseWikiPageId()

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_return)

    # app.get_json, which contains requests.get, uses the monkeypatch
    assert Wikipedia.page_id(['Tour Eiffel']) == ('Tour Eiffel', 1359783)


class MockResponseWikiIntroduction:

    # mock json() method always returns a specific testing dictionary
    @staticmethod
    def json():
        return {'batchcomplete': '',
                'query': {'pages': {'1359783': {
                    'pageid': 1359783,
                    'ns': 0,
                    'title': 'Tour Eiffel',
                    'extract': "La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes)."
                }}}}


def test_wiki_introduction(monkeypatch):

    # Any arguments may be passed and mock_get() will always return our
    # mocked object, which only has the .json() method.
    def mock_return(url, params):
        return MockResponseWikiIntroduction()

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_return)

    # app.get_json, which contains requests.get, uses the monkeypatch
    assert Wikipedia.intro('1359783') == "La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes)."


if __name__ == '__main__':
    # print("MockResponse('où bonne mère').json() :", MockResponse('où bonne mère').json())
    # print("MockResponse('adresse Tour Eiffel').json() :", MockResponse('adresse Tour Eiffel').json())
    print("MockResponse('sähr^pôrzejgùm').json() :", MockResponse('sähr^pôrzejgùm').json())
