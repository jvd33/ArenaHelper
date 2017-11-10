import mongoengine as me

"""
Abstract class for all documents, makes object instantiation easy
"""


class Doc(me.Document):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    meta = {'allow_inheritance': True, 'abstract': True}

    @staticmethod
    def map_obj(json, mappings):
        kwargs = {}
        for k, v in mappings.items():
            if v not in json.keys():
                continue
            kwargs.update({k: json[v]})
        return kwargs


"""
MongoDB Document for storing data for individual races, including icon filepaths
"""


class PlayerRace(Doc):
    race_id = me.IntField()
    mask = me.IntField()
    name = me.StringField()
    faction = me.StringField()

    meta = {'indexes': [
        {'fields': ['$name', '$faction', '$race_id']}
    ], 'collection': 'playerrace'}

    def from_api_json(self, json):
        mappings = {
            "race_id": "id",
            "mask": "mask",
            "name": "name",
            "faction": "side"
        }
        kwargs = self.map_obj(json, mappings)
        return PlayerRace(**kwargs)
"""
MongoDB Document for storing individual talent choices, including icon filepaths and descriptions
"""


class PlayerTalent(Doc):
    spell_id = me.IntField()
    name = me.StringField()
    tier = me.IntField()
    column = me.IntField()
    icon = me.StringField()
    description = me.StringField()
    cast_time = me.StringField()
    spec_name = me.StringField()
    class_name = me.StringField()

    meta = {'indexes': [
        {'fields': ['$name', '$spell_id', '$class_name']}
    ], 'collection': 'playertalent'}

    def from_api_json(self, json):
        mappings = {
            "spell_id": "id",
            "icon": "icon",
            "name": "name",
            "description": "description",
            "cast_time": "castTime",
            "tier": "tier",
            "column": "column",
            "spec_name": "spec_name",
            "class_name": "class_name"
        }
        kwargs = self.map_obj(json, mappings)
        return PlayerTalent(**kwargs)

"""
MongoDB Document for storing the talent tree information for each individual player.
"""


class PlayerTalentTree(Doc):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    spec_name = me.StringField()
    spec_description = me.StringField()
    spec_role = me.StringField()
    icon = me.StringField()
    order = me.IntField()
    talents = me.ListField(me.ReferenceField(PlayerTalent))
    class_name = me.StringField()
    spec_id = me.IntField()

    meta = {'indexes': [
        {'fields': ['$spec_name']}
    ], 'collection': 'playertalenttree', 'allow_inheritance': True}

    def from_api_json(self, json):
        mappings = {
            "spec_name": "name",
            "spec_description": "description",
            "spec_role": "role",
            "icon": "icon",
            "order": "order",
            "class_name": "class_name"
        }
        kwargs = self.map_obj(json, mappings)
        spec = PlayerTalentTree(**kwargs)
        spec.class_name = spec.class_name.replace("-", " ").lower()
        for i in range(7):
            row = []
            for j in range(3):
                query = me.Q(spec_name=spec.spec_name) & me.Q(class_name=spec.class_name) & \
                        me.Q(tier=i) & me.Q(column=j)
                row.extend(list(PlayerTalent.objects(query).all()))

            if len(row) < 3:
                cols = [el.column for el in row]
                q = me.Q(spec_name=None) & me.Q(class_name=spec.class_name) & \
                    me.Q(tier=i) & me.Q(column__nin=cols)
                result = PlayerTalent.objects(q).all()
                if result is not None:
                    row.extend(result)
            spec.talents.extend(row)
        return spec

"""
Document for storing player achievements for easy lookup
"""


class Achievement(Doc):
    a_id = me.IntField(unique=True)
    title = me.StringField()
    description = me.StringField()
    icon = me.StringField()
    criteria = me.ListField(me.IntField())

    meta = {'indexes': [
        {'fields': ['$title', '$a_id']}
    ], 'collection': 'achievement'}

    def from_api_json(self, json):
        mappings = {
            "a_id": "id",
            "title": "title",
            "description": "description",
            "icon": "icon"
        }
        kwargs = self.map_obj(json, mappings)
        return Achievement(**kwargs)
"""
Document for storing player worn items to be shown in the armory
"""


class Item(Doc):
    i_id = me.IntField()
    name = me.StringField()
    slot = me.StringField()
    item_level = me.IntField()
    icon = me.StringField()
    quality = me.IntField()

    meta = {'indexes': [
        {'fields': ['$name', '$i_id']}
    ], 'collection': 'item'}

    def from_api_json(self, json):
        mappings = {
            "i_id": "id",
            "name": "name",
            "icon": "icon",
            "quality": "quality",
            "item_level": "itemLevel",
            "slot": "slot"
        }
        kwargs = self.map_obj(json, mappings)
        return Item(**kwargs)

    @staticmethod
    def set_slot(item, slot):
        item.slot = slot
        return item

"""
MongoDB Document for storing all player classes, including icon filepaths and specialization information
"""


