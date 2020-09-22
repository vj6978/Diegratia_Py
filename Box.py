import datetime
from Contract import BoxContract

"""
    Box lifecycle methods declared. 
    Define any extra methods here.
"""
class Box(BoxContract.Contract):

    def __init__(self, deviceId):
        self.deviceId = deviceId
        self.boxBreached = False
        self.numOfTimesBoxOpened = 0

    def onInitialConfiguration(self):
        print("Box - {} - Configuration Complete At : {}".format(self.deviceId, datetime.datetime.now()))

    # TODO: Action to perform when box is breached.
    def onBreach(self):
        print("Box has been breached!")
        pass

    def onDeactivation(self):
        print("Deactivation Protocol Initiated!")
        pass

    def onNetworkLoss(self):
        print("Network loss detected!")
        pass