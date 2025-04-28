# Riley Ahlrichs    4-18-2025
# Lab Week 12: 

from fourInSequence import checkAdjacent, checkForNextMoveWin, checkDraw, checkWinner

testBoard = [
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."]
]

def test_checkForNextMoveWin():
    test_board = [
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    ["X", "X", "X", ".", ".", ".", "."],
    ["O", "O", "O", "O", ".", ".", "."]
]
    test_board_copy = [
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        ["X", "X", ".", ".", ".", ".", "."],
        ["O", "O", ".", ".", ".", ".", "."]
    ]
# Test where the next move would win the game

    # Simulate the board state before the move
    test_board[5][0] = "X"  # Player 1's move

    assert checkForNextMoveWin(test_board, 1) == 3  # Assume this move wins the game

    # Test where the next move does not win the game
    test_board_copy[5][1] = "X"  # Move does not win
    assert checkForNextMoveWin(test_board_copy, 1) == -1

# Test for checkAdjacent function
def test_checkAdjacent():
    # Test for a game board where adjacent pieces exist
    testBoard = [
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."]
    ]
    
   # Test where no adjacent pieces exist
    result = checkAdjacent(testBoard, 1)
    print(f"checkAdjacent returned (no adjacents): {result}")
    assert result == -1  # No adjacent pieces should be found in this case

    # Test where player 1 has adjacent pieces
    testBoard[5][2] = "X"  # Place a piece to create adjacency
    result = checkAdjacent(testBoard, 1)
    print(f"checkAdjacent returned (adjacents): {result}")
    assert result != -1 

# Test for checkDraw function
def test_checkDraw():
    # Test case where the board is not yet full (not a draw)
    assert checkDraw(testBoard) == False

    # Test case where the board is full but no winner (draw)
    full_board = [
        ["X", "O", "X", "O", "X", "O", "X"],
        ["O", "X", "O", "X", "O", "X", "O"],
        ["X", "O", "X", "O", "X", "O", "X"],
        ["O", "X", "O", "X", "O", "X", "O"],
        ["X", "O", "X", "O", "X", "O", "X"],
        ["O", "X", "O", "X", "O", "X", "O"]
    ]
    assert checkDraw(full_board) == True  # Board is full and no winner, so it's a draw

# Test for checkWinner function
def test_checkWinner():
    # Test case where player 1 wins (horizontal, vertical, diagonal, etc.)
    testBoard[5][0] = "X"
    testBoard[4][0] = "X"
    testBoard[3][0] = "X"
    testBoard[2][0] = "X"  # Player 1 forms a vertical line in column 0
    assert checkWinner(testBoard, 1) == True # Player 1 is the winner

    # Test case where there is no winner (board is not full yet)
    assert checkWinner(testBoard, 1) == True  # No winner yet

    # Test case for a draw situation
    full_board_no_winner = [
    ["X", "O", "X", "O", "X", "X", "X"],
    ["O", "O", "X", "X", "O", "X", "O"],
    ["X", "X", "X", "O", "O", "O", "X"],
    ["O", "O", "O", "X", "X", "X", "O"],
    ["X", "X", "X", "O", "O", "O", "X"],
    ["O", "X", "O", "X", "O", "X", "O"]
]
    assert checkWinner(full_board_no_winner, 1) == False  # No winner in this draw situation