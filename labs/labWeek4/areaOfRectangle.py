#Riley Ahlrichs             2-10-2025
#Lab Week 4 - Create a function called areaOfRectangle that takes in 2 parameters and returns the area which is 
# those 2 parameters multiplied by each other. The main function will use the values entered above to calculate the area of the rectangle

def areaOfRectangle(baseValue, heightValue):
    #CITATION - URL: https://www.geeksforgeeks.org/area-of-rectangle/
    #CITATION - Date Written/Posted:  Last Updated : 15 Oct, 2024 
    return baseValue * heightValue

def main():
    print("Let's find the area of a rectangle!")
    base = float(input("Enter base value: "))
    height = float(input("Enter height value: "))
    answer = areaOfRectangle(base, height)
    print(f"The area of the rectangle is: {answer}")

if __name__ == "__main__":
    main()