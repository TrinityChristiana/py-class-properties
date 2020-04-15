# **************************** Challenge: Sensitive Information ****************************

'''
Author: Trinity Terry
pyrun: python sensitive_info.py
'''

#  Create a class to represent a patient of a doctor's office. The Patient class will accept the following information during initialization

# Social security number
# Date of birth
# Health insurance account number
# First name
# Last name
# Address


class Patient:
    # Define getters for all properties.
    # Define a setter for all but the read only property.
    # Ensure that only the appropriate value can be assigned to each.

    def __init__(self, ssn, dob, hianum, f_name, l_name, address):
        """
        Creates Class Instance

        Student(first_name: str, last_name: str, age: int, cohort_number: int)

        Returns: Instance
        """
        self.social_security_number = ssn
        self.date_of_birth = dob
        self.health_insurance_acc_num = hianum
        self.first_name = f_name
        self.last_name = l_name
        self.address = address

    # First name (string)
    @property
    def social_security_number(self):
        try:
            return self.__social_security_number
        except AttributeError:
            return 0

    @social_security_number.setter
    def social_security_number(self, ssn):
        try:
            if self.social_security_number is 0 and type(ssn) is str:
                self.__social_security_number = ssn
            elif self.social_security_number is not 0:
                raise AttributeError
            elif type(ssn) is not str:
                raise TypeError
        except AttributeError:
            print("Cannot update social_security_number ")
        except TypeError:
            print("Please provide a string variable for the social_security_number")

    @property
    def date_of_birth(self):
        try:
            return self.__date_of_birth
        except AttributeError:
            return 0

    @date_of_birth.setter
    def date_of_birth(self, dob):
        try:
            if self.date_of_birth is 0 and type(dob) is str:
                self.__date_of_birth = dob
            elif self.date_of_birth is not 0:
                raise AttributeError
            elif type(dob) is not str:
                raise TypeError
        except AttributeError:
            print("Cannot update date_of_birth ")
        except TypeError:
            print("Please provide a string variable for the date_of_birth")

    @property
    def health_insurance_acc_num(self):
        try:
            return self.__health_insurance_acc_num
        except AttributeError:
            return 0

    @health_insurance_acc_num.setter
    def health_insurance_acc_num(self, hianum):
        try:
            if type(hianum) is str:
                self.__health_insurance_acc_num = hianum
            else:
                raise TypeError
        except TypeError as taco:
            print("Please provide a string variable for the health_insurance_acc_num")

    @property
    def first_name(self):
        try:
            return ""
        except AttributeError:
            return 0

    @first_name.setter
    def first_name(self, first_name):
        try:
            if type(first_name) is str:
                self.__first_name = first_name
            else:
                raise TypeError
        except TypeError as taco:
            print("Please provide a string variable for the first_name")

    @property
    def last_name(self):
        try:
            return ""
        except AttributeError:
            return 0

    @last_name.setter
    def last_name(self, last_name):
        try:
            if type(last_name) is str:
                self.__last_name = last_name
            else:
                raise TypeError
        except TypeError as taco:
            print("Please provide a string variable for the last_name")

    @property
    def full_name(self):
        try:
            return f"{self.__first_name} {self.__last_name}"
        except AttributeError:
            return 0


# instance of Product class
cashew = Patient(
    "097-23-100", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way"
)

# This should not change the state of the object
cashew.social_security_number = "838-31-2256"

# Neither should this
cashew.date_of_birth = "7001294103"


# But printing either of them should work
print(cashew.social_security_number)   # "097-23-1003"

# These two statements should output nothing
print(cashew.first_name)
print(cashew.last_name)

# # But this should output the full name
print(cashew.full_name)   # "Daniela Agnoletti"
