from abc import ABC, abstractmethod

"""
    This abstract class defines the contract laying out the lifecycle for each box.
"""

class Contract(ABC):

    """
        Initial Box Conig Logic
    """
    @abstractmethod
    def intialConfiguration(self):
        pass

    """
        Box is Opened Illegaly logic
    """
    @abstractmethod
    def boxBreached(self):
        pass

    """
        Box Deactivation Logic
    """
    @abstractmethod
    def deactivate(self):
        pass

    """
        Box Was Never Breached. Reboot. Config after inital
    """
    @abstractmethod
    def reboot(self):
        pass
