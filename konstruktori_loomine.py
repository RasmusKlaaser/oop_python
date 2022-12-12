"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""
    pass


class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.age = 0


class Student:
    """Represent student with firstname, lastname and age."""
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    pass


if __name__ == '__main__':
    # empty usage
    empty_class = Empty()

    # 3 x person usage
    person1 = Person()
    person1.firstname = "John"
    person1.lastname = "Dow"
    person1.age = 48
    person2 = Person()
    person2.firstname = "Ada"
    person2.lastname = "William"
    person2.age = 23
    person3 = Person()
    person3.firstname = "Adam"
    person3.lastname = "Williams"
    person3.age = 25

    # 3 x student usage
    student1 = Student("John")
    student2 = Student("Adams")
    student3 = Student("Willy")