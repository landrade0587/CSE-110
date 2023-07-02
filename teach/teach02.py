""""""""
#File: teach02.py
#Author:Luis Andrade
#Purpose: Practice formatting strings.
""""""""
print()
print("Good Morning")
print("At this time we will collect your personal information")
print("Please enter the following information:")

# This prints a blank line
print()

first_name = input("First name: ")
last_name = input("Last name: ")
email = input("Email address: ")
phone = input("Phone number: ")
job_title = input("Job title: ")
id_number = input("ID Number: ")

# This time I used a \n to make a blank line before this:
print("\nThe ID Card is:")
print("----------------------------------------")
print(f"{last_name.upper()}, {first_name.capitalize()}")
print(job_title.title())
print(f"ID: {id_number}")
print()
print(email.lower())
print(phone)
print("----------------------------------------")