class PlayerClass(Doc):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if kwargs:
            self.name = kwargs['name'].lower()

    class_id = me.IntField()
    name = me.StringField()
    talent_trees = me.ListField(me.ReferenceField(PlayerTalentTree))
    mask = me.IntField()

    meta = {'indexes': [
        {'fields': ['$name', '$class_id']}
    ], 'collection': 'playerclass'}

    def from_api_json(self, json):
        mappings = {
            "class_id": "id",
            "name": "name",
            "mask": "mask",
        }
        kwargs = self.map_obj(json, mappings)
        return PlayerClass(**kwargs)

"""
MongoDB Document for storing realm data, including population and type (PvE, PvP, RP, RP-PvP)
"""


class Realm(Doc):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if kwargs:
            self.set_display_name()

    name = me.StringField()
    realm_type = me.StringField()
    battlegroup = me.StringField()
    locale = me.StringField()
    timezone = me.StringField()
    display_name = me.StringField()

    meta = {'indexes': [
        {'fields': ['$name', '$realm_type', '$battlegroup', '$locale', '$display_name']}
    ], 'collection': 'realm'}

    def set_display_name(self):
        self.display_name = "{} ({})".format(self.name, str(self.realm_type).upper().replace('V', 'v'))

    def from_api_json(self, json):
        mappings = {
            "name": "name",
            "realm_type": "type",
            "battlegroup": "battlegroup",
            "locale": "locale",
            "timezone": "timezone"
        }
        kwargs = self.map_obj(json, mappings)
        return Realm(**kwargs)

"""
Used for Players, stores all concrete talent trees used by each player for analysis
"""


class ConcreteTalentTree(Doc):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if len(kwargs.items()) > 0:
            self.uid = kwargs['calc_talent'] + kwargs['spec_name']

    spec_name = me.StringField()
    spec_description = me.StringField()
    spec_role = me.StringField()
    icon = me.StringField()
    order = me.IntField()
    talents = me.ListField(me.ReferenceField(PlayerTalent))
    class_name = me.StringField()
    spec_id = me.IntField()
    spec_order = me.StringField()
    selected = me.BooleanField()
    calc_talent = me.StringField()
    uid = me.StringField(unique=True)

    meta = {'indexes': [
        {'fields': ['$spec_name', '$spec_id']}
    ], 'collection': 'concretetalenttree', 'allow_inheritance': True}

    def from_api_json(self, json):
        mappings = {
            "spec_name": "name",
            "spec_description": "description",
            "spec_role": "role",
            "icon": "icon",
            "order": "order",
            "class_name": "class_name",
            "selected": "selected"
        }
        input_uid = json['spec']['name'] + json['calcTalent']
        existing = ConcreteTalentTree.objects(uid=input_uid).first()
        if existing:
            return existing
        kwargs = self.map_obj(json['spec'], mappings)
        kwargs.update({
            "spec_order": json['calcSpec'],
            "calc_talent": json['calcTalent'],
        })
        kwargs.update({"selected": json['selected']}) if 'selected' in json.keys() else None
        spec = ConcreteTalentTree(**kwargs)
        talents = []
        for talent in json['talents']:
            query = me.Q(spec_name=spec.spec_name)
            player_spec = PlayerTalentTree.objects(query).first()
            spec.class_name = player_spec.talents[0].class_name
            talents.extend([t for t in player_spec.talents if t.spell_id == talent['spell']['id']])

        if len(talents) < 7:
            cols = [el.column for el in talents]
            q = me.Q(spec_name=None) & me.Q(class_name=spec.class_name) & \
                me.Q(tier__nin=[t['tier'] for t in talents]) & me.Q(column__nin=cols)
            result = PlayerTalent.objects(q).all()
            if result is not None:
                talents.extend(result)

        spec.talents.extend(talents)
        player_cls = PlayerClass.objects(name=spec.class_name).first()
        spec.spec_id = player_cls.mask + spec.order
        spec.class_name = player_cls.name
        spec.uid = input_uid
        setattr(spec, "selected", None)
        return spec

"""
Reference document for containing detailed player statistic information
"""


class PlayerStatistics(me.EmbeddedDocument):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    twos_win_loss = me.DictField()
    threes_win_loss = me.DictField()
    rbg_win_loss = me.DictField()
    twos_rating = me.IntField()
    threes_rating = me.IntField()
    rbg_rating = me.IntField()
    hks = me.IntField()
    arena_hks = me.IntField()
    bg_hks = me.IntField()
    achievement_points = me.IntField()
    bgs_won = me.IntField()
    bgs_played = me.IntField()
    rbgs_won = me.IntField()
    rbgs_played = me.IntField()
    arenas_won = me.IntField()
    arenas_played = me.IntField()
    arena_breakdown = me.DictField()  # Breaks down the win/loss ratio of certain arena maps
    high_2s = me.IntField()
    high_3s = me.IntField()
    high_5s = me.IntField()
    duels_won = me.IntField()
    duels_lost = me.IntField()

    meta = {'collection': 'playerstatistics'}

    def from_api_json(self, json):
        mappings = {
            "twos_rating": "twos_rating",
            "threes_rating": "threes_rating",
            "rbg_rating": "rbg_rating",

        }
        kwargs = Doc.map_obj(json, mappings)
        return PlayerStatistics(**kwargs)

