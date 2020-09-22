import uuid
from Box import Box

"""
    Driver class
    Manages the lifecycle of the Box
"""
class Driver:
    def __init__(self):
        self.deviceId = uuid.uuid4()
        self.box = Box(self.deviceId)
        self.boxBreach = False
        self.initialConfiguration = False

    def open(self):
        if not self.initialConfiguration:
            self.startMonitoringBreach()
        self.box.onBreach()

    def startMonitoringBreach(self):
        print("Initializing Box With Device ID : {}".format(self.deviceId))
        print("Powering On and calling initialConfiguration method")
        self.box.onInitialConfiguration()
        self.initialConfiguration = True

    def deactivate(self):
        self.initialConfiguration = False
        self.box.onDeactivation()

driver = Driver()