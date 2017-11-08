from api import client
import urllib.parse
from mongo.db import MongoManager

"""
API Client for gathering all general game data.
Realms
Talents for all classes and specs
Races
Classes and specs
Player Armory Data
"""


class DataClient(client.APIClient):

    def __init__(self, locale=None):
        super().__init__(locale)
        self.db = MongoManager()

    # Sends an HTTP request to get all realm data for a specific locale
    def get_realms(self):
        url = self.endpoints["realms"]
        payload = {'locale': self.locale}
        json = self.make_request(url, payload)
        self.db.insert_realms(json["realms"])

    # Sends a request that gets all talent choices and constructs a talent object
    def get_talents(self):
        url = self.endpoints["talents"]
        payload = {"locale": self.locale}
        json = self.make_request(url, payload)
        for k, v in dict(json).items():
            cls = v["class"]
            for tier in v["talents"]:
                for t in tier:
                    for i in range(len(t)):
                        talent = {}
                        for a, b in t[i]["spell"].items():
                            talent.update({a: b})
                        talent["tier"] = t[i]["tier"]
                        talent["column"] = t[i]["column"]
                        talent["class_name"] = cls.replace("-", " ").lower()
                        if "spec" in t[i].keys():
                            talent["spec_name"] = t[i]["spec"]["name"]
                        self.db.insert_talent(talent)

    # Sends a request that loads in all talent specializations
    def get_specs(self):
        url = self.endpoints["talents"]
        payload = {'locale': self.locale}
        json = self.make_request(url, payload)
        for k, v in dict(json).items():
            cls = v["class"]
            for spec in v["specs"]:
                spec["class_name"] = cls.lower()
                self.db.insert_talent_trees(spec)

    # Sends a request that gets all playable race data
    def get_races(self):
        url = self.endpoints["races"]
        payload = {'locale': self.locale}
        json = self.make_request(url, payload)
        self.db.insert_races(json["races"])

    # Sends a request that gets all player class data
    def get_classes(self):
        url = self.endpoints["classes"]
        payload = {'locale': self.locale}
        json = self.make_request(url, payload)
        self.db.insert_classes(json["classes"])


