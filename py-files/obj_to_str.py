# **************************** Challenge: Convert Student Object to a String ****************************

'''
Author: Trinity Terry
pyrun: python obj_to_str.py
'''
 
class Student:

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

    @property
    def full_name(self):
        try:
            return f"{self.first_name} {self.last_name}"
        except AttributeError:
            return 0

    # Use the __str__ and __repr__ magic methods on your class to specify what an object's string representation should be. It's just like the toString() method in JavaScript.
    # Change your class so that any objects created from it will be rerpesented as strings in the following format.
            # Mike Ellis is 35 years old and is in cohort 39
    
    def __repr__(self):
        return f"{self.full_name} is {self.age} years old and is in cohort {self.cohort_number}"



trinity = Student()
trinity.first_name = "Trinity"
trinity.last_name = "Terry"
trinity.age = 20
trinity.cohort_number = 38

print(trinity)