from gqlschema.models import Player, PvPLadder, construct
import graphene as gql
from mongo import db

mongodb = db.MongoManager()


class Query(gql.ObjectType):
    player = gql.Field(Player, name=gql.String(), realm=gql.String())
    ladder = gql.Field(PvPLadder, bracket=gql.String())

    def resolve_player(self, info, name, realm):
        return mongodb.get_player(name, realm)

    def resolve_ladder(self, info, bracket):
        pass

schema = gql.Schema(query=Query)

