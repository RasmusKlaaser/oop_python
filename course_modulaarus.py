class Course:
    def __init__(self, name: str):
        self.name = name
        self.grades = []

    def add_grade(self, student, grade):
        self.grades.append(tuple([student, grade]))

    def get_grades(self) -> list[tuple[str, int]]:
        return self.grades

    def set_grade(self, Student, grade):
        self.grades.append(tuple(Student, grade))

    def get_average_grade(self) -> float:
        average = -1
        if len(self.grades):
            total = 0
            for grade in self.grades:
                total += grade[1]
            average = total / len(self.grades)
        return average

    def __repr__(self):
        return f"{self.name}"