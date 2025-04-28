# Riley Ahlrichs        3-5-2025
# Lab Week 7: You will create several functions that check if a string contains a certain substring

def findSubStringV1(input_string, substring):
    return input_string.find(substring)

def findSubStringV2(input_string, substring):
    if substring in input_string:  # Check if the substring is in the string
        return input_string.index(substring)  # Use .index() method to find the index
    return -1  # Return -1 if the substring is not found

def findSubStringV3(input_string, substring):
    for i in range(len(input_string) - len(substring) + 1):  # Iterate through the main string
        if input_string[i:i+len(substring)] == substring:  # Compare substring
            return i  # Return the starting index if a match is found
    return -1  # Return -1 if the substring is not found


def main():
    user_input1 = input("Enter the main string: ")
    substring1 = input("Enter the substring: ")
    index1 = findSubStringV1(user_input1, substring1)  # Call the function to find the index
    print(f"The index of the substring is: {index1}")

    user_input2 = input("Enter the main string: ")  # Take input from the user
    substring2 = input("Enter the substring: ")  # Take substring input from the user
    index2 = findSubStringV2(user_input2, substring2)  # Call the function to find the index
    print(f"The index of the substring is: {index2}")

    user_input3 = input("Enter the main string: ")  # Take input from the user
    substring3 = input("Enter the substring: ")  # Take substring input from the user
    index3 = findSubStringV2(user_input3, substring3)  # Call the function to find the index
    print(f"The index of the substring is: {index3}")


if __name__ == "__main__":
    main()