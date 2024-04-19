from degree import Degree
from lectureHall import LectureHall
from professor import Professor
from student import Student
from address import Address
from course import Course
from menu import Menu


# class Main:
#     def __init__(self):
#         oDegree = Degree(111, 'Computer Science', 3200)
#         oLectureHall = LectureHall('Bloco 2, sala 14', 40)
#         oAddressStudent = Address('Avenida San Francisco', 23, 'Serra Talhada', 'Pernambuco', 'Brasil')
#         oAddressProfessor = Address('Travessa João Carlos', 55, 'Triunfo', 'Pernambuco', 'Brasil')
#         oProfessor = Professor(222, 'John Stuart', oAddressProfessor, 'Software Engineer')
#         oCourse = Course(333, 'Machine Learning', 2, 'Maths', 60, oProfessor, oLectureHall)
#         oStudent = Student(1, 'Leuh', oDegree, oAddressStudent, oCourse)
#
#         # oAddress = Address
#         # oStudent.setAddress(oAddress)
#         oStudent.setName("Leuh")
#         oStudent.getAddress().setCity("Santa")
#         print(oStudent.getName())
#         print(oStudent.getAddress().getCity())
#
#
# Main()

Menu().run()
