import mongoengine as me
import mongo.models as mm
from mongoengine.errors import NotUniqueError
import pymongo as pm
import os
from bson import ObjectId
from bson.json_util import dumps

"""
MongoDB Management Class. Responsible for all interaction with the underlying document store
"""


class MongoManager:

    def __init__(self, host=os.environ["MONGODB_HOST"]):
        self.host = host
        self.client = me.connect("arenahelper", host=host)

    # Purges the old arena ladder and updates data. Stores pre-purge analytics for later usage
    def purge_ladders(self):
        pmc = pm.MongoClient(self.host, 27017)
        db = pmc['arenahelper']
        ladders = [l for l in db['pvp_ladder'].find({})]
        db['pvp_ladder'].remove({"_id": {'$in': [i['_id'] for i in ladders]}})
        if ladders:
            db['old_ladders'].insert_many(ladders)

    # Helper func
    def resolve_object(self, obj):
        result = obj.to_mongo()
        result.pop('_cls')
        for k in result:
            if k[0] in ['_', '$']:
                result.pop(k)
                continue
            attr = getattr(obj, k)
            if isinstance(attr, list):
                docs = []
                for el in attr:
                    docs.append(self.resolve_object(el))
                result[k] = docs
            elif isinstance(result[k], ObjectId):
                result[k] = self.resolve_object(getattr(obj, k))
        return result

    # Completes the document by resolving all ObjectId references into embedded documents for API calls
    def resolve_all(self, obj):
        id = obj.to_mongo()['_id']
        result = self.resolve_object(obj)
        return result

    # Gets full player data for an individual player
    def get_player(self, player_name, realm_name, resolve_refs=False):
        realm = mm.Realm.objects(name=realm_name).first()
        query = me.Q(name=player_name) & me.Q(realm=realm)
        if resolve_refs:
            player = mm.Player.objects(query).first()
            return self.resolve_all(player)
        return mm.Player.objects(query).first()

    # Updates an individual player with fresh armory data
    def update_player(self, old_id, new):
        realm = mm.Realm.objects(name=new['realm'].name).first()
        new.realm = realm
        new.player_spec.save()
        for spec in new.talents:
            if mm.ConcreteTalentTree.objects(uid=spec.uid).first() is not None:
                continue
            spec.save()
        pmc = pm.MongoClient(self.host, 27017)
        db = pmc['arenahelper']
        db.players.replace_one({"_id": old_id}, new.__dict__)

    # Inserts an object with fully formed player data for armory viewing
    def insert_player(self, player):
        realm = mm.Realm.objects(name=player['realm']).first()
        query = me.Q(name=player['name']) & me.Q(realm=realm)

        player = mm.Player.from_api_json(mm.Player(), player)
        player.player_spec.save()

        talents = []
        for spec in player.talents:
            if mm.ConcreteTalentTree.objects(uid=spec.uid).first() is not None:
                talents.append(mm.ConcreteTalentTree.objects(uid=spec.uid).first())
                continue
            spec.save()
            talents.append(spec)
        for talent in talents:
            talent.save()
        player.talents = talents

        items = []
        for item in player.items:
            q = me.Q(i_id=item.i_id) & me.Q(item_level=item.item_level)
            existing = mm.Item.objects(q).first()
            if existing is not None:
                items.append(mm.Item.objects(q).first())
                continue
            item.save()
            items.append(item)
        player.items = items
        player.realm = realm
        if self.get_player(player.name, player.realm.name) is not None:
            self.update_player(mm.Player.objects(query).first().to_mongo()['_id'], player)
            return
        player.save()

    # Populates the realm information with a json blob of all realm data
    def insert_realms(self, realms):
        if mm.Realm.objects.first():
            return
        for r in realms:
            realm = mm.Realm.from_api_json(mm.Realm(), r)
            realm.save()

    # Populates the class collection with data for a player class
    def insert_classes(self, classes):
        if mm.PlayerClass.objects.first():
            return
        for c in classes:
            cls = mm.PlayerClass.from_api_json(mm.PlayerClass(), c)
            cls.talent_trees = mm.PlayerTalentTree.objects(class_name=cls.name.lower())
            cls.save()

    # Populates the race collection with data for a player race
    def insert_races(self, races):
        if mm.PlayerRace.objects.first():
            return
        for r in races:
            race = mm.PlayerRace.from_api_json(mm.PlayerRace(), r)
            race.save()

    # Populates the ladder collection
    def insert_ladder(self, ladder):
        rows = ladder.pop('rows')
        lad = mm.PvPLadder(**ladder)
        players = [mm.PvPLadderPlayer.from_api_json(mm.PvPLadderPlayer(), row) for row in rows]
        lad.players = players
        lad.save()

    # Populates the individual talent collections
    def insert_talent(self, talent):
        talent = mm.PlayerTalent.from_api_json(mm.PlayerTalent(), talent)
        talent.save()

    # Inserts generic player talent trees, API data is wonky so the logic is bad and I should feel bad
    def insert_talent_trees(self, tree):
        try:
            spec = mm.PlayerTalentTree.from_api_json(mm.PlayerTalentTree(), tree)
            spec.spec_id = spec.order
            spec.save()
        except NotUniqueError:
            return

    # Inserts concrete player talent trees
    def insert_concrete_talent_tree(self, tree):
        spec = mm.ConcreteTalentTree.from_api_json(mm.ConcreteTalentTree(), tree)
        if spec in mm.ConcreteTalentTree.find({}).all():
            return
        spec.save()
        return spec

    # Returns a full armory player object given json with player name, realm, and locale
    def get_stored_armory_player(self, player_name, realm, locale='en_US'):
        return mm.Player.objects.first(name=player_name, realm=realm, locale=locale)

    # Inserts a new armory item into the database
    def insert_item(self, item):
        pass

