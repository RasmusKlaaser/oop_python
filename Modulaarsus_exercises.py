"""School class which stores information about courses and students."""


class Course:
    def __init__(self, name: str):
        self.__course = name
    def get_grades(self):
        self.__all_grades = []
        self.__grade = 0
        self.__all_grades_append(self.__name, self.__grade)
        list[tuples[Students, int]]
        results = list(tuple(),append)

    def add_course(self, course: Course):
        if course not in courses:
            courses += {course}

    def add_grade(self, course, grade):
        self.__grades.append(tuple([course, grade]))


    def get_average_grade(self) -> float:
        average_grade = -1
        if len(self.__grades) > 0:
            total_grades = 0
            for grade in self.__grades:
                total_grades += grade[1]
            average_grade = total_grades / len(self.__grades)
        return average_grade



class Student:
    def __init__(self, name: str):
        self.__student = name
        self.__id = None
        self.__grades = []


    def set_id(self, id: int):
        if self.__id == None:
            self.__id = id
        pass

    def get_id(self) -> list:
        return self.__id
        pass

    def get_grades(self) -> list:
        return self.__grades
        pass

print(student_id)


class School:

    def __init__(self, name):
        self.__name = name
        self.__courses = []
        self.__grades = []

    def add_course(self, course):
        if course not in self.__courses:
            self.__courses.append(course)


    def add_student(self, student):
        if student in self.__students:
            pass
        else:
            id = random.randit((1), 100)
            student_set_id(id)
            self.__students.append(student)

    def add_student_grade(self, student, course, grade: str):
        if student in self.__students and course in self.__courses:
            student_add_grade(tuple([course, grade]))
            course_add_grade(tuple([student, grade]))
        pass

    def get_students(self) -> list:
        return self.__students
        pass

    def get_courses(self) -> list:
        return self.__courses
        pass

    def get_everage_grade(self):
        all_grades = 0
        if len(self.__grade == 0):
            return -1
        else:
            for grade in grades:
