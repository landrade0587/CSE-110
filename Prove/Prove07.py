""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
File: prove07.py
Author: Luis Andrade
Date: 8 november 2022
Purpose: Create a puzzle game.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Presentation of the game to the user.
print("\n Welcome to the word guessing game!.")
print("\n The Puzzle Game.")
print("\n The game contains a hidden secret word.")
print("You see is shown underscores ( _ ) for each letter of the word.")
print("You can enters a guess. If the guess is correct, the user wins and the game is over.")
print("If the guess is not correct, you can will be given a hint to help them improve their guess for the next round.")
print("The game continues prompting, you use for new guesses and showing them hints until they guess the word correctly.")
print("It all depends on what you choose as you progress through this world full of adventure and fun.")
print("\n When the game is over, the game displays the number of guesses that were made.·")
print("Good luck.  and Have Fun ")

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
    guess_counter = guess_counter  +  1
    guess_search = input ("\n What is your guess? ")
    
    for i, letter in enumerate(guess_search.lower()):
        if i < len(word_secret) and letter == word_secret[i]: 
             print("\n Your hint correctly is: ", end = " ")
             print(letter.upper(), end = " ")            
        elif letter in word_secret:
            print(letter.lower(), end = " ")
        else:
         print("_", end = " ")
    print()

#end or terminated the game with this mensage
print("Congratulations! You guessed it!")
print(f"It took you {guess_counter} guesses.")
