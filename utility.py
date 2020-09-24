import pymongo
import config

class Utility:
    """
    :parameter tbName table Name to which data should be saved.
    """
    def saveToMongo(self, **kwargs):
        client = pymongo.MongoClient(config._URI)
        Database = client.get_database(config._db_string)
        Database[config._tbName].insert_one(kwargs)