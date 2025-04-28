#Riley Ahlrichs             2-10-2025
#Lab Week 4 - Create a function called calculateCurrent that takes in 2 parameters and returns the average score.
# The main function takes the input then calls the calculateCurrent function to get the output in the terminal

def calculateCurrent(voltageValue, resistanceValue):
    #CITATION - URL: https://byjus.com/physics/ohms-law/
    #CITATION - Date Written/Posted: 2020 (exact date not mentioned)
    return voltageValue / resistanceValue

def main():
    print("Let's calculate your average score!")
    voltage = float(input("Enter the voltage value: "))
    resistance = float(input("Enter the resistance value: "))
    answer = calculateCurrent(voltage, resistance)
    print(f"Your average score is: {answer}")

if __name__ == "__main__":
    main()