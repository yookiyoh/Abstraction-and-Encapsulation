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
def accelerate_car(car):
    car.brake()
    time.sleep(0.5)   # Pause for 0.5 seconds