#calculation test, run through 1-8 and show the TA all 8 options
#drawing mulitple tridecagons, 
#adventure story, make up your own story and use if else conditions
# calculationTest.py
# Author: [Your Name]
# Date: [Creation Date]
# Lab Number: [Lab Number]
# Description: This script allows users to interact with functions from different modules to perform various calculations.

import myShapes
import myPhysics
import myOhmsLaw
import myFinances

def main():
    continue_calculating = True  # Loop condition
    
    while continue_calculating:
        print("\nSelect a calculation:")
        print("1. Area of a Rectangle (myShapes)")
        print("2. Perimeter of a Rectangle (myShapes)")
        print("3. Area of a Circle (myShapes)")
        print("4. Circumference of a Circle (myShapes)")
        print("5. Distance (Physics)")
        print("6. Velocity (Physics)")
        print("7. Voltage (Ohm's Law)")
        print("8. Resistance (Ohm's Law)")
        print("9. Current (Ohm's Law)")
        print("10. Simple Interest (Finance)")
        print("11. Compound Amount (Finance)")
        print("12. Quit")

        choice = input("Enter the number corresponding to your choice: ")

        if choice == '1':
            length = float(input("Enter length of rectangle: "))
            width = float(input("Enter width of rectangle: "))
            print(f"Area of rectangle: {myShapes.areaOfRectangle(length, width)}")

        elif choice == '2':
            length = float(input("Enter length of rectangle: "))
            width = float(input("Enter width of rectangle: "))
            print(f"Perimeter of rectangle: {myShapes.rectanglePerimeter(length, width)}")

        elif choice == '3':
            radius = float(input("Enter radius of circle: "))
            print(f"Area of circle: {myShapes.areaOfCircle(radius)}")

        elif choice == '4':
            radius = float(input("Enter radius of circle: "))
            print(f"Circumference of circle: {myShapes.circleCircumference(radius)}")

        elif choice == '5':
            speed = float(input("Enter speed: "))
            time = float(input("Enter time: "))
            print(f"Distance: {myPhysics.distanceSpeedTime(speed, time)}")

        elif choice == '6':
            initial_velocity = float(input("Enter initial velocity: "))
            acceleration = float(input("Enter acceleration: "))
            time = float(input("Enter time: "))
            print(f"Velocity: {myPhysics.velocityAccelerationTime(initial_velocity, acceleration, time)}")

        elif choice == '7':
            current = float(input("Enter current: "))
            resistance = float(input("Enter resistance: "))
            print(f"Voltage: {myOhmsLaw.calculateVoltage(current, resistance)}")

        elif choice == '8':
            voltage = float(input("Enter voltage: "))
            current = float(input("Enter current: "))
            print(f"Resistance: {myOhmsLaw.calculateResistance(voltage, current)}")

        elif choice == '9':
            voltage = float(input("Enter voltage: "))
            resistance = float(input("Enter resistance: "))
            print(f"Current: {myOhmsLaw.calculateCurrent(voltage, resistance)}")

        elif choice == '10':
            principal = float(input("Enter principal: "))
            interest = float(input("Enter interest: "))
            time = float(input("Enter time (in years): "))
            print(f"Annual Percentage Rate: {myFinances.annualPercentageRate(principal, interest, time)}")

        elif choice == '11':
            principal = float(input("Enter principal: "))
            rate = float(input("Enter interest rate: "))
            time = float(input("Enter time (in years): "))
            print(f"Compound Amount: {myFinances.compoundAmount(principal, rate, time)}")

        elif choice == '12':
            running = False
            print("Goodbye!")
            
        else:
            print("Error: Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
