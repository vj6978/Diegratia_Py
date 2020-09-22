from abc import ABC, abstractmethod

"""
    This abstract class defines the contract laying out the lifecycle for each box.
"""

class Contract(ABC):

    """
        Initial Box Conig Logic
    """
    @abstractmethod
    def onInitialConfiguration(self):
        pass

    """
        Box is Breached
    """
    @abstractmethod
    def onBreach(self):
        pass

    """
        Box Deactivation Logic
    """
    @abstractmethod
    def onDeactivation(self):
        pass

    """
        Box loses network connectivity.
    """
    @abstractmethod
    def onNetworkLoss(self):
        pass
