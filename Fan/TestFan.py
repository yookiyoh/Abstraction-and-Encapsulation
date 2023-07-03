# Ralph Lorenz I. Codilan
# BSCpE 1-5
# Object-Oriented Programming | Car Class

# Pseudocode
'''
Class TestFan:
    Main:
        fan1 = Fan(speed=fan.FAST, radius=10, color="yellow", on=True)
        fan2 = Fan(speed=fan.MEDIUM, radius=5, color="blue", on=False)

        Print("Fan 1:")
        Print("Speed: ", fan1.speedGetter())
        Print("Radius: ", fan1.radiusGetter())
        Print("Color: ", fan1.colorGetter())
        Print("On: ", fan1.onGetter())

        Print("Fan 2:")
        Print("Speed: ", fan2.speedGetter())
        Print("Radius: ", fan2.radiusGetter())
        Print("Color: ", fan2.colorGetter())
        Print("On: ", fan2.onGetter())
'''



# Import Fan
from Fan import Fan

# Import libraries
import time
from tqdm import tqdm

# Define a TestFan class
class TestFan:
    # Have TestFan constructor/s
    # Constructor that initializes the Fan objects with their properties and methods
    def __init__(self):
        try:
            speed = self.get_speed_input()   # Get speed input from the user
            radius = self.get_radius_input()   # Get radius input from the user
            color = input("Enter fan color: ")   # Get speed input from the user
            on = self.get_on_input()   # Get on/off input from the user
            
            fan1 = Fan(speed=speed, radius=radius, color=color, on=on)   # Create fan1 object using user-provided values

            speed = self.get_speed_input()   # Get speed input from the user
            radius = self.get_radius_input()   # Get radius input from the user
            color = input("Enter fan color: ")   # Get speed input from the user
            on = self.get_on_input()   # Get on/off input from the user
            
            fan2 = Fan(speed=speed, radius=radius, color=color, on=on)   # Create fan2 object using user-provided values

            self.display_fan_properties(fan1)   # Display fan1 properties
            self.display_fan_properties(fan2)   # Display fan2 properties
        
        except ValueError as e:
            print("Error: ", str(e))

    # Method that enables input for fan speed
    def get_speed_input(self):
        speed = int(input("Enter fan speed (1 for SLOW, 2 for MEDIUM, 3 for FAST): "))   # Get speed input as an integer
        if speed in (Fan.__SLOW, Fan.__MEDIUM, Fan.__FAST):   # Check if speed is a valid option
            return speed   # Return the valid speed value
        else:
            raise ValueError("Invalid speed value. Must be SLOW, MEDIUM, or FAST.")   # Raise an error for invalid speed
        
    
