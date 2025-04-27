# Riley Ahlrichs        3-3-2025
# Assignment 3 - NimGrab
# Here is my fun rendition of the game NimGrab!
import random

print("\nLet's play NIMGRAB!\n")
print("By: Riley Ahlrichs")
print("{COMS 1270 Section 1}")

def display_rules():
    print("""
    ** Rules of NIMGRAB! **
    1. The goal is to avoid being the last player to take the last item!
    2. Players alternate turns, removing between 1 - 3 items.
    3. You can't take more items than are left in the row.
    4. The player who takes the last item loses.
    5. The winner will be displayed to the screen.
    6. This game can be played in 1-player or 2-player mode.
    """)

def display_items(items_left):
    # Create a string with each item represented by '*'
    items_display = "* " * items_left
    print(f"Items left: {items_left}")
    print(items_display.strip())  # Remove the trailing space

def players_turn(player, items_left, X, Y):
    print(f"{player}'s turn.")
    
    # Loop until valid input is given
    while True:
        # Ask for input
        take_input = input(f"How many items will you take? (between {X} and {Y}): ")
        
        # Check if the input is a valid number and within the range
        if take_input.isnumeric():
            take = int(take_input)  # Convert to integer
            if X <= take <= Y and take <= items_left:
                break  # Exit the loop when a valid input is given
            else:
                print(f"Invalid move! You can only take between {X} and {Y} items. Try again.")
        else:
            print("Invalid input! Please enter a number.")
    
    items_left -= take
    display_items(items_left)  # Show updated items after the turn
    return items_left

def computers_turn(items_left, X, Y):    # This helps to make sure the computer doesn't do anything 'catastrophic'
    # Handle the case where there are only 1 or 2 items left
    if items_left == 1:
        take = 1  # Take the last item and lose
        print(f"Computer takes {take} item.")
    elif items_left == 2:
        take = 1  # Take 1 item to leave the last item for the player to take and loose
        print(f"Computer takes {take} item.")
    elif items_left == 3:
        take = 2  # Take 2 items to leave the last item for the player to take and loose
        print(f"Computer takes {take} items.")
    else:
        # Otherwise, take a random number between X and Y
        take = random.randint(X, Y)
        if take > items_left:
            take = items_left  # If the number is too large, take all remaining items
        print(f"Computer takes {take} items.")
    
    items_left -= take
    display_items(items_left)  # Show updated items after the computer's turn
    return items_left

def check_for_loser(items_left):    # This is to help with returning the winner of the game
    if items_left == 0:
        return True
    return False

def play_game(player_mode):
    items_left = random.randint(20, 25)  # Random number of items between 20 and 25
    X, Y = 1, 3  # Can take between 1 and 3 items each turn, decided to hard code this in

    print(f"Starting the game off with {items_left} items.\n")
    display_items(items_left)  # Show initial items at the start

    while True:
        if player_mode == 1:  # 1-player mode
            # Human player's turn
            items_left = players_turn("Player", items_left, X, Y)
            if check_for_loser(items_left):
                print("Player loses! You took the last item.")
                print("Computer wins!")
                break
            # Computer's turn
            items_left = computers_turn(items_left, X, Y)
            if check_for_loser(items_left):
                print("Computer loses! It took the last item.")
                print("Player wins!")
                break
        else:  # 2-player mode
            # Player 1's turn
            items_left = players_turn("Player 1", items_left, X, Y)
            if check_for_loser(items_left):
                print("Player 1 loses! Player 1 took the last item.")
                print("Player 2 wins!")
                break
            # Player 2's turn
            items_left = players_turn("Player 2", items_left, X, Y)
            if check_for_loser(items_left):
                print("Player 2 loses! Player 2 took the last item.")
                print("Player 1 wins!")
                break

def main():
    while True:
        print("\n1. Play 1-player mode - against a computer")
        print("2. Play 2-player mode - against a human")
        print("3. Read rules")
        print("4. Quit")
        
        choice = input("Please select an option 1 - 4: ")
        
        if choice == '1':
            play_game(1)  # 1-player mode against computer
        elif choice == '2':
            play_game(2)  # 2-player mode
        elif choice == '3':
            display_rules()
        elif choice == '4':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
