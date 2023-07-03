# Ralph Lorenz I. Codilan
# BSCpE 1-5
# Object-Oriented Programming | Car Class

# Pseudocode

'''
class Car:
    __year_model
    __maker
    __speed
    
    method __init__(year_model, make):
        __year_model = year_model
        __make = make
        __speed = 0
    
    method accelerate():
        __speed += 5
    
    method brake(): 
        if __speed >= 5:
            __speed -= 5
        else:
           __speed = 0

    method get_speed():
        return __speed
'''


# Define a Car class with its properties and methods
class Car:
    # Enable Car class constructor/s
    # Constructor that initializes the Car object with year model, maker, and speed
    self.__year_model = year_model
    self.__maker = maker
    self.__speed = 0

    # Execute the Car class methods
    # Method that increases the car's speed by 5
    def accelerate(self):
        self.__speed += 5

    # Method that enables the car's brakes
    def brake(self):
        if self.__speed >= 5:
            # If the speed is greater than or equal to 5, decrease the speed by 5
            self.__speed -= 5
        else:
            # If the speed is less than 5, set the speed to 0
            self.__speed = 0
    
    # Method that returns the current speed of the car
    def get_speed(self):
        return self.__speed