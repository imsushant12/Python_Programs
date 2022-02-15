class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # a function to get the name of the Person
    def get_name(self):
        return self.name
    
    # Setting the get_name() function as a property using the property() function.
    name_property = property(get_name)

if __name__ == "__main__":
    Jack = Person("Jack", 26)
    print("The name of the Person is:", Jack.name_property)