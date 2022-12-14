"""Encapsulation exercise."""


class Student:
    """Represent student with name, id and status."""

    def __init__(self, name, id):
        """A."""
        self.__name = name
        self.__id = id
        self.__status = "Active"

    def get_id(self):
        """B."""
        return self.__id

    def get_name(self):
        """C."""
        return self.__name

    def get_status(self):
        """D."""
        return self.__status

    def set_name(self, name):
        """E."""
        self.__name = name

    def set_status(self, status):
        """F."""
        if status == "Active" or status == "Inactive" or status == "Expelled" or status == "Finished":
            self.__status = status
        else:
            pass


student = Student('John', 1)
print(student.get_status())
student.set_name("Willy")
print(student.get_name())
print(student.set_status("Inactive"))
print(student.get_status())
