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