"""
MongoDB Document containing detailed player information, used for armory pages
"""


class Player(Doc):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if kwargs:
            genders = ["Male", "Female"]
            self.faction = "alliance" if kwargs['faction'] == 0 else "horde"
            if self.player_gender not in genders:
                self.player_gender = "Male" if kwargs['player_gender'] == 0 else 'Female'

    @staticmethod
    def mappings():
        return {
            "name": "name",
            "level": "level",
            "achievement_points": "achievementPoints",
            "icon": "thumbnail",
            "player_gender": "gender",
            "faction": "faction"
        }

    name = me.StringField()
    realm = me.ReferenceField(Realm)
    player_class = me.ReferenceField(PlayerClass)
    player_spec = me.ReferenceField(ConcreteTalentTree)
    player_gender = me.StringField()
    faction = me.StringField()
    achievements = me.ListField(me.ReferenceField(Achievement))
    guild = me.StringField()
    items = me.ListField(me.ReferenceField(Item))
    statistics = me.EmbeddedDocumentField(PlayerStatistics)
    professions = me.DictField()
    talents = me.ListField(me.ReferenceField(ConcreteTalentTree))
    title = me.StringField()
    achievement_points = me.IntField()
    race = me.ReferenceField(PlayerRace)
    level = me.IntField()
    icon = me.StringField()
    display_name = me.StringField()
    ilvl = me.IntField()
    equipped_ilvl = me.IntField()

    meta = {'indexes': [
        {'fields': ['$name', '$realm', '$player_class', '$player_spec', '$faction', '$faction', '$race']}
    ], 'collection': 'player', 'allow_inheritance': True}

    def from_api_json(self, json):
        kwargs = self.map_obj(json, self.mappings())
        player = Player(**kwargs)
        player.race = PlayerRace.objects(race_id=json['race']).first()
        player.player_class = PlayerClass.objects(class_id=json['class']).first()
        player.talents = [ConcreteTalentTree.from_api_json(ConcreteTalentTree(), obj) for obj in json['talents']
                          if 'talents' in obj.keys() and len(obj['talents']) > 0]
        player.player_spec = [ConcreteTalentTree.from_api_json(ConcreteTalentTree(), obj) for obj in json['talents']
                              if 'selected' in obj.keys()][0]
        player.guild = json['guild']['name'] if 'guild' in json.keys() else ""
        profs = {}
        if 'professions' in json.keys():
            if 'primary' in json['professions'].keys():
                for prof in json['professions']['primary']:
                    profs.update({prof['name']: prof['rank']})
        for title in json['titles']:
            player.title = title['name'] % player.name if 'selected' in title.keys() else "%s" % player.name
        player.professions = profs
        player.ilvl = json['items'].pop("averageItemLevel")
        player.equipped_ilvl = json['items'].pop("averageItemLevelEquipped")
        player.items = [Item.set_slot(Item.from_api_json(Item(), json['items'][obj]), obj) for obj in json['items']]
        return player

"""
Embedded Document for storing PvP ladder ranking data
"""


class PvPLadderPlayer(me.EmbeddedDocument):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    rank = me.IntField()
    rating = me.IntField()
    name = me.StringField()
    realm_name = me.StringField()
    race_id = me.IntField()
    class_id = me.IntField()
    spec_id = me.IntField()
    faction = me.StringField()
    season_wins = me.IntField()
    season_losses = me.IntField()
    weekly_wins = me.IntField()
    weekly_losses = me.IntField()

    def from_api_json(self, json):
        mappings = {
            "rank": "ranking",
            "rating": "rating",
            "name": "name",
            "realm_name": "realmName",
            "race_id": "raceId",
            "class_id": "classId",
            "spec_id": "specId",
            "season_wins": "seasonWins",
            "season_losses": "seasonLosses",
            "weekly_wins": "weeklyWins",
            "weekly_losses": "weeklyLosses"
        }
        kwargs = Doc.map_obj(json, mappings)
        return PvPLadderPlayer(**kwargs)

""""
MongoDB Document that stores all the players in the arena ladder ordered by some rank
"""


class PvPLadder(Doc):
    bracket = me.StringField()
    locale = me.StringField()
    page = me.IntField()
    per_page = me.IntField()
    next_page = me.IntField()
    players = me.EmbeddedDocumentListField(PvPLadderPlayer)
    fetch_date = me.DateTimeField()

    meta = {'indexes': [
        {'fields': ['$bracket', '$locale']}
        ], 'collection': 'pvpladder'}



