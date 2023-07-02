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
from colorama import Fore, Back, Style
from tqdm import tqdm

# Define a TestFan class
class TestFan:
    # Have TestFan constructor/s