# Ralph Lorenz I. Codilan
# BSCpE 1-5
# Object-Oriented Programming | Pet Class

# Pseudocode

'''
class Pet:
    def __init__(self):
        // Initialize the attributes with default values
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    def set_name(self, name):
        // Set the name of the pet
        self.__name = name

    def set_animal_type(self, animal_type):
        // Set the animal type of the pet
        self.__animal_type = animal_type

    def set_age(self, age):
        // Set the age of the pet
        self.__age = age

    def get_name(self):
        // Get the name of the pet
        return self.__name

    def get_animal_type(self):
        // Get the animal type of the pet
        return self.__animal_type

    def get_age(self):
        // Get the age of the pet
        return self.__age
'''



# Define a Pet Class with its properties and methods
class Pet:
    # Enable Pet Class constructor/s
    # Constructor that initializes the Pet object attributes with default values
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0
    
    # Method that sets the name of the pet
    def set_name(self, name):
        self.__name = name
    
    # Method that sets the animal type of the pet
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    
    # Method that sets the age of the pet
    def set_age(self, age):
        self.__age = age
    
    
