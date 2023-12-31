# Ralph Lorenz I. Codilan
# BSCpE 1-5
# Object-Oriented Programming | Fan Class

# Pseudocode

'''
Class Fan:
    Constants:
        SLOW = 1
        MEDIUM = 2
        FAST = 3

    Private Fields:
        speed: int
        on: bool
        radius: float
        color: string

    Methods:
        Constructor(speed, radius, color, on):
            Set the speed to the given value, or default to SLOW if not provided.
            Set the radius to the given value, or default to 5 if not provided.
            Set the color to the given value, or default to blue if not provided.
            Set the on state to the given value, or default to False if not provided.

        Getters and setters for speed, on, radius, and color:
            speedGetter():
                Return the value of speed.

            speedSetter(newSpeed):
                Set the value of speed to newSpeed.

            onGetter():
                Return the value of on.

            onSetter(newOn):
                Set the value of on to newOn.

            radiusGetter():
                Return the value of radius.

            radiusSetter(newRadius):
                Set the value of radius to newRadius.

            colorGetter():
                Return the value of color.

            radiusSetter(newRadius):
                Set the value of color to newColor.
'''



# Define a Fan class with its properties and methods
class Fan:
    __SLOW = 1   # Private constant attribute representing the slow speed of the fan
    __MEDIUM = 2   # Private constant attribute representing the medium speed of the fan
    __FAST = 3   # Private constant attribute representing the fast speed of the fan

    # Enable Fan class constructor/s
    # Constructor that initializes the Fan object to its default settings
    def __init__ (self, speed=1, radius=5, color="blue", on=False):
        # Defined the default values for speed, radius, color, and on state
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on
    
    # Execute the Fan class methods
    # Method that gets the current speed of the fan
    def get_speed(self):
        return self.__speed
    
    # Method that sets the speed of the fan with the given value
    def set_speed(self, speed):
        if speed in (Fan.__SLOW, Fan.__MEDIUM, Fan.__FAST):
            self.__speed = speed   # Assign the new speed
        else:
            raise ValueError("Invalid speed value. Must be SLOW, MEDIUM, or FAST.")
    
    # Method that gets the current radius of the fan
    def get_radius(self):
        return self.__radius
    
    # Method that sets the radius of the fan with the given value
    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius   # Assign the new radius
        else:
            raise ValueError("Invalid radius value. Must be greater than 0.")
    
    # Method that gets the current color of the fan
    def get_color(self):
        return self.__color
    
    # Method that sets the color of the fan with the given value
    def set_color(self, color):
        self.__color = color   # Assign the new color
    
    # Method that checks if the fan is turned on or not
    def is_on(self):
        return self.__on
    
    # Method that sets the status of the fan (on/off)
    def set_radius(self, on):
        self.__on = bool(on)   # Convert the input to a Boolean value

    # Method that displays a message describing the fan's status
    def display_message(self):
        if self.__on:
            message = f"The {self.__color} fan is spinning at {self.__speed} speed."
        else:
            message = f"The {self.__color} fan is currently off."
        return message
    
    # Method that increases the fan's speed by 1 if it is not already at the maximum
    def increase_speed(self):
        if self.__speed < Fan.__FAST:
            self.__speed += 1
        
    # Method that decreases the fan's speed by 1 if it is not already at the minimum
    def decrease_speed(self):
        if self.__speed > Fan.__SLOW:
            self.__speed -= 1