from student import Student
# from notebook import degreeList, courseList, printFormat
from address import Address
from degree import Degree
from course import Course
from notebook import Notebook


class Menu:
    def __init__(self):
        self.choices = {
            1: Notebook().addStudent(),
            2: 'self.addDegree',
            3: 'Add Degree',
            4: 'Add Course',
            5: 'Add Lecture Hall',
            6: 'Exit',
        }

    def displayMenu(self):
        print(f'''Education System
        {'=' * 30}
        1. Add Student
        2. Add Professor
        3. Add Degree
        4. Add Course
        5. Add Lecture Hall
        6. Exit
        {'=' * 30}''')

    def run(self):
        while True:
            self.displayMenu()
            try:
                choice = int(input('Enter your choice: '))
                if choice in self.choices:
                    action = self.choices[choice]
                    if callable(action):
                        action()
                    else:
                        print('Invalid choice')
                else:
                    print('Invalid choice')
            except ValueError:
                print('Invalid input. Please enter an integer')


    # def addStudent(self):
    #     print(f'Student Enrollment\n'
    #           f'{'=' * 30}')
    #     idNumber = int(input('Student ID: '))
    #     nameStu = input('Student Name: ')
    #     print(f'Student Address\n'
    #           f'{'=' * 30}')
    #     street = input('Street name: ')
    #     number = int(input('Number: '))
    #     city = input('City: ')
    #     state = input('State: ')
    #     country = input('Country: ')
    #     oAddress = Address(street, number, city, state, country)
    #     print(f'Student Degree\n'
    #           f'{'=' * 30}')
    #     print(f'Available Degrees:\n')
    #     printFormat(degreeList())
    #     degree_option = int(input('Choice a Degree: '))
    #     code = degree_option
    #     name = degreeList()[degree_option][0]
    #     duration = degreeList()[degree_option][1]
    #     oDegree = Degree(code, name, duration)
    #     print(f'Student Courses\n'
    #           f'{'=' * 30}')
    #     print(f'Available Courses:\n')
    #     printFormat(courseList())
    #     course_option = int(input('Choice a Course: '))
    #     code = course_option
    #     name = courseList()[course_option][0]
    #     semester = courseList()[course_option][1]
    #     requisites = courseList()[course_option][2]
    #     contactHours = courseList()[course_option][3]
    #     professor = courseList()[course_option][4]
    #     lectureHall = courseList()[course_option][5]
    #     oCourse = Course(code, name, semester, requisites, contactHours, professor, lectureHall)
    #     oStudent = Student(idNumber, nameStu, oDegree, oAddress, oCourse)
    #
    #     return print(oStudent)
    #
    # def addDegree(self):
    #     print(f'Degree Registration\n'
    #           f'{'=' * 30}')
    #     code = int(input('Degree Code: '))
    #     name = input('Degree Name: ')
    #     duration = int(input('Degree Duration: '))
    #     oDegree = Degree(code, name, duration)
    #     print(f'Confirm Degree Registration\n'
    #           f'{'=' * 30}\n'
    #           f'{oDegree}\n'
    #           f'{'=' * 30}')
    #     confirm = input('Confirm Degree Registration (y[1]/n[2])')
    #     if confirm == '1':
    #         degreeList()[code] = [oDegree]
    #     else:
    #         print(f'Degree Registration Error')
    #     printFormat(degreeList())


