from address import Address
from professor import Professor


class Coordinator(Professor):
    def __init__(self, idNumber, name, address: Address, background):
        Professor.__init__(self, idNumber, name, address, background)
