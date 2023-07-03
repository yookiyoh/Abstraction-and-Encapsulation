# Ralph Lorenz I. Codilan
# BSCpE 1-5
# Object-Oriented Programming | Pet Class

# Pseudocode

'''
Import time  # Import the time module for delays
Import tqdm  # Import tqdm for progress bar
Import tkinter as tk  # Import tkinter for GUI
Import messagebox from tkinter  # Import messagebox for displaying error messages
Import Pet from Pet module  # Import the Pet class from Pet module

# Create a class for the Pet Details Widget
Class PetDetailsWidget(tk.Tk):
    Initialize():
        Call super().__init__()
        Create an instance of the Pet class and assign it to self.pet
        Set the window title to "Pet Details"
        Call setup_ui() to set up the user interface

    setup_ui():
        Create labels, input fields, and a button for the user interface
        Pack the labels, input fields, and button in the window

    submit_button_clicked():
        Get the input values from the user
        Validate the input values
        If any field is empty, show an error message and return
        Try to convert the age to an integer
        If it raises a ValueError, show an error message and return
        Set the pet details using the Pet class methods
        Call display_pet_details() to display the pet details

    display_pet_details():
        Call clear_widgets() to clear any existing widgets in the window
        Create labels to display the pet details
        Pack the labels in the window
        Call animate_labels() to animate the labels
        Call animate_window_size() to animate the window size

    clear_widgets():
        Remove all widgets from the window

    animate_labels():
        Define colors as a list of colors
        Define a delay between color changes
        Perform color change animation 5 times
            Iterate over the colors
                Call update_labels_color() to update the color of the labels
                Update the window
                Pause for the specified delay

    update_labels_color():
        Iterate over the labels
            Update the color of the labels

    animate_window_size():
        Get the current width and height of the window
        Perform window size animation 3 times
            Increase the width and height of the window by 50
            Update the window
            Pause for 0.5 seconds
            Reset the width and height of the window
            Update the window
            Pause for 0.5 seconds

If __name__ == "__main__":
    Create an instance of the PetDetailsWidget
    Run the GUI main loop

    Pause for 0.5 seconds

    For each iteration in tqdm(range(100)) with description "Processing" and unit "%" and ASCII style:
        Pause for 0.01 seconds
'''



# Import the Pet Class from Pet Module
from Pet import Pet

# Import libraries
import time   # Import the time module for the delays
from tqdm import tqdm   # Import tqdm for progress bar
import tkinter as tk   # Import tkinter for GUI
from tkinter import messagebox   # Import messagebox for displaying error messages

