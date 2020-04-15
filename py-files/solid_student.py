
# Define a Python class named Student. This class will have 5 properties.
class Student:
    # Define getters for all properties.
    # Define a setter for all but the read only property.
# Ensure that only the appropriate value can be assigned to each.

    def __init__(self):
        """
        Creates Class Instance

        Student(first_name: str, last_name: str, age: int, cohort_number: int)

        Returns: Instance
        """
        self.first_name = ""
        self.last_name = ""
        self.age = 0
        self.cohort_number = 0

    # First name (string)
    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return 0

    @first_name.setter
    def first_name(self, new_name):
        if type(new_name) is str:
            self.__first_name = new_name
        else:
            raise TypeError("Please provide a string for value of first_name")

    # Last name (string)
    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return 0

    @last_name.setter
    def last_name(self, new_name):
        if type(new_name) is str:
            self.__last_name = new_name
        else:
            raise TypeError("Please provide a string for value of last_name")

    # Age (integer)
    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0

    @age.setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError("Please provide a integer for value of age")

    # Cohort number (integer)
    @property
    def cohort_number(self):
        try:
            return self.__cohort
        except AttributeError:
            return 0

    @cohort_number.setter
    def cohort_number(self, new_cohort):
        if type(new_cohort) is int:
            self.__cohort = new_cohort
        else:
            raise TypeError("Please provide a integer for value of cohort_number")

    # The full name property should return first name and last name separated by a space. It's value cannot be set.
    # Full name (read-only string)
    @property
    def full_name(self):
        try:
            return f"{self.first_name} {self.last_name}"
        except AttributeError:
            return 0

trinity = Student()
print(trinity.full_name)