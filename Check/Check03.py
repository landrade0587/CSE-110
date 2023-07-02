"""""""""""""""""""""""""""""""""""""""""""""""""""
File: check03.py
Author: Luis Andrade 
Purpose: Practice using mathematical expressions.
"""""""""""""""""""""""""""""""""""""""""""""""""""
print("\n hello at this time we will help you calculate some data")
print("\n Please enter the information requested for a better experience")
print("\n First we will calculate how old you will be next year")
age = int(input("\n How old are you? "))
next_year_age = age + 1
print(f"On your next years, you will be {next_year_age}.")

# Note that we could do the addition right in the display if we wanted:
print(f"\n On your next birthday, you will be {age + 1}.")

print() # This prints a blank line


print("second we will calculate how many eggs you have")
cartons = int(input("How many egg cartons do you have? "))
eggs = cartons * 30
print(f"You have {eggs} eggs")

# In the next example, to create a blank line I included \n at the beginning of the string
print("\n\n Finally we will calculate how many cookies you have and how to distribute them among your friends")
cookies = int(input("\n How many cookies do you have? "))
people = int(input("How many people are there? "))

cookies_per_person = cookies / people

print(f"Each person may have {cookies_per_person} cookies")
print("thanks for participating have a great day")