# Riley Ahlrichs        3-3-2025
# Lab Week 7: When a string is reversed, its characters print out in the opposite order of their original
# configuration. Then create multiple different versions demonstrating how to reverse a string.

def reverseStringV1(str1):
    str1 = str1[::-1]
    return str1

def reverseStringV2(str2):
    str2 = "".join(reversed(str2))
    return str2

def reverseStringV3(str3):
    reversed_string = ''
    for i in range(len(str3)-1,-1, -1):       # 0-9
        reversed_string += str3[i]
    return reversed_string

def reverseStringV4(str4):
    reversed_string = ''
    # Loop through the original string from the last character to the first
    for char in str4:
        reversed_string = char + reversed_string  
    return reversed_string

def reverseStringV5(str5):
    reversed_string = ''
    # Initialize an index to the last character of the string
    index = len(str5) - 1
    # Use a while loop to iterate through the string from the end to the beginning
    while index >= 0:
        reversed_string += str5[index]  # Append the character at the current index
        index -= 1  
    return reversed_string



def main():
    str1 = input("Enter your favorite animal: ")
    answer = reverseStringV1(str1)
    print(answer)

    str2 = input("Enter a greeting: ")
    answer2 = reverseStringV2(str2)
    print(answer2)

    str3 = input("Enter your name: ")
    answer3 = reverseStringV3(str3)
    print(answer3)

    str4 = input("Enter a string: ")
    answer4 = reverseStringV4(str4)
    print(answer4)

    str5 = input("Enter a string: ")
    answer5 = reverseStringV4(str5)
    print(answer5)


if __name__ == "__main__":
    main()