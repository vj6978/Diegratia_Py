from abc import ABC, abstractmethod

"""
    This abstract class defines the contract laying out the lifecycle for each box.
"""

class BoxContract(ABC):
    """
        Initial Box Configuration logic
    """
    @abstractmethod
    def intialConfiguration(self):
        pass

    """
        Box is Opened Illegaly logic
    """
    @abstractmethod
    def illegalBoxOpen(self):
        pass
