import pymongo
import config

class Utility:
    """
            Save To Mongo Utility

            dummyData = {"deviceId": str(self.__deviceId), "x": "100", "y": "200", "z": "300"}
            self.utility.saveToMongo(**dummyData)
        """
    def saveToMongo(self, **kwargs):
        client = pymongo.MongoClient(config._URI)
        Database = client.get_database(config._db_string)
        Database[config._tbName].insert_one(kwargs)