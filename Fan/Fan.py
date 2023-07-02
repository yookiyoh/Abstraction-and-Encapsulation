# Ralph Lorenz I. Codilan
# BSCpE 1-5
# Object-Oriented Programming | Car Class

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
    

