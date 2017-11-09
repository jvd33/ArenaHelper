import graphene as gql
from graphene.types.datetime import DateTime

"""
GraphQL models from the DB, same as the mongdb models for the most part
"""


def construct(object_type, doc):
    field_names = [f for f in object_type._meta.fields]
    kwargs = {attr: val for attr, val in doc.items()
            if attr in field_names}
    return object_type(**kwargs)


class Race(gql.ObjectType):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    race_id = gql.Int()
    mask = gql.Int()
    name = gql.String()
    faction = gql.String()


class Talent(gql.ObjectType):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    spell_id = gql.Int()
    name = gql.Int()
    tier = gql.Int()
    column = gql.Int()
    icon = gql.String()
    description = gql.String()
    spec_name = gql.String()
    class_name = gql.String()


class Item(gql.ObjectType):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    i_id = gql.Int()
    name = gql.String()
    slot = gql.String()
    item_level = gql.Int()
    icon = gql.Int()


class PlayerClass(gql.ObjectType):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    class_id = gql.Int()
    name = gql.String()
    mask = gql.Int()


class TalentTree(gql.ObjectType):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    _id = gql.String()
    spec_name = gql.String()
    spec_description = gql.String()
    spec_role = gql.String()
    icon = gql.String()
    order = gql.String()
    talents = gql.List(gql.Field(Talent))
    class_name = gql.String()
    spec_id = gql.Int()
    spec_order = gql.String()
    selected = gql.Boolean()
    calc_talent = gql.String()
    uid = gql.String()


class Realm(gql.ObjectType):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    name = gql.String()
    realm_type = gql.String()
    battlegroup = gql.String()
    timezone = gql.String()
    display_name = gql.String()


class Player(gql.ObjectType):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    name = gql.String()
    realm = gql.Field(Realm)
    player_class = gql.Field(PlayerClass)
    player_spec = gql.Field(TalentTree)
    player_gender = gql.String()
    faction = gql.String()
    guild = gql.String()
    items = gql.List(gql.Field(Item))
    professions = gql.JSONString()
    talents = gql.List(gql.Field(TalentTree))
    title = gql.String()
    achievement_points = gql.Int()
    race = gql.Field(Race)
    level = gql.Int()
    icon = gql.String()
    display_name = gql.String()
    ilvl = gql.Int()
    equipped_ilvl = gql.Int()


class PvPLadderPlayer(gql.ObjectType):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    rank = gql.Int()
    rating = gql.Int()
    name = gql.String()
    realm_name = gql.String()
    race_id = gql.Int()
    class_id = gql.Int()
    spec_id = gql.Int()
    faction = gql.String()
    season_wins = gql.Int()
    season_losses = gql.Int()
    weekly_wins = gql.Int()
    weekly_losses = gql.Int()


class PvPLadder(gql.ObjectType):
    bracket = gql.String()
    page = gql.Int()
    per_page = gql.Int()
    player = gql.List(gql.Field(PvPLadderPlayer))
    fetch_date = DateTime()