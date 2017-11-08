import graphene as gql


"""
GraphQL models from the DB, same as the mongdb models for the most part
"""


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

class TalentTree(gql.ObjectType):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

