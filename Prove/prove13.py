"""
File: prove13.txt
Author: Luis Andrade
Date: 10 December 2022
Purpose: Prove Assignment Milestone.
"""
print( """ \n\n\n 
+============================================+
|                                            |
| ¡Welcome to the The program will allow     |
|    you to know the thermal sensation!      |
|                                            |
+============================================+""")
print( "\n\n  Please stay one moment please..... " )

import time
for second in range(1, 6):
    print(second, "Moment")
    time.sleep(1)
print("Are you Ready?")	
print("Ok then let's move on!")


print("""\n\n
 I¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯I
 º                                                   º
 º    Whith this program  you can get information    º
 º       about then displays the wind chill values   º
 º            for various wind speeds                º
 º              at that temperature.                 º
 º                                                   º
 I¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯I""")

import math

def fahrenheit_degrees(f):
    return f

#fahrenheit_degrees = (celsius_degrees  * 9 / 5)+32
def fahrenheit_degrees1(c):
    return (c* 9 / 5)+32

def speed(V):
    return V

# Wind Chill (ºF) = 35.74 + 0.6215*T - 35.75(V**0.16) + 0.4275T(V**0.16)
def windchill(f):
    return 35.74 + 0.6215*f - 35.75(V**0.16) + 0.4275*T(V**0.16)

def compute_temperature(shape, value1, value2=0):
    temperature = -1

    if shape == "f":
        temperature = fahrenheit_degrees(value1)
    elif shape == "fahrenheit_degrees1":
        temperature = fahrenheit_degrees1(value1)
    elif shape == "speed":
        speed = (value1)
    elif shape == "windchill"
        windchill = (value1)
    
    return temperature

shape = ""

while temperature != "exit":
    temperature = input("What temperature do you have? ")

    # Convert it to lower case once, so we don't have to keep converting it
    shape = shape.lower()

    if shape == "fahrenheit_degrees":
        f = float(input("What is the temperature of the f? "))
        temperature = compute_temperature(shape, f)
        print(f"The temperature fahrenheit is {temperature}")
    elif shape == "fahrenheit_degrees1":
        c = float(input("What is the temperature of the c? "))
        temperature1 = compute_temperature1(shape, c)
        print(f"The temperature is {temperature1}")
    elif shape == "speed":
        speed = float(input("What is the speed?  "))
        speed = compute_speed(shape, V)
        print(f"The area is {speed}")
    elif shape == "windchill":
        radius = float(input("What is the windchill? "))
        windchill = compute_windchill(shape, )
        print(f"The windchill is {windchill}")


