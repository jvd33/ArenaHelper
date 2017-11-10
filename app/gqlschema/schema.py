from gqlschema.models import Player, PvPLadder, construct, PvPLadderPlayer
import graphene as gql
from mongo import db

mongodb = db.MongoManager()


class Query(gql.ObjectType):
    player = gql.Field(Player, name=gql.String(), realm=gql.String())
    ladder = gql.Field(PvPLadder, bracket=gql.String(), page=gql.Int())

    def resolve_player(self, info, name, realm):
        return mongodb.get_player(name, realm)

    def resolve_ladder(self, info, bracket, page=1):
        mongoladder = mongodb.get_ladder(bracket, page)
        ladder = construct(PvPLadder, mongoladder)
        players = []
        for player in mongoladder['players']:
            p = construct(PvPLadderPlayer, player)
            p.faction = mongodb.get_player_faction(p.name, p.realm_name)
            players.append(p)
        ladder.players = players
        return ladder


schema = gql.Schema(query=Query)

