class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Seting the get_name() function as a property using the @property decorator.
    @property
    def get_name(self):
        return self.name

    # Setting the get_name() as a setter decorator.
    @get_name.setter
    def get_name(self, new_name):
        self.name = new_name


if __name__ == "__main__":
    Jack = Person("Jack", 26)
    print("The old name of the Person is:", Jack.get_name)

    new_name = "Jack Sparrow"
    Jack.get_name = new_name

    print("The new name of the Person is:", Jack.get_name)
