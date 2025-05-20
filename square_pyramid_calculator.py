#!/usr/bin/env python3
# Created by: Gustav I
# Created on: May 19, 2025
# This program calculates the volume of a square pyramid
# using loops, nested conditionals, compound boolean expressions,
# input validation, and a demo mode with default arguments.

# Constants
MIN_VAL = 0.0
MAX_VAL = 1000.0


# Function with default parameters for demo
def calculate_volume(base=5.0, height=10.0):
    volume = (1 / 3) * base * base * height
    return volume


# Ask how many times to run the calculation
while True:
    try:
        tries = int(input("How many volume calculations would you like to perform? "))
        if tries > 0:
            break  # Valid input, exit loop
        else:
            print("Tries must be greater than 0.")
    except ValueError:
        print("Invalid input for number of tries. Must be a whole number.")

# Loop through the number of calculations
for i in range(tries):
    print(f"\n--- Calculation #{i+1} ---")
    print("Welcome to the Square Pyramid Volume Calculator!")

    while True:
        try:  # Try catch for demo and while loop for input
            demo = input("Would you like a demo? (yes/no): ").strip().lower()
            if demo != "yes" and demo != "no":
                print("Please type 'yes' or 'no'.")
                continue

            if demo == "yes":  # Demo outcome no. 1
                volume = calculate_volume()
                print(f"\nDemo Mode: Base = 5.0, Height = 10.0")
                print(f"Volume = {volume:.2f} cubic units")
                break  # Go to next try

            else:  # User input for base and height
                base = float(input("Enter the base of the pyramid (0-1000): "))
                height = float(input("Enter the height of the pyramid (0-1000): "))

                # Compound boolean + nested if
                if (MIN_VAL < base <= MAX_VAL) and (MIN_VAL < height <= MAX_VAL):
                    volume = calculate_volume(base, height)
                    print(f"\nVolume = {volume:.2f} cubic units")
                    break
                else:  # Error message for 0 > user_input or user_input > 1000
                    print(
                        "Error: Base and height must be greater than 0 and less than or equal to 1000."
                    )

        except ValueError:  # Try catch output for non numeric input
            print("Invalid input. Please enter numeric values only.")
