import uuid
import datetime
from BreachProtocol import BreachProtocol
from Contract import BoxContract

"""
    Box lifecycle methods declared. 
    Define any extra methods here.
"""
class Box(BoxContract.Contract):

    def __init__(self):
        self.__deviceId = uuid.uuid4()
        self.__initialConfigComplete = False
        self.breachProtocol = BreachProtocol()
        self.breachProtocol.setDaemon(True)

    @property
    def initialConfigComplete(self):
        return self.__initialConfigComplete

    @initialConfigComplete.setter
    def initialConfigComplete(self, initialConfigComplete):
        self.__initialConfigComplete = initialConfigComplete

    def onInitialConfiguration(self) -> None:
        print("Initial configuration for box - {} completed at : {}".format(self.__deviceId, datetime.datetime.now()))
        self.__initialConfigComplete = True

    # TODO: Action to perform when box is breached. Remove Deactivate Parameter
    def onBreach(self) -> None:
        print("Box has been breached!")
        self.breachProtocol.start()
        pass

    def onDeactivation(self) -> None:
        print("Deactivation Protocol Initiated!")
        self.__initialConfigComplete = False
        self.onCleanUp()

    def onNetworkLoss(self) -> None:
        print("Network loss detected!")
        pass

    def onCleanUp(self) -> None:
        print("Initiating Clean Up Sequence")
        pass