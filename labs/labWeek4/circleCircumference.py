#Riley Ahlrichs             2-10-2025
#Lab Week 4 - Create a function called circleCircumference that takes 1 parameter and uses the math library to 
# calculate the circumference of a circle. The main function gets input from the user and and prints the 
# answer to the console.
import math

def circleCircumference(radiusValue):
    #CITATION - URL: https://tutors.com/lesson/what-is-circumference-definition-equation
    #CITATION - Date Written/Posted: January 26, 2023
    #CITATION - Author: Malcolm McKinsey
    num = math.pi
    return 2 * num * radiusValue

def main():
    print("Let's find the circumference of a circle!")
    radius = float(input("Enter radius value: "))
    answer = circleCircumference(radius)
    print(f"The circumference of the circle is: {answer}")

if __name__ == "__main__":
    main()