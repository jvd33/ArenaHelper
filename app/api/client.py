import requests
import os
import urllib.parse

"""
Superclass for the API Clients, makes calling the WoW API slightly easier
"""


class APIClient:
    def __init__(self, locale="en_US", region="us"):
        self.base = os.environ["APIURL"].format(region)
        self.region = region
        self.api_key = os.environ["APIKEY"]
        self.endpoints = {
            'realms': urllib.parse.urljoin(self.base, 'realm/status'),
            'races': urllib.parse.urljoin(self.base, 'data/character/races'),
            '2v2': urllib.parse.urljoin(self.base, 'leaderboard/2v2'),
            '3v3': urllib.parse.urljoin(self.base, 'leaderboard/3v3'),
            'rbg': urllib.parse.urljoin(self.base, 'leaderboard/rbg'),
            'player': urllib.parse.urljoin(self.base, 'character/{}/{}'),
            'classes': urllib.parse.urljoin(self.base, 'data/character/classes'),
            'talents': urllib.parse.urljoin(self.base, 'data/talents'),
        }
        self.locales = ['en_US', 'en_GB', 'es_ES', 'fr_FR', 'ru_RU', 'de_DE', 'pt_PT', 'it_IT']
        self.locale = locale

    # Makes a request to the URL with the given params, and appends the API key in sys environment
    def make_request(self, url, params):
        params.update({'apikey': self.api_key})
        response = requests.get(url, params=params)
        print("GET: " + response.url)
        return response.json()
