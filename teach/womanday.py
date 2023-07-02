"""
File: womanday.py
Author: Luis Andrade
Purpose: Congratulate the woman on her day on March 8, 2023
"""
print ()
print("Good Morning")
print("Please fill in the following information: ")
print ()
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
print()
print("According to the information provided by you then:")
print("Your name is {0}, {1} {0}.".format(last_name, first_name))
print()
# other ways for the requirement would be the following codes
# print("Your name is {}, {} {}.".format(last_name, first_name, last_name))
# print(f"your name is {last_name}, {first_name} {last_name}.")
# print("Your name is " + last_name + ", " + first_name + " " + last_name + ".")
print("Thanks for the information provided.")
print("Have a nice day")
print("Happy Women's Day")
print("Have a good day")
print ("Now...")

print( """ \n
+============================================+
|                                            |
| ¡Welcome to this program that will         |
|  remind you of something very valuable !   |
|                                            |
+============================================+""")
print( "\n\n  Please stay one moment please..... " )

import time
for second in range(1, 6):
    print(second, "Moment")
    time.sleep(1)
print("Are you Ready?")	
print("Ok then let's move on!")

quote = "Who can find a virtuous woman? for her price is far above rubies.The heart of her husband doth safely trust in her, so that he shall have no need of spoil. She will do him good and not evil all the days of her life. She seeketh wool, and flax, and worketh willingly with her hands. She is like the merchants ships; she bringeth her food from afar. She ariseth also while it is yet night, and giveth meat to her household, and a portion to her maidens. She considereth a field, and buyeth it: with the fruit of her hands she planteth a vineyard. She girdeth her loins with strength, and strengtheneth her arms. She perceiveth that her merchandise is good: her candle goeth not out by night. She layeth her hands to the spindle, and her hands hold the adistaff. She stretcheth out her hand to the apoor; yea, she reacheth forth her hands to the needy. She is not afraid of the snow for her household: for all her household are clothed with scarlet. She maketh herself coverings of tapestry; her aclothing is silk and purple. Her husband is known in the gates, when he sitteth among the elders of the land. She maketh fine linen, and selleth it; and delivereth girdles unto the merchant. Strength and honour are her clothing; and she shall rejoice in time to come. She openeth her mouth with wisdom; and in her tongue is the law of akindness. She looketh well to the ways of her household, and eateth not the bread of aidleness. Her children arise up, and call her blessed; her husband also, and he praiseth her."

run_again = "yes"

while run_again == "yes":
    user_number = int(input("Please enter a number between 1 to 5: "))

    for i, letter in enumerate(quote):
        # Remember that the % operator divides by a number and returns the remainder.
        # So we can get every 3rd letter by dividing by 3 and looking for a remainder of 0,
        # or more generically, we can divide by the user's number
        if i % user_number == 0:
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")
    
    # This puts a newline at the end of the list of quote
    print()

    run_again = input("Would you like to enter another number? yes or no? ")
print()
print()
print()
print("{0}, {1} {0}.".format(last_name, first_name))
print("Happy Women's Day")
print("Have a good day")
print("Goodbye")