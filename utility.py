import pymongo
import requests
from . import config

class Utility:
    def json(self, **kwargs):
        return {
            "device_no": self.device_no,
            "status": self.status,
            "msg": self.msg,
            "number_of_times_box_was_opened": str(self.num_of_times_box_opened),
            "condition_of_the_box": self.condition_of_the_box
        }

    def save_to_mongo(self, **kwargs):
        client = pymongo.MongoClient(config._URI)
        Database = client[config._db_string]
        Database["sb" + self.device_no].insert(self.json())
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        pload = self.json()
        r = requests.post(url="https://cargodiegratia.herokuapp.com/api/new", json=pload, headers=headers)
        print("Response is: %s" % r.text)