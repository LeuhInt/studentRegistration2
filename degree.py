class Degree:
    def __init__(self, code, name, duration):
        self.__code = int(code)
        self.__name = str(name)
        self.__duration = int(duration)

    def getCode(self):
        return self.__code

    def getName(self):
        return self.__name

    def getDuration(self):
        return self.__duration

    def setCode(self, code: int):
        self.__code = code

    def setName(self, name: str):
        self.__name = name

    def setDuration(self, duration: int):
        self.__duration = duration

    def __str__(self):
        return (f'Degree code: {self.getCode()}\n'
                f'Degree name: {self.getName()}\n'
                f'Degree duration: {self.getDuration()}h')
