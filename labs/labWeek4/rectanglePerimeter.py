#Riley Ahlrichs             2-10-2025
#Lab Week 4 - Create a function called rectanglePerimeter that takes in 2 paramters and will return the value of 
# the perimeter of a rectangle. The main function will gather input from the user and pass that to the first function
# and use the values entered to calculate the perimeter of the rectangle

def rectanglePerimeter(lengthValue, widthValue):
    #CITATION - URL: https://www.geeksforgeeks.org/perimeter-of-rectangle/
    #CITATION - Date Written/Posted:   Last Updated : 13 Jan, 2025 
    return 2 * (lengthValue + widthValue)

def main():
    print("Let's find the perimeter of a rectangle!")
    length = float(input("Enter length value: "))
    width = float(input("Enter width value: "))
    answer = rectanglePerimeter(length, width)
    print(f"The perimeter of a rectangle is: {answer}")

if __name__ == "__main__":
    main()