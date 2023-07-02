""""""""
# File: 02Prove.py
# Author: Luis Andrade
# Purpose: Practice Assignment  in the Word Games.
# This program is Mad Libs are a type of funny story.
# Where a person is asked for words without knowing their contex.
""""""""
print()
print("Good Morning")
print("Please enter the following words in the next Mad Libs for complete:")
print("adjective: happy")
print("animal: zebra")
print("verb: sneeze")
print("exclamation: Hooray")
print("verb1: read")
print("verb2: drive")
print()
print("The other day, I was really in trouble. It all started when I saw a very")
print("______  _________  ________  down the hallway. _________! I yelled. But all")
print("I could think to do was to ________ over and over. Miraculously,")
print("that caused it to stop, but not before it tried to ________")
print("right in front of my family")
print()
# Ask for the basic information in the words
adjective = input("adjective: ")
animal = input("animal: ")
verb = input("verb: ")
exclamation = input("exclamation: ")
verb1 = input("verb1: ")
verb2 = input("verb2: ")
# Now print out the  Card with the story
print("\nYour story is:")
print("--------------------------------------------------------------------------------------")
print("The other day, I was really in trouble. It all started when I saw a very")
#print("Your name is {0}, {1} {0}.".format(last_name, first_name))
print("{0} {1} {2} down the hallway. `{3}`! I yelled. But all".format(adjective, animal, verb, exclamation.capitalize()))
#print("Your name is {}, {} {}.".format(last_name, first_name, last_name)) 
print("I could think to do was to {} over and over. Miraculously,".format(verb1))
print("that caused it to stop, but not before it tried to {}".format(verb2))
print("right in front of my family")
print()
print("-----------------------------------------------------------------------------")