"""
File: prove09.py
Author: Luis Andrade
date: 12 november 2022
Purpose: Assignment Milestone
"""
print(
"""
I¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯I
º                                                   º
º      ¡Welcome to the shopping cart program!       º 
º      Please select one of the following options:  º
º               1. Add article.                     º
º               2. See cart..                       º
º               3. Remove item..                    º
º               4. Calculate the total.             º
º               5. Exit.                            º
º                                                   º
I¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯I
""")

articles = []
name = (None)
option=int(input("\n Please enter an action:  "))

if option == 1:
    print ("What item would you like to add? ")
    while name != "stop":
     name = input("Choice the netx article: ")
    if name != "stop":
      articles.append(name)
elif option == 2:
    print("The contents of the shopping cart are: ")
   
    print()
    print("Your articules are:")

    for article in articles:
       print(article)
elif option == 3:
    print("Which item would you like to remove? ")
elif option == 4:
    print("The total price of the items in the shopping cart is: ")
elif option == 5:
    print("Thank you. Goodbye. ")
else:
    print("Sorry, that is not a valid item number.")

