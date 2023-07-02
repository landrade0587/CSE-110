"""""""""""""""""""""""""""""""""""""""""""""""""""
File: check04.py
Author: Luis Andrade 
date: 5 september 2022
Purpose: Solving problems with variables and expressions, and displaying the results.
"""""""""""""""""""""""""""""""""""""""""""""""""""
print("\n hello we are measure the value of degrees in Fahrenheit, Celsius, or Kelvin")
print("\n Please enter the information requested for a better experience")

print("\n First we will calculate Convert degrees in Fahrenheit to Celsius ")
fahrenheit_degrees = float(input("\n\n What is the temperature in degrees Fahrenheit? "))
celsius_degrees = (fahrenheit_degrees - 32) * 5 / 9
print(f"The temperature in degrees Celsius is {celsius_degrees:.1f} degrees.")

print() # This prints a blank line

print("\n Second we will calculate Convert degrees in Celsius to Fahrenheit ")
celsius_degrees = float(input("What is the temperature in degrees Celsius? "))
fahrenheit_degrees = (celsius_degrees  * 9 / 5)+32
print(f"The temperature in degrees Fahrenheit is {fahrenheit_degrees:.2f} degrees.")

print() # This prints a blank line

print("\n Third we will calculate Convert Kelvin to Fahrenheit degrees.")
Kelvin = float(input("What is the temperature in Kelvin? "))
fahrenheit_degrees = (Kelvin  - 273) * 9/5 + 32
print(f"The temperature in degrees Fahrenheit is {fahrenheit_degrees:.3f} degrees.")

print() # This prints a blank line

print("\n Fourth we will calculate Convert Kelvin to Celsius degrees.")
Kelvin = float(input("What is the temperature in Kelvin? "))
celsius_degrees = (Kelvin - 273.15)
print(f"The temperature in degrees Celsius is {celsius_degrees:.4f} degrees.")

print("\n\n Thanks for participating have a great day")