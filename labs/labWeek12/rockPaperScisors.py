# Riley Ahlrichs    4-18-2025
# Lab Week 12: Created a rock, paper, scissors game with a computer. You play an odd number of games and whoever wins the most games wins
# overall. If you and the computer win the same, its a draw
import random

# Function to generate the computer's move
def generateComputerMove():
    return random.choice(["Rock", "Paper", "Scissors"])

# Function to determine the winner of a round
def determineWinner(player1_move, player2_move):
    if player1_move == player2_move:
        return "Draw"
    elif (player1_move == "Rock" and player2_move == "Scissors") or \
         (player1_move == "Paper" and player2_move == "Rock") or \
         (player1_move == "Scissors" and player2_move == "Paper"):
        return player1_move
    else:
        return player2_move
        
# Function to play a single round
def playRound(player_move):
    computer_move = generateComputerMove()
    winner = determineWinner(player_move, computer_move)
    
    if winner == "Draw":
        return "It's a draw!"
    elif winner == player_move:
        return "You Win!"
    else:
        return "Computer Wins!"

# Main function to run the game
def main():
    print("Welcome to Rock, Paper, Scissors!")
    rounds = int(input("How many rounds would you like to play? (Choose an odd number): "))
    
    while rounds % 2 == 0:
        print("Please choose an odd number of rounds.")
        rounds = int(input("How many rounds would you like to play? (Choose an odd number): "))

    player_score = 0
    computer_score = 0

    for round_num in range(1, rounds + 1):
        print(f"Round {round_num}")
        player_move = input("Enter your move (Rock, Paper, or Scissors): ").capitalize()
        while player_move not in ["Rock", "Paper", "Scissors"]:
            player_move = input("Invalid move. Please enter Rock, Paper, or Scissors: ").capitalize()
        
        result = playRound(player_move)
        print(result)
        
        if result == "You Win!":
            player_score += 1
        elif result == "Computer Wins!":
            computer_score += 1

        # If one player wins more than half of the rounds, the game ends
        if player_score > rounds // 2:
            print("You won the game!")
            break
        elif computer_score > rounds // 2:
            print("Computer won the game!")
            break

    if player_score == computer_score:
        print("The game is a draw!")
    else:
        print(f"Final score: You {player_score} - Computer {computer_score}")

# Call the main function if this script is being run directly
if __name__ == "__main__":
    main()
