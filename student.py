from degree import Degree
from address import Address
from course import Course
from course import Professor


class Student:
    def __init__(self, idNumber, name, degree: Degree, address: Address, course: Course):
        self.__idNumber = int(idNumber)
        self.__name = str(name)
        self.__degree = degree
        self.__address = address
        self.__course = course

    def getIdNumber(self):
        return self.__idNumber

    def getName(self) -> str:
        return self.__name

    def getDegree(self):
        return self.__degree

    def getAddress(self):
        return self.__address

    def getCourse(self):
        return self.__course

    def setIdNumber(self, idNumber: int):
        self.__idNumber = idNumber

    def setName(self, name: str):
        self.__name = name

    def setDegree(self, degree):
        self.__degree = degree

    def setAddress(self, address):
        self.__address = address

    def setCourse(self, course):
        self.__course = course

    def __str__(self):
        return (f'{'ENROLLMENT':^60}\n'
                f'{'-' * 60}\n'
                f'{'STUDENT INFORMATION':^30}\n'
                f'{'-' * 60}\n'
                f'ID Number: {self.__idNumber}\n'
                f'Student name: {self.__name} \n'
                f'Address: {self.__address} \n'
                f'{'-' * 60}\n'
                f'{'DEGREE INFORMATION':^30}\n'
                f'{'-' * 60}\n'
                f'{self.__degree}\n'
                f'{'-' * 60}\n'
                f'{'COURSE INFORMATION':^30}\n'
                f'{'-' * 60}\n'
                f'Course code: {self.__course.getCode()}\n'
                f'Course semester: {self.__course.getSemester()}º\n'
                f'Course name: {self.__course.getName()}\n'
                f'Course duration: {self.__course.getContactHours()}h\n'
                f'Requisites: {self.__course.getRequisites()}\n'
                f'Professor name: {self.__course.getProfessor().getName()}\n'
                f'Lecture Hall: {self.__course.getLectureHall()}\n')
