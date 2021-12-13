import os

import pymongo


def get_mongo_client():
    """Get correct mongo client
    Returns:
        pymongo.database.Database -- client that points to db
    """
    mongo_client = pymongo.MongoClient(os.environ['MONGO_CLIENT'])
    return mongo_client['bfxfee']

