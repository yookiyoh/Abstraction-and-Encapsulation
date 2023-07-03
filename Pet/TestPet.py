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

# Create a class for the Pet Details Widget
class PetDetailsWidget(tk.Tk):
    # Have TestPet constructor/s
    # Constructor that initializes the Pet Details Widget with their properties and methods
    def __init__(self):
        super().__init__()
        self.pet = Pet()   # Create an instance of the Pet class
        self.title("Pet Details")   # Set the window title
        self.setup_ui()   # Set up the user interface

    # Method that comprises labels, input fields, and button for user interface
    def setup_ui(self):
        self.name_label = tk.Label(self, text="Name:", font=("Ubuntu", 14, "bold"))
        self.name_input = tk.Entry(self, font=("Ubuntu", 12))

        self.type_label = tk.Label(self, text="Type:", font=("Ubuntu", 14, "bold"))
        self.type_input = tk.Entry(self, font=("Ubuntu", 12))

        self.age_label = tk.Label(self, text="Age:", font=("Ubuntu", 14, "bold"))
        self.age_input = tk.Entry(self, font=("Ubuntu", 12))

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_button_clicked, font=("Ubuntu", 12))

        # Pack the labels, input fields, and button in the window
        self.name_label.pack(pady=10)
        self.name_input.pack()
        self.type_label.pack(pady=10)
        self.type_input.pack()
        self.age_label.pack(pady=10)
        self.age_input.pack()
        self.submit_button.pack(pady=15)
    
    # Method that gets the input values from the user
    def submit_button_clicked(self):
        name = self.name_input.get().strip()
        animal_type = self.type_input.get().strip()
        age_str = self.age_input.get().strip()

        # Validate the input values
        if not name or not animal_type or not age_str:
            messagebox.showerror("Error", "Please fill in all the fields.")
            return
        
        try:
            age = int(age_str)
        except ValueError:
            messagebox.showerror("Error", "Age must be a valid integer.")
            return
        
        # Set the pet details using the Pet class methods
        self.pet.set_name(name)
        self.pet.set_animal_type(animal_type)
        self.pet.set_age(age)

        self.display_pet_details()   # Display the pet details

    # Method that displays the pet details
    def display_pet_details(self):
        self.clear_widgets()   # Clear any existing widgets in the window

        # Create labels to display the pet details
        pet_name_label = tk.Label(self, text="Name: " + self.pet.get_name(), font=("Ubuntu", 14, "bold"), fg="green")
        pet_type_label = tk.Label(self, text="Type: " + self.pet.get_animal_type(), font=("Ubuntu", 14, "bold"), fg="blue")
        pet_age_label = tk.Label(self, text="Age: " + str(self.pet.get_name()), font=("Ubuntu", 14, "bold"), fg="purple")

        # Pack the labels in the window
        pet_name_label.pack(pady=10)
        pet_type_label.pack(pady=5)
        pet_age_label.pack(pady=5)

        self.animate_labels(pet_name_label, pet_type_label, pet_age_label)   # Animate the labels
        self.animate_window_size()   # Animate the window size

    # Method that removes all widgets from the window
    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.pack_forget()
    
    # Method that animates the labels
    def animate_labels(self, *labels):
        colors = ["green", "blue", "purple"]
        delay = 500   # Delay between color changes (in milliseconds)

        for _ in range(5):   # Perform color change animation 5 times
            for color in colors:
                self.update_labels_color(labels, color)
                self.update()
                time.sleep(delay / 1000)
    
    # Method that updates the label colors
    def update_labels_color(self, labels, color):
        for label in labels:
            label.config(fg=color)
        
    # Method that animates the window size
    def animate_window_size(self):
        width, height = self.winfo_width(), self.winfo_height()

        for _ in range(3):   # Perform window size animation 3 times
            self.geometry(f"{width + 50}x{height + 50}")
            self.update()
            time.sleep(0.5)

            self.geometry(f"{width}x{height}")
            self.update()
            time.sleep(0.5)
        


if __name__ == '__main__':
    widget = PetDetailsWidget()   # Create an instance of the PetDetailsWidget
    widget.mainloop()   # Run the GUI main loop

    time.sleep(0.5)

    for _ in tqdm(range(100), desc="Processing", unit="%", ascii=True):
        time.sleep(0.01)

        # program testing