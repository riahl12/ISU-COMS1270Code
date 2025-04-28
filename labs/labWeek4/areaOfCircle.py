#Riley Ahlrichs             2-10-2025
#Lab Week 4 - Create a function called areaOfCircle that takes in 2 parameters to return the area of a circle
# and uses the main function to collect the values entered to calculate the area of a circle 

import math

def areaOfCircle(radiusValue):
    #CITATION - URL: https://www.geeksforgeeks.org/area-of-a-circle/
    #CITATION - Date Written/Posted: Last Updated : 14 Jan, 2025 
    num = math.pi
    return num * (radiusValue ** 2)

def main():
    print("Let's find the area of a circle!")
    radius = float(input("Enter radius value: "))
    answer = areaOfCircle(radius)
    print(f"The area of the circle is: {answer}")

if __name__ == "__main__":
    main()