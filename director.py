from address import Address
from professor import Professor


class Director(Professor):
    def __init__(self, idNumber, name, address: Address, background):
        super().__init__(idNumber, name, address, background)
