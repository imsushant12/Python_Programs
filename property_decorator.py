class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Seting the get_name() function as a property using the @property decorator.
    @property
    def get_name(self):
        return self.name


if __name__ == "__main__":
    Jack = Person("Jack", 26)
    print("The name of the Person is:", Jack.get_name)
