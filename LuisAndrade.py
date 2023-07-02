"""""""""""""""""""""""""""""""""""""""""""""""""""
File: LuisAndrade.py
Author: Luis Andrade 
Date: 8 october 2022
Purpose: Practice using mathematical expressions and Milestone - Meal Price Calculator.
"""""""""""""""""""""""""""""""""""""""""""""""""""
# Stretch number 1: Using the math library
import math
print("\n Hello at this time we will help you calculate some data for excelent service")
print("\n Please enter the information requested for a better experience in the restaurant")
child = float(input ("\n What is the price of a child's meal?: $ "))
print (f"  The price child's meal is: $ {child:.2f}")
adult =float( input("\n What is the price of an adult's meal?: $ "))
print(f"  The price adult's meal is: $ {adult:.2f}")

print() # This prints a blank line or \n in the line of code
children = input ("\n How many children are there? ")
print (f" Therefore we have: {children} children.")
adults = input ("\n How many adults are there? ")
print (f"  Therefore we have: {adults} adults.")

rate = input ("\n What is the sales tax rate? $ ")
print (f"  Therefore we have the sales tax rate in this restaurant is: $ {rate}.")

print ("\n So your bill of sale is deducted by")

print (" \n The total child's meal is:" )
total_child =  child * 4
print(f" $ {+ total_child:.2f}")

print ("\n The total adult's meal is:  ")
total_adult =  adult * 2
print(f" $ {+ total_adult:.2f}")

print ("\n Your account subtotal is:  ")
subtotal =  total_child + total_adult
print(f" $ {subtotal:.2f}")

print ("\n The sales tax rate is:  ")
sales_tax = float(( (subtotal * 6) / 100))
print(f" $ {+ sales_tax:.2f}")

print ("\n The total sales in your purchase is:  ")
total = float(( (subtotal + sales_tax )))
print(f" $ {+ total:.2f}")

payment_amount =  float(input ("\n  What is the payment amount? $ "))
print (f" Therefore the payment amount is $ {payment_amount:.2f} dollars.")

changes =  payment_amount - total
print (f" And your change amount is $ {changes:.2f} dollars.")

print("\n\n Thanks for participating have a great day")