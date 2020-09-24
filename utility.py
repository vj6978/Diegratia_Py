import pymongo
import config

class Utility:
    def saveToMongo(self, tbName, **kwargs):
        client = pymongo.MongoClient(config._URI)
        Database = client.get_database(config._db_string)
        result = Database[tbName].insert_one(kwargs)