from Box import Box
from Contract import DriverContract

"""
    Driver class
    Manages the lifecycle of the Box
"""
class Driver(DriverContract.Contract):
    def __init__(self):
        self.box = Box()
        self.DEACTIVATION_MESSAGE_EXPECTED_IN = 30

    def startInitialConfiguration(self):
        self.box.onInitialConfiguration()

    """
        Callback method
        
        Interface logic with processor or controller to determine when a box is open. Run it in loop.
        deactivate parameter should be removed. For Simulation only.
        On a separate thread, wait and see if deactivation message is received within stipulated time.
        If no, continue breach protocol.
        If yes, start deactivation protocol. 
    """
    def open(self, deactivate = False):

        if self.box.initialConfigComplete:
            if deactivate:
                self.box.onDeactivation()
            else:
                self.box.onBreach()
        else:
            self.startInitialConfiguration()