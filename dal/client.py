"""
Create client to connect MongoDB
"""


from pymongo.mongo_client import MongoClient


def client(uri) -> MongoClient:
    """Create client to connect cluster"""
    client = MongoClient(uri)
    try:
        client.admin.command("ping")
        print("Connected to MongoDB!")
    except Exception as e:
        raise Exception(f'__client error: {e}')
    return client


def __database(client: MongoClient):
    """Get database from claster"""
    try:
        db = client["ServiceMD"]
    except Exception as e:
        raise Exception(f'__database error: {e}')

    return db


def __collection(db):
    """Get collection from database"""
    try:
        collection = db['MetaData']
    except Exception as e:
        raise Exception(f'__collection error: {e}')
    return collection


def get_collection(client: MongoClient):
    db = __database(client)
    return __collection(db)
