# Riley Ahlrichs        3-29-2025
# Lab Week 10: This program takes a list of integers, then moves all occurrences of a given number to the end while maintaining the order of the other elements.

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

def endNum(intList, num):
    # Function to move all occurrences of 'num' to the end of the list while maintaining order
    result = [x for x in intList if x != num]  # List of non-'num' elements
    result.extend([num] * intList.count(num))  # Add 'num' to the end
    return result

def main():
    # Step 1: Get the list of integers
    intList = getInput()

    # Step 2: Get the number to move to the end
    num = int(input("Enter the number to move to the end: "))

    # Step 3: Call endNum() to rearrange the list
    rearranged_list = endNum(intList, num)

    # Step 4: Print the rearranged list
    print(f"Rearranged list: {rearranged_list}")


if __name__ == "__main__":
    main()