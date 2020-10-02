import time
import threading
import config
from utility import Utility
from PiCameraUtility import PiCameraUtility

class BreachProtocol(threading.Thread):
    def __init__(self, deviceId, event):
        threading.Thread.__init__(self)
        self.__deviceId = deviceId
        self.event = event
        self.utility = Utility()
        self.camera = PiCameraUtility(self.__deviceId)

    """
        Code to capture images and other required breach events.
        Spawn threads as required.
    """
    def run(self):
        print("Initiating Breach Protocol! Starting 30 second timer to wait for deactivation message")
        while not self.event.isSet():
            self.camera.snap()
            time.sleep(config.IMAGE_CAPTURE_DELAY)
        else:
            print("Deactivation Message Reached")