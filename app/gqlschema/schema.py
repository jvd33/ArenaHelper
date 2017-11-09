from app.gqlschema.models import *
import graphene as gql
from app.mongo import db

mongodb = db.MongoManager()


class Query(gql.ObjectType):
    player = gql.Field(Player, name=gql.String(), realm=gql.String())
    ladder = gql.Field(PvPLadder, bracket=gql.String())

    def resolve_player(self, info, name, realm):
        return construct(Player, mongodb.get_player(name, realm))

schema = gql.Schema(query=Query)
