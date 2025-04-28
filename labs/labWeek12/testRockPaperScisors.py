# Riley Ahlrichs    4-18-2025
# Lab Week 12: 
from rockPaperScisors import generateComputerMove, determineWinner, playRound
from unittest.mock import patch

# Test for generateComputerMove function
def test_generate_computer_move():
    moves = ["Rock", "Paper", "Scissors"]
    for _ in range(100):
        result = generateComputerMove()
        assert result in moves, f"Expected one of {moves}, but got {result}"

# Test for determineWinner function
def test_determine_winner():
    # Rock vs Scissors -> Rock wins
    assert determineWinner("Rock", "Scissors") == "Rock"
    # Paper vs Rock -> Paper wins
    assert determineWinner("Paper", "Rock") == "Paper"
    # Scissors vs Paper -> Scissors wins
    assert determineWinner("Scissors", "Paper") == "Scissors"
    # Rock vs Paper -> Paper wins
    assert determineWinner("Rock", "Paper") == "Paper"
    # Paper vs Scissors -> Scissors wins
    assert determineWinner("Paper", "Scissors") == "Scissors"
    # Scissors vs Rock -> Rock wins
    assert determineWinner("Scissors", "Rock") == "Rock"
    # Same move -> Draw
    assert determineWinner("Rock", "Rock") == "Draw"
    assert determineWinner("Paper", "Paper") == "Draw"
    assert determineWinner("Scissors", "Scissors") == "Draw"

# Test for playRound function
def test_play_round():
  # Made it so I could actually test the choices instead of the random generator
    # Player chooses Rock, we mock computer to choose Scissors → Player should win
    with patch('rockPaperScisors.generateComputerMove', return_value='Scissors'):
        assert playRound('Rock') == 'You Win!'

    # Player chooses Rock, we mock computer to choose Paper → Computer should win
    with patch('rockPaperScisors.generateComputerMove', return_value='Paper'):
        assert playRound('Rock') == 'Computer Wins!'

    # Both choose Rock → Draw
    with patch('rockPaperScisors.generateComputerMove', return_value='Rock'):
        assert playRound('Rock') == "It's a draw!"

    # Because Scissors beats Paper
    with patch('rockPaperScisors.generateComputerMove', return_value='Scissors'):
        assert playRound('Paper') == 'Computer Wins!'

    # Paper beats Rock
    with patch('rockPaperScisors.generateComputerMove', return_value='Rock'):
        assert playRound('Paper') == 'You Win!'
    
    # Both chose Paper - Draw
    with patch('rockPaperScisors.generateComputerMove', return_value='Paper'):
        assert playRound('Paper') == "It's a draw!"

    # Scissors beats Paper
    with patch('rockPaperScisors.generateComputerMove', return_value='Paper'):
        assert playRound('Scissors') == "You Win!"

    # Rock beats Scissors
    with patch('rockPaperScisors.generateComputerMove', return_value='Rock'):
        assert playRound('Scissors') == 'Computer Wins!'

    # Both chose Scissors - Draw
    with patch('rockPaperScisors.generateComputerMove', return_value='Scissors'):
        assert playRound('Scissors') == "It's a draw!"
    
 # # Assume the human plays Rock, and the computer plays Paper
    # result = playRound("Rock")
    # assert result == "Computer Wins!"  # Because Paper beats Rock
    
    # # Assume the human plays Paper, and the computer plays Scissors
    # result = playRound("Paper")
    # assert result == "Computer Wins!"  # Because Scissors beats Paper
    
    # # Assume the human plays Scissors, and the computer plays Rock
    # result = playRound("Scissors")
    # assert result == "Computer Wins!"  # Because Rock beats Scissors
    
    # # Assume the human plays Rock, and the computer plays Rock
    # result = playRound("Rock")
    # assert result == "It's a draw!"  # Because both players played Rock
    
    # # Assume the human plays Paper, and the computer plays Paper
    # result = playRound("Paper")
    # assert result == "It's a draw!"  # Because both players played Paper
    
    # # Assume the human plays Scissors, and the computer plays Scissors
    # result = playRound("Scissors")
    # assert result == "It's a draw!"  # Because both players played Scissors