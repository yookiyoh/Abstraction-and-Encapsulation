# Ralph Lorenz I. Codilan
# BSCpE 1-5
# Object-Oriented Programming | Car Class

# Pseudocode

'''
import time
import tkinter as tk
from tkinter import messagebox
from tqdm import tqdm
from Car import Car

method accelerate_car(car):
    car.accelerate()
    time.sleep(0.5)

method brake_car(car):
    car.brake()
    time.sleep(0.5)

method main():
    car = Car(2023, "Exampler Maker")

    progress_bar = create_tqdm(total=10, desc="Accelerating and Braking", unit="step")

    window = create_tkinter_window(title="Car Acceleration")

    speed_label = create_tkinter_label(text="Current Speed:")
    speed_label.pack()

    speed_value = create_tkinter_label(text=car.get_speed())
    speed_value.pack()

    try:
        loop 5 times:
            accelerate_car(car)
            update_speed_label(speed_value, car.get_speed())
            update_progress_bar(progress_bar)
            update_window(window)

        loop 5 times:
            brake_car(car)
            update_speed_label(speed_value, car.get_speed())
            update_progress_bar(progress_bar)
            update_window(window)

        update_speed_label(speed_value, 0)
        update_progress_bar(progress_bar)
        update_window(window)
        sleep(0.5)

    except Exception as e:
        show_error_message("Error", e)

    finally:
        close_progress_bar(progress_bar)
        destroy_window(window)

if __name__ == '__main__'
    main()
'''



# Import Car
from Car import Car

 # Import libraries
import time
import tkinter as tk
from tkinter import messagebox
from tqdm import tqdm

# Have TestCar methods
# Method that increases the car's speed by calling the accelerate method
def accelerate_car(car):
    car.accelerate()
    time.sleep(0.5)   # Pause for 0.5 seconds

# Method that decreases the car's speed by calling the brake method
def brake_car(car):
    car.brake()
    time.sleep(0.5)   # Pause for 0.5 seconds

# Method transpiring main functions of the program
def main():
    # Create a Car object with year model and manufacturer
    car = Car(2023, "Bugatti")

    # Create a progress bar with a total of 10 steps, description "Accelerating and Braking", and unit "step"
    progress_bar = tqdm(total=10, desc="Accelerating and Braking", unit="step")

    # Create a GUI window using Tkinter
    window = tk.Tk()
    window.title("Car Acceleration")

    # Create a label to display the text "Current Speed:"
    speed_label = tk.Label(window, text="Current Speed:")
    speed_label.pack()

    # Create a label to display the current speed of the car
    speed_value = tk.Label(window, text=str(car.get_speed()))
    speed_value.pack()

    try:
        # Accelerate the car 5 times
        for _ in range(5):
            accelerate_car(car)
            speed_value.config(text=str(car.get_speed()))   # Update the label with the current speed
            progress_bar.update(1)   # Update the progress bar by 1 step
            window.update()   # Update the GUI window

        # Brake the car 5 times
        for _ in range(5):
            brake_car(car)
            speed_value.config(text=str(car.get_speed()))   # Update the label with the current speed
            progress_bar.update(1)   # Update the progress bar by 1 step
            window.update()   # Update the GUI window
        
        # Set the label to display "0" to indicate the speed is "0"
        speed_value.config(text="0")
        progress_bar.update(1)   # Update the progress bar by 1 step
        window.update()   # Update the GUI window
        time.sleep(0.5)   # Pause for 0.5 seconds

    except Exception as e:
        # Display an error message box with an error message
        messagebox.showerror("Error occurred", str(e))
    
    finally:
        progress_bar.close()   # Close the progress bar
        window.destroy()   # Dismantle the GUI window

# Create a TestCar instance to execute the program
if __name__ == '__main__':
    main()

    # testing the program