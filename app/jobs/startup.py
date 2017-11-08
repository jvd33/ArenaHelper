from api.arena_client import ArenaClient
from api.data_client import DataClient
from mongo.db import MongoManager
from jobs.ladder_update import LadderUpdateJob
import pymongo as pm
import mongo.models as mm
import os

"""
This runs on initial start up, seeding all necessary data for a first-time run of the program
Stores the relevant data from Blizzard's API as JSON in MongoDB

Seeds:
2v2, 3v3, and RBG ladders for all regions
Realms
Classes
Races
Talents

Does not seed:
Individual player armory data


Data must be seeded in the proper order!
"""


class StartupJob:
    def __init__(self):
        self.db = MongoManager()
        self.host = os.environ["MONGODB_HOST"]
        self.ladder_update = LadderUpdateJob()
        self.regions = ['en_US', 'en_GB', 'es_ES', 'fr_FR', 'ru_RU', 'de_DE', 'pt_PT', 'it_IT']
        self.dc = DataClient()
        self.ac = ArenaClient()

    # Seeds all data necessary for the system to run initially
    def seed(self):
        actions = {
            "realm": self.dc.get_realms,
            "player_talent": self.dc.get_talents,
            "player_talent_tree": self.dc.get_specs,
            "player_classes": self.dc.get_classes,
            "player_races": self.dc.get_races,
        }
        pmc = pm.MongoClient(self.host, 27017)
        db = pmc['arenahelper']
        for k in actions.keys():
            actions[k]() if k not in db.collection_names() else None
        self.ladder_update.update_ladders()

        self.ac.get_player("Languish", "Thrall")
        self.ac.get_player("Zavgor", "Mal'Ganis")
        self.ac.get_player("Aviro", "Thrall")
        self.seed_top_10_each_bracket()

    # Seeds the armory player for the top 100 players in each bracket, no duplicates
    def seed_top_10_each_bracket(self):
        ladders = mm.PvPLadder.objects().all()
        for ladder in ladders:
            top = ladder.players[0:10]
            for player in top:
                self.ac.get_player(player.name, player.realm_name)
