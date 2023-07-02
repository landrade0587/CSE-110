""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
File: prove05.py
Author: Luis Andrade
Date: 3 november 2022
Purpose: Milestone - Adventure Game 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# step through the level 1
print("\n Welcome to this game.")
print("\n Adventure into the City.")
print("\n In the city of Valinor you must find your lost friend,")
print("through some levels that will lead you to him.")
print("Depending on the options you choose you can find him.")
print("or you can return to the beginning of this game.")
print("and as another way that will end the game completely.")
print("it all depends on what you choose as you progress through this world full of adventure and fun.")
print("\n Now as you walk down the street you find cars·")

# move to level 2
car=int(input("\n How many cars are parked, between 1 and 10:  "))
if car <=2:
    print ("Sorry you can not advance by car they are already busy, continue by bicycle it will take you 3 minutes to reach level 2")
elif 2<=car<=5:
    print("Sorry these cars are out of gas, use the motorcycle it will take you 2 minutes to reach level 2")
elif 6<=car<=10:
    print("Very good, here is a car available for you, you advance to level 2, it will take you 1 minute. You can also bring a friend with you.")
else:
    print("You must wait 5 minutes to continue walking to the next level.")


# move to level 3
model = input("\n What is your favorite car model: FERRARI, HONDA, OTHER CAR? ")
if model == "FERRARI":
    print("That's my favorite car too! You can reach level 3 in 1 minute and you can take another friend with you.")
elif model == "HONDA":
    print("Very good with this car you advance to level 3 in 2 minutes. But you don't have more space because the car is busy.")
elif model == "OTHER CAR":
    print("Very well with this car you advance to level 3 in 3 minutes but you must leave your friends because the car is full.")
else:
    print("Sorry you can not advance by car to level 3, this car is broken. Continue walking it will take you 5 minutes.")


# move to level  4
color = input("\n Choose the car color you prefer between RED; BLUE or YELLOW:  ")
if color == "RED":
    print ("It's a great car, you earn bonuses and coins and you can bring another friend.")
elif color == "BLUE":
    print("That's my favorite car color  too! Congratulations, you earn double points and coins. You can also bring 2 more friends.")
elif color == "YELLOW":
    print("Very well you earn only coins and your friends cannot advance with you.")
else:
    print("you must continue walking. Many successes.. ")

# move to level 5 (to be continue...)
print("\n\n Congratulations, you have reached level 4. From now on, more adventures with your friends full of fun await you.")
print ("to be continue...")




#prove09 original
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

option=int(input("\n Please enter an action:  "))
if option == 1:
    print ("What item would you like to add? ")
elif option == 2:
    print("The contents of the shopping cart are: ")
elif option == 3:
    print("Which item would you like to remove? ")
elif option == 4:
    print("The total price of the items in the shopping cart is ")
elif option == 5:
    print("Thank you. Goodbye. ")
else:
    print("Sorry, that is not a valid item number.")


articles = []
name = None

while name != "stop":
    name = input("Choice the netx article: ")
   
    if name != "stop":
        articles.append(name)

print()
print("Your articules are:")

for article in articles:
    print(article)