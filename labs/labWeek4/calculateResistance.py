#Riley Ahlrichs             2-10-2025
#Lab Week 4 - Create a function called calculateResistance that takes in 2 parameters and returns the power consumption
# The main function will get input from the user and call the calculateResistance function to output an answer

def calculateResistance(voltageValue, currentValue):
    #CITATION - URL: https://byjus.com/physics/ohms-law/
    #CITATION - Date Written/Posted: 2020 (exact date not mentioned)
    return voltageValue / currentValue

def main():
    print("Let's calculate your power consumption!")
    voltage = float(input("Enter the voltage value: "))
    current = float(input("Enter the current value: "))
    answer = calculateResistance(voltage, current)
    print(f"Your power consumption is: {answer}")

if __name__ == "__main__":
    main()