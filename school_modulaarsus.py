import random
class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def add_student(self, student):
        if student not in self.students:
            id = random.randint(1, 1000)
            while any(student.get_id() == id for student in self.students):
                id = random.randint(1, 1000)
            student.set_id(id)
            self.students.append(student)

    def add_student_grade(self, student, course, grade: int):
        if student in self.students and course in self.courses:
            student.add_grade(course, grade)
            course.add_grade(student, grade)

    def get_students(self) -> list[str]:
        return self.students

    def get_courses(self) -> list[str]:
        return self.courses

    def get_students_ordered_by_average_grade(self) -> list[str]:
        for i in range(len(self.students) - 1):
            if self.students[i].get_average_grade() < self.students[i + 1].get_average_grade():
                help = self.students[i]
                self.students[i] = self.students[i + 1]
                self.students[i + 1] = help
        return self.students
