from degree import Degree
from student import Student
from course import Course
from address import Address
from lectureHall import LectureHall
from professor import Professor


class Notebook:

    def __init__(self):
        self.studentDict = {}
        self.degreeDict = {}
        self.courseDict = {}
        self.lectureHallDict = {}
        self.addressDict = {}
        self.professorDict = {}

    def addStudent(self):
        idNumber = str(input('Enter the Student ID Number: '))
        name = str(input('Enter the Student Name: '))
        address = self.addAddress()
        degree = self.addDegree()
        course = self.addCourse()
        oStudent = Student(idNumber, name, degree, address, course)
        self.studentDict[idNumber] = oStudent
        return oStudent

    def addDegree(self):
        code = int(input('Enter the Degree Code: '))
        name = str(input('Enter the Degree Name: '))
        duration = int(input('Enter the Degree Duration: '))
        oDegree = Degree(code, name, duration)
        self.degreeDict[code] = oDegree
        return oDegree

    def addCourse(self):
        code = int(input('Enter the Course Code: '))
        name = str(input('Enter the Course Name: '))
        semester = int(input('Enter the Course Semester: '))
        requisites = str(input('Enter the Course Requisites: '))
        contactHours = int(input('Enter the Course Contact Hours: '))
        oProfessor = self.addProfessor()
        oLectureHall = self.addLectureHall()
        oCourse = Course(code, name, semester, requisites, contactHours, oProfessor, oLectureHall)
        self.courseDict[code] = oCourse
        return oCourse

    def addLectureHall(self):
        name = str(input('Enter the Lecture Hall Name: '))
        seats = int(input('Enter the Lecture Hall Seats: '))
        oLectureHall = LectureHall(name, seats)
        self.lectureHallDict[name] = oLectureHall
        return oLectureHall

    def addAddress(self):
        street = str(input('Enter the Street Address: '))
        number = int(input('Enter the Street Number: '))
        city = str(input('Enter the City: '))
        state = str(input('Enter the State: '))
        country = str(input('Enter the Country: '))
        oAddress = Address(street, number, city, state, country)
        self.addressDict[street] = oAddress
        return oAddress

    def addProfessor(self):
        idNumber = int(input('Enter the Professor ID Number: '))
        name = str(input('Enter the Professor Name: '))
        background = str(input('Enter the Professor Background: '))
        address = self.addAddress()
        oProfessor = Professor(idNumber, name, address, background)
        self.professorDict[idNumber] = oProfessor
        return oProfessor

    def listStudents(self):
        print(self.studentDict)

    def listLectureHalls(self):
        print('Lecture Halls:')
        for k in self.lectureHallDict:
            print(self.lectureHallDict[k])

    # def degreeList():
    #     degrees = {
    #         1: ['Computer Science', 3200],
    #         2: ['Software Engineering', 3500],
    #         3: ['System Information Technology', 3100]
    #     }
    #     return degrees
    #
    # def courseList():
    #     courses = {
    #         1: ['Maths I', 1, 'no requisites', 60, 'John', 'Bloco I sala 10'],
    #         2: ['Maths II', 1, 'Maths I', 60, 'Mary', 'Bloco I sala 12'],
    #         3: ['Programming Languages I', 1, 'no requisites', 60, 'Joseph', 'Bloco I sala 13'],
    #         4: ['Programming Languages II', 2, 'Programming Languages I', 60, 'Stuart', 'Bloco II sala 10'],
    #         5: ['Software Engineering I', 1, 'no requisites', 60, 'Max', 'Bloco II sala 15'],
    #         6: ['Software Engineering II', 2, 'Software Engineering I', 60, 'John', 'Bloco I sala 5'],
    #         7: ['Hardware Engineering I', 1, 'no requisites', 60, 'Ellis', 'Bloco II sala 14'],
    #         8: ['Hardware Engineering II', 2, 'Hardware Engineering I', 60, 'Clair', 'Bloco III sala 9'],
    #     }
    #     return courses

    # def printFormat(data):
    #     for key, value in data.items():
    #         print(f'{key}: Degree: {value[0]}, Duration: {value[1]}')
