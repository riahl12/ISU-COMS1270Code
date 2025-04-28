#Riley Ahlrichs             2-10-2025
#Lab Week 4 - Create a function called compoundAmount that takes 4 parameters and returns the amount of 
# compound interest. The main function gathers input from the user and calls the previous function to return the 
# value to the console. 

def compoundAmount(principalValue, interestRate, compound, timeValue):
    #CITATION - URL: https://www.investopedia.com/terms/c/compoundinterest.asp
    #CITATION - Date Written/Posted: Updated February 28, 2024
    return principalValue * (1 + (interestRate/100) / compound)**(compound * timeValue)

def main():
    print("Let's calculate your compound interest!")
    principal = float(input("Enter your principal amount: "))
    rate = float(input("Enter your interest rate: "))
    number_compounds = float(input("Enter the number of times your interest compounds: "))
    time = float(input("Enter time in years: "))
    answer = compoundAmount(principal, rate, number_compounds,time)
    print(f"Your compound interest is: {answer}")

if __name__ == "__main__":
    main()