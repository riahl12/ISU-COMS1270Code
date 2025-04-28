# Riley Ahlrichs        3-29-2025
# Lab Week 10: This program takes a list of integers as input, finds the minimum and maximum values, and prints them.

def findMin(numbers):
    # Initialize the first element as the minimum value
    min_value = numbers[0]
    
    # Go through the list to find the minimum value
    for num in numbers:
        if num < min_value:
            min_value = num
    
    return min_value

def findMax(numbers):
    # Initialize the first element as the maximum value
    max_value = numbers[0]
    
    # Go through the list to find the maximum value
    for num in numbers:
        if num > max_value:
            max_value = num
    
    return max_value

def getInput():
    # Initialize an empty list to store the input numbers
    numbers = []
    
    # While loop to take input from the user
    while True:
        user_input = input("Enter a number (or '*' to stop): ")
        if user_input == '*':
            break
        numbers.append(user_input)
    
    return numbers

def main():
    # Get user input from another function
    string_of_numbers = getInput()

    # Convert the list of strings to a list of integers
    numbers = [int(num) for num in string_of_numbers]

    min_value = findMin(numbers)
    max_value = findMax(numbers)

    print(f"The minimum value is: {min_value}")
    print(f"The maximum value is: {max_value}")

if __name__ == "__main__":
    main()