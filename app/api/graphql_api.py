import requests
from api.client import APIClient
from mongo import db, models
"""
Class that will be exposed as an API if any players or developers want to pull their own JSON data from this app
"""


class GraphQL_API(APIClient):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = db.MongoManager()

    def get_full_player(self, player_name, realm):
        return models.Player.objects({})

