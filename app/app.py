from api.data_client import DataClient
from api.arena_client import ArenaClient
import gqlschema.schema as schema
from jobs.startup import StartupJob
from mongo.db import MongoManager
from flask import Flask
from flask_graphql import GraphQLView


app = Flask(__name__)
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
    print(db.get_player("Aviro", "Thrall", True))
    app.run(host='0.0.0.0', port=4000)
    # startup.seed()
