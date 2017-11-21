from api.data_client import DataClient
from gqlschema import schema
from api.arena_client import ArenaClient
from jobs.startup import StartupJob
from mongo.db import MongoManager
from flask import Flask
from flask_graphql import GraphQLView
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema.schema,
        graphiql=True
    )
)


if __name__ == "__main__":

    startup = StartupJob()
    db = MongoManager()
    #startup.seed()
    print(dict(db.get_player("Aviro", "Thrall", True)))
    app.run(host='0.0.0.0', port=4000)
    # startup.seed()
