import threading
from utility import Utility

class BreachProtocol(threading.Thread):
    def __init__(self, deviceId, event):
        threading.Thread.__init__(self)
        self.__deviceId = deviceId
        self.event = event
        self.utility = Utility()

    """
        Code to capture images and other required breach events.
        Spawn threads as required.
    """
    def run(self):
        print("Initiating Breach Protocol! Starting 30 second timer to wait for deactivation message")
        while not self.event.isSet():
            print("Running required processes related breach.")
            #TODO: In order to reduce the amount of data being sent to server, take measures such as sending coordintes only if they change, etc.
            # dummyData = {"deviceId": str(self.__deviceId), "x": "100", "y": "200", "z": "300"}
            # self.utility.saveToMongo(**dummyData)

