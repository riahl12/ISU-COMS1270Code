#Riley Ahlrichs             2-10-2025
#Lab Week 4 - Create a function called calculateVoltage that takes 2 parameters and returns the 2 parameters
# multiplied together. The main function takes input from the users and calls the first function to print
# the answer to the console. The values entered are used to calculate voltage.

def calculateVoltage(currentValue, resistanceValue):
    #CITATION - URL: https://byjus.com/physics/ohms-law/
    #CITATION - Date Written/Posted: 2020 (exact date not mentioned)
    return currentValue * resistanceValue

def main():
    print("Let's calculate your average score!")
    current = float(input("Enter the current value: "))
    resistance = float(input("Enter the resistance value: "))
    answer = calculateVoltage(current, resistance)
    print(f"Your average score is: {answer}")

if __name__ == "__main__":
    main()