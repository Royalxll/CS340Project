from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, username, password):
        # Connection Variables
        USER = username
        PASS = password
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        # Initialize Connection
        self.client = MongoClient(
        'mongodb://%s:%s@%s:%d/?authSource=admin' % (USER, PASS, HOST, PORT)
        )

        self.database = self.client[DB]
        self.collection = self.database[COL]
    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        """Insert a document into the animals collection."""
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print("Error inserting document:", e)
                return False
        else:
            return False

    # Create method to implement the R in CRUD.
    def read(self, query):
        """Find and return documents from the animals collection."""
        if query is not None:
            try:
                result = self.collection.find(query)
                return list(result)
            except Exception as e:
                print("Error reading documents:", e)
                return []
        else:
            return []
    
        # Update method to implement the U in CRUD.
    def update(self, query, data):
        """Update documents in the animals collection."""
        if query is not None and data is not None:
            try:
                result = self.collection.update_many(
                    query,
                    {"$set": data}
                )
                return result.modified_count
            except Exception as e:
                print("Error updating documents:", e)
                return 0
        else:
            return 0

    # Delete method to implement the D in CRUD.
    def delete(self, query):
        """Delete documents from the animals collection."""
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print("Error deleting documents:", e)
                return 0
        else:
            return 0