from abc import ABC, abstractmethod

"""
    This abstract class defines the contract laying out the lifecycle for each box.
"""

class Contract(ABC):

    """
        Initial Box Conig Logic
    """
    @abstractmethod
    def onInitialConfiguration(self) -> None:
        pass

    """
        Box is Breached
    """
    @abstractmethod
    def onBreach(self) -> None:
        pass

    """
        Box Deactivation Logic
    """
    @abstractmethod
    def onDeactivation(self) -> None:
        pass

    """
        Box loses network connectivity.
    """
    @abstractmethod
    def onNetworkLoss(self) -> None:
        pass

    """
        Box clean up activities after deactivation
    """
    @abstractmethod
    def onCleanUp(self) -> None:
        pass
