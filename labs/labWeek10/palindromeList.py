# Riley Ahlrichs        3-29-2025
# Lab Week 10: This program takes a list of strings as input and checks if the list is palindromic.

def palindromeList(palList):
    # Check if the list is palindromic by comparing corresponding elements from both ends
    for i in range(len(palList) // 2):  # Only loop through the first half
        if palList[i] != palList[len(palList) - 1 - i]:  # Compare from start and end
            return False
    return True

def getInput():
    # Initialize an empty list to store the strings
    palList = []
    
    # Loop to take input from the user
    while True:
        user_input = input("Enter a word (or '*' to stop): ")
        if user_input == '*':
            break
        palList.append(user_input)
    
    return palList

def main():
    # Get the list of strings from user input
    palList = getInput()

    # Check if the list is palindromic
    is_palindrome = palindromeList(palList)

    # Print the result
    print(f"Is the list palindromic? {is_palindrome}")


if __name__ == "__main__":
    main()
