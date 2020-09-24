import threading
from utility import Utility

class BreachProtocol(threading.Thread):
    def __init__(self, deviceId):
        threading.Thread.__init__(self)
        self.__deviceId = deviceId
        self.utility = Utility()

    """
        Code to capture images and other required breach events
    """
    def run(self):
        print("Initiating Breach Protocol. Saving GPS location in db")
        dummyData = {"deviceId": str(self.__deviceId), "x": "100", "y": "200", "z": "300"}
        self.utility.saveToMongo("LocationTable", **dummyData)

