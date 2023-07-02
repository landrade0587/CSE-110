""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
File: prove08.py
Author: Luis Andrade
Date: 11 november 2022
Purpose: Create a puzzle game.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Presentation of the game to the user.
print(
"""
+====================================================+
|               The Puzzle Game.                     |
|     Welcome to the word guessing game!.            |
|   The game contains a hidden secret word.          |
| It all depends on what you choose as you progress  |
|  through this world full of adventure and fun.     |
|You can them improve their guess for the next round.|
|           Good luck.  And Have Fun.                |
+====================================================+
""")

# wait the seconds
import time
for second in range(1, 6):
    print(second, "moments")
    time.sleep(1)
print("Ready or not, here we come the first part!")


#see the introduction firts part
print(
"""
+================================+
|       First, Friend!           |
|  Enter a name of the prophet   |
|   and guess what name I've     |
|      picked for you.           |
|  So, what is the secret name?  |
+================================+
""")

#we will guess a name of the prophet
prophet = input("Enter prophet name: ")
if prophet == "Amulek":
    print("Yes - Amulek is the name of the prophet!")
elif prophet == "amulek":
    print("No, I want a big Amulek!")
else:
    print("\n The name of prophet is Amulek! Not", prophet + "!")

#wait the seconds
import time
for second in range(1, 4):
    print(second, "moments")
    time.sleep(1)
print("Ready or not, here we come the second part! \n")

#see the introduction second part
print(
"""
I¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯I
º Second, Friend! The game contains a hidden secret word.   º 
º You see is shown underscores (_) for each letter of the   º
º word. You can enters a guess. You can see the capital     º
º letter is correct and goes in that place. If it is        º
º lowercase it is in the word but it does not go there.     º
º If the guess is correct, The user wins, the game is over. º
º                     Are you ready?                        º
I¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯I
""")


print("""
                I¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯I
                º                               º
                º           Good luck!          º
                º                               º
                I¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯I
""")

# the secret word
word_secret = "nephi"
guess_search = " "
guess_counter = 0

# for the hint word secret:
print("\n Your hint is: ", end = " ")

# loop for introduce the word_secret:
for letter in word_secret:
        print("_", end = " ")

print()

#the loop while define this:
while word_secret !=guess_search:
    guess_counter +=  1
    guess_search = input ("\n What is your guess? ")
    
    for i, letter in enumerate(guess_search.lower()):
        if i < len(word_secret) and letter == word_secret[i]: 
             print("\n Your hint correctly  is: ", end ="")
             print(letter.upper(), end = " ")   
        elif letter in word_secret:
            print(letter.lower(), end = " ")
        else:
         print("_", end = " ")
    print()

#end or terminated the game with this mensage
print("""
         I¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯I
         º                               º
         º       Congratulations!        º
         º        You guessed it!        º
         º                               º
         I¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯®¯I
""")

print(f"\n It took you {guess_counter} guesses.")

print("             *")
print("            * *")
print("           *   *")
print("          *     *")
print("         ***   ***")
print("           *   *")
print("           *   *")
print("           *****")
