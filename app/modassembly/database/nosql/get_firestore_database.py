import os

from google.cloud import firestore


_database = None
FIRESTORE_DB = os.environ["FIRESTORE_DB"]


def get_firestore_database() -> firestore.Client:
    global _database
    if _database is None:
        _database = firestore.Client(database=FIRESTORE_DB)
    return _database
