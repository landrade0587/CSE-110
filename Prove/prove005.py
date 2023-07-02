print("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. ")
choice = input("Which one do you want to pick up?")

if choice.lower() == "match":
    print("\n You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out.  ")
    choice = input("Do you want to RUN, or HIDE behind a tree?")
    
    if choice.lower() == "run":
        print("You chose to run...")
        choice = input("Do yoou chose to eat PIZZA or TACO.")

        #if
        #elif
        #else
 
    
    elif choice.lower() == "hide":
           print (" You chose to hide ")

    
    
    else:
            print("invalid choise")


elif choice.lower() == "flaslight":
    print ("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side.")
    input("Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?")


else:
 print("invalid choice.")