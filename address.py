class Address:
    def __init__(self, street, number, city, state, country):
        self.__street = str(street)
        self.__number = int(number)
        self.__city = str(city)
        self.__state = str(state)
        self.__country = str(country)

    def getStreet(self):
        return self.__street

    def getNumber(self):
        return self.__number

    def getCity(self):
        return self.__city

    def getState(self):
        return self.__state

    def getCountry(self):
        return self.__country

    def setStreet(self, street: str):
        self.__street = street

    def setNumber(self, number: int):
        self.__number = number

    def setCity(self, city: str):
        self.__city = city

    def setState(self, state: str):
        self.__state = state

    def setCountry(self, country: str):
        self.__country = country

    def __str__(self):
        return (f'Street name: {self.getStreet()} - Street number: {self.getNumber()}\n'
                f'City: {self.getCity()} - State: {self.getState()} - Country: {self.getCountry()}')
