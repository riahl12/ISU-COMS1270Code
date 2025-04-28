# Riley Ahlrichs        3-5-2025
# Lab Week 7: A string is a palindrome if its characters read forwards are the same as the characters read
# backwards. I will import my reverseString file and create 2 functions that will check if a string is a palindrome.
import reverseString

def palindromeCheckV1(str1):
    reversed_string = reverseString.reverseStringV1(str1)  # Reverse the string using reverseStringV1
    if str1 == reversed_string:  # Check if the original string is the same as the reversed string
        return f"'{str1}' is a palindrome"
    else:
        return f"'{str1}' is not a palindrome"


def palindromeCheckV2(str2):
    length = len(str2)
    for i in range(length // 2):  # Compare characters from both ends
        if str2[i] != str2[length - 1 - i]:  # If characters don't match, it's not a palindrome
            return f"'{str2}' is not a palindrome"
    return f"'{str2}' is a palindrome"


def main():
    str1 = input("Enter a string: ")  
    result1 = palindromeCheckV1(str1)  
    print(result1)

    str2 = input("Enter a string: ")
    result2 = palindromeCheckV1(str2)  
    print(result2)


if __name__ == "__main__":
    main()