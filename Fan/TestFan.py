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
        if speed in (_Fan.__SLOW, _Fan.__MEDIUM, _Fan.__FAST):   # Check if speed is a valid option
            return speed   # Return the valid speed value
        else:
            raise ValueError("Invalid speed value. Must be SLOW, MEDIUM, or FAST.")   # Raise an error for invalid speed
        
    # Method that enables input for fan radius
    def get_radius_input(self):
        radius = float(input("Enter fan radius: "))   # Get radius input as a float
        if radius > 0:   # Check if radius is greater than zero
            return radius   # Return the valid radius value
        else:
            raise ValueError("Invalid radius value. Must be greater than zero.")   # Raise an error for invalid radius
        
    # Method that enables the fan status 
    def get_on_input(self):
        on = input("Turn on fan? (y/n): ")   # Get on/off input as a string
        return on.lower() == 'y'   # Return True if 'y' is entered, False otherwise
    
    # Method that displays the fan properties
    def display_fan_properties(self, fan):
        print("\nLoading info...\n")   # Print loading message
        for i in tqdm(range(100)):   # Iterate over a range with tqdm progress bar
            time.sleep(0.01)   # Sleep for a short duration

        time.sleep(2)   # Sleep for 2 seconds
        print("\n[Fan Info Loaded Successfully!]\n")   # Print success message
        print("Fan Speed:", fan.get_speed())   # Print fan speed
        print("Fan Radius:", fan.get_radius())   # Print fan radius 
        print("Fan Color:", fan.get_color())   # Print fan color 
        print(fan.display_message())   # Print fan message (spinning or off)
        print()

# Create an instance of the TestFan class to execute the program
TestFan()

    # Testing the program
    # Error identified. Fixing the program