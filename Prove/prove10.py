"""
File: prove10.py
Author: Luis Andrade
date: 3 December 2022
Purpose: Assignment Milestone prove in the cart shopping
"""
component = []
costs = []

print( """ \n\n\n 
+========================================+
|                                        |
| ¡Welcome to the shopping cart program! |
|                                        |
+======================================== +""")
print( "\n\n Please stay one moment please... " )

import time
for second in range(1, 6):
    print(second, "Moment")
    time.sleep(1)
print("Are you Ready?")	
print("Ready or not, here I come!")

while True:
 print("""\n\n
 I¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯I
 º                                                   º
 º      Please select one of the following options:  º
 º               1. Add article.                     º
 º               2. See cart.                        º
 º               3. Remove article.                  º
 º               4. Calculate the total.             º
 º               5. Exit.                            º
 º                                                   º
 I¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯I""")
 option = input("\n\n Please enter your option: ")

 if option == "1":
      article = input ("What article would you like to add a cart? ")
      component.append(article)
      cost = float(input(f"What is the cost of {article}? "))
      costs.append(cost)
      print(f"{article} has been added to the cart corretly.")
  
 elif option == "2":
      print("\n\n The contents of the shopping cart are: ")
      for i, article in enumerate(component):
        print(f"{i + 1}. {article} --- $ {costs[i]}")
      print("    *")
      print("   * *")
      print("  *   *")
      print(" *     *")
      print("***   ***")
      print("  *   *")
      print("  *   *")
      print("  *****")
      print("Your list for the moment goes like this:")

 elif option == "3":
      i = int(input("\n\n Which article would you like to remove? "))
      if i <= len(component) and i > 0:
       component.pop(i - 1)
       costs.pop(i - 1)
      print("Article Removed. ")
       
 elif option == "4":
      total = 0
      for cost in costs:
         total = total + cost
      print(f"\n\n The total price of the items in the shopping cart is: $ {total:.2f} ")
       
 elif option == "5":
     print("\n\n Thank you.")
     print("Goodbye. ")
     break

 elif option >= "6":
    print("\n\n Sorry, that is not a valid item number.")  
    print("Try again: the values items numbers is 1 to 5 only.")
           