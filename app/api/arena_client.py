import requests
from api import client
from mongo.db import MongoManager
from datetime import datetime

"""
API Client for gathering all PvP specific data.
2v2 Ladder Data
3v3 Ladder Data
RBG Ladder Data
Player PvP Statistics
Player PvP Achievements
Honor Talents when available! (Pls blizz, pls)
"""


class ArenaClient(client.APIClient):

    def __init__(self, locale=None):
        super().__init__(locale)
        self.db = MongoManager()

    # Sends a request that gets a specific PvP ladder by locale
    def get_pvp_ladder(self, bracket):
        url = self.endpoints[bracket]
        payload = {'locale': self.locale}
        json = self.make_request(url, payload)
        json.update({'bracket': bracket, 'locale': self.locale, 'fetch_date': datetime.now()})
        self.db.insert_ladder(json)

    # Sends a request that gets PvP stats for a specific player
    def get_pvp_stats(self, player_name, realm):
        url = self.endpoints['player'].format(realm, player_name)
        payload = {'locale': self.locale, 'fields': 'pvp'}
        json = self.make_request(url, payload)
        return json

    # Sends a request that gets all the highly specific armory data for a specific player based on name, realm, locale
    def get_player(self, player_name, realm):
        fields = ["achievements", "pvp", "guild", "items", "professions", "statistics", "talents", "titles"]
        url = self.endpoints["player"].format(realm, player_name)
        payload = {'locale': self.locale}
        payload.update({'fields': fields})
        json = self.make_request(url, payload)
        json.update({'realm': realm})
        self.db.insert_player(json)

