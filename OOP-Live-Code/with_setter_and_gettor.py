#!/usr/bin/python3
class Person:
    def __init__(self, name, age):
        self._name = name  # underscore denotes it as a private attribute
        self._age = age

    # Getter method for name
    def get_name(self):
        return self._name

    # Setter method for name
    def set_name(self, name):
        self._name = name

    # Getter method for age
    def get_age(self):
        return self._age

    # Setter method for age
    def set_age(self, age):
        if age >= 0:  # Example constraint: age must be non-negative
            self._age = age
        else:
            print("Age cannot be negative.")

# Creating an object of Person class
person1 = Person("Alice", 30)

# Using getter methods to access attributes
print("Name:", person1.get_name())
print("Age:", person1.get_age())

# Using setter methods to modify attributes
person1.set_name("Bob")
person1.set_age(25)

# Displaying modified attributes
print("Modified Name:", person1.get_name())
print("Modified Age:", person1.get_age())
