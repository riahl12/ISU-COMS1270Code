# Riley Ahlrichs        3-29-2025
# Lab Week 10: This program takes a list of integers and rotates it based on user input.

def getInput():
    # Function to collect integer input from the user
    intList = []
    while True:
        user_input = input("Enter an integer (or '*' to stop): ")
        if user_input == '*':
            break
        else:
            intList.append(int(user_input))
    return intList

def rotateList(intList, rot):
    # Function to rotate the list by 'rot' positions (right for positive, left for negative)
    length = len(intList)
    
    if length == 0:
        return intList
    
    # Normalize the rotation value (in case rot is greater than the length of the list)
    rot = rot % length  # This ensures that the rotation works even for values greater than the list length
    
    if rot == 0:
        return intList
    elif rot > 0:
        # Rotate to the right
        return intList[-rot:] + intList[:-rot]
    else:
        # Rotate to the left
        return intList[-rot:] + intList[:-rot]

def main():
    # Step 1: Get the list of integers
    intList = getInput()

    # Step 2: Get the rotation value
    rot = int(input("Enter the number of positions to rotate the list: "))

    # Step 3: Call rotateList() to rotate the list
    rotated_list = rotateList(intList, rot)

    # Step 4: Print the rotated list
    print(f"Rotated list: {rotated_list}")

# Ensure that the main function is only called when the script is executed directly
if __name__ == "__main__":
    main()