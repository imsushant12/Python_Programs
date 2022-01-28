# Class without getter and setters.
class Student:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age


# Class using getters and setters.
class Person:
    def __init__(self, name=""):
        self.name = name

    # getter method to get the values of the class
    def get_name(self):
        return self.name

    # setter method to set the values of the class
    def set_name(self, new_value):
        self.name = new_value


if __name__ == "__main__":
    # Dealing with class without getters and setters:
    Tom = Student()
    # Setting the name of the student-Tom:
    Tom.name = "Tom Hardy"
    Tom.age = 5
    print(f"Name: {Tom.name}, Roll Number: {Tom.age}")

    # ---------------------------------------------
    # Dealing with class with getters and setters:
    Tom = Person()
    # Setting the name of the Person-Tom:
    Tom.set_name("Tom Hardy")
    # Getting the name of the Person-Tom:
    print(f"Name: {Tom.get_name()}")
