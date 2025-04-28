# Riley Ahlrichs        #2-20-25
# Lab Week 5: write a short interactive 'story' using if statements to control the flow of the narrative,
# and the input() function to let the user decide what to do next.


def main():
    print("Welcome to your Mysterious Adventure Story!")
    print("By: Riley Ahlrichs")

    print("\nYou find yourself in a mysterious forest with three paths ahead of you.")
    choice1 = input("Do you want to go [left], [right], or [forward]?: ").lower()
    
    if choice1 == "left":
        print("\nYou walk down the left path and discover a deep dark cave.")
        choice2 = input("Do you want to [enter] the cave, or [leave] it?: ").lower()
        
        if choice2 == "enter":
            print("\nInside the cave, you find a glowing crystal!")
            choice3 = input("Do you want to [take] the crystal or [leave] it?: ").lower()
            
            if choice3 == "take":
                print("\nThe crystal grants you magical powers! You win!")
            elif choice3 == "leave":
                print("\nYou leave the crystal behind and exit the cave safely. You win!")
            else:
                print("\nThat wasn't an option! You walk out of the cave with no crystal.")
        elif choice2 == "leave":
            print("\nYou decide to leave the cave and head back to the forest.")
        else:
            print("\nThat wasn't an option! You stand there indecisively.")
    
    elif choice1 == "right":
        print("\nYou walk down the right path and encounter a giant spider!")
        choice2 = input("Do you want to [fight] the spider, or [run] away?: ").lower()
        
        if choice2 == "fight":
            print("\nYou fight the spider bravely and win! You continue your adventure.")
        elif choice2 == "run":
            print("\nYou run away from the spider, safely returning to the forest.")
        else:
            print("\nThat wasn't an option! You get tangled in the web!")
    
    elif choice1 == "forward":
        print("\nYou walk straight ahead and stumble upon a beautiful waterfall.")
        choice2 = input("Do you want to [swim] in the waterfall, or [rest] by the shore?: ").lower()
        
        if choice2 == "swim":
            print("\nYou swim in the waterfall and discover a hidden underwater cave!")
            choice3 = input("Do you want to [explore] the cave, or [leave] it?: ").lower()
            
            if choice3 == "explore":
                print("\nInside the cave, you find a treasure chest! You win!")
            elif choice3 == "leave":
                print("\nYou swim out of the cave and return to the shore.")
            else:
                print("\nThat wasn't an option! You swim back to the shore.")
        elif choice2 == "rest":
            print("\nYou rest by the shore and enjoy the peaceful sound of the waterfall.")
        else:
            print("\nThat wasn't an option! You sit in the wet sand, unsure what to do next.")
    
    else:
        print("\nThat wasn't an option! You stand still and do nothing.")
    
    print("\nThank you for playing! You have completed the adventure.")

if __name__ == "__main__":
    main()