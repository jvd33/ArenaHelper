from api.data_client import DataClient
from api.arena_client import ArenaClient
from jobs.startup import StartupJob
from mongo.db import MongoManager
import mongo.models as mm

if __name__ == "__main__":

    startup = StartupJob()
    db = MongoManager()
    #startup.seed()
    print(db.get_player("Aviro", "Thrall", True))
    # startup.seed()
