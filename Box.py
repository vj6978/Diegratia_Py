import uuid
import datetime
import threading
from BreachProtocol import BreachProtocol
from Contract import BoxContract
from DeactivationService import DeactivationService

"""
    Box lifecycle methods declared. 
    Define any extra methods here.
"""
class Box(BoxContract.Contract):
    def __init__(self):
        self.__deviceId = uuid.uuid4()
        self.__initialConfigComplete = False
        self.event = threading.Event()
        self.breachProtocol = BreachProtocol(self.__deviceId, self.event)
        self.deactivationService = DeactivationService(self.event)

    @property
    def initialConfigComplete(self):
        return self.__initialConfigComplete

    @initialConfigComplete.setter
    def initialConfigComplete(self, initialConfigComplete):
        self.__initialConfigComplete = initialConfigComplete

    """
        Callbacks Functions
        -------------------
    """
    def onInitialConfiguration(self) -> None:
        #Add your code
        self.__initialConfigComplete = True
        print("Initial configuration for box - {} completed at : {}".format(self.__deviceId, datetime.datetime.now()))

    # TODO: Action to perform when box is breached. Remove Deactivate Parameter
    def onBreach(self) -> None:
        #Don't change this function
        print("Box has been breached!")
        self.deactivationService.start()
        self.breachProtocol.start()
        pass

    def onDeactivation(self) -> None:
        print("Deactivation Protocol Initiated!")
        # Add your code
        self.__initialConfigComplete = False
        self.onCleanUp()

    def onNetworkLoss(self) -> None:
        print("Network loss detected!")
        # Add your code
        pass

    def onCleanUp(self) -> None:
        print("Initiating Clean Up Sequence")
        # Add your code
        pass