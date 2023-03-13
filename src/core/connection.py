from pymongo import MongoClient

from .config import settings


def create_mongo_client() -> MongoClient:
    """Create a new client to the Mongo database"""

    client = MongoClient(settings.DATABASE_URI)
    return client
