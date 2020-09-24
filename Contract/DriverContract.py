from abc import ABC, abstractmethod

"""
    Driver defines the lifecycle that drives the entire program and invokes the methdos of the box. 
    The Driver class should follow this contract.
"""
class Contract(ABC):
    @abstractmethod
    def startInitialConfiguration(self) -> None:
        pass

    @abstractmethod
    def open(self) -> None:
        pass