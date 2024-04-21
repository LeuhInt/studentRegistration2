from abc import ABC, abstractmethod
from address import Address


class Servant(ABC):
    def __init__(self, idNumber, name, address: Address):
        self.__idNumber = int(idNumber)
        self.__name = str(name)
        self.__address = address

    @abstractmethod
    def getIdNumber(self):
        pass

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getAddress(self):
        pass

    @abstractmethod
    def setIdNumber(self, idNumber):
        pass

    @abstractmethod
    def setName(self, name):
        pass

    @abstractmethod
    def setAddress(self, address):
        pass
