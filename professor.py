from address import Address
from servant import Servant


class Professor(Servant):
    def __init__(self, idNumber, name, address: Address, background):
        super().__init__(idNumber, name, address)
        self.__background = str(background)

    def getIdNumber(self):
        return self.__idNumber

    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def getBackground(self):
        return self.__background

    def setIdNumber(self, idNumber):
        self.__idNumber = idNumber

    def setName(self, name):
        self.__name = name

    def setAddress(self, address):
        self.__address = address

    def setBackground(self, background):
        self.__background = background
