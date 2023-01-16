

class Student:
    def __init__(self, name: str):
        self.name = name
        self.__grades = []
        self.__id = None

    def set_id(self, id: int):
        if self.__id == None:
            self.__id = id
        else:
            return("Cant change ID")

    def get_id(self):
        return self.__id

    def add_grade(self, course, grade):
        self.__grades.append(tuple([course, grade]))

    def get_grades(self) -> list[tuple[str, int]]:
        return self.__grades

    def get_average_grade(self):
        average = -1
        if len(self.__grades):
            total = 0
            for grade in self.__grades:
                total += grade[1]
            average = total / len(self.__grades)
        return average

    def __repr__(self) -> str:
        return f"{self.name}"

