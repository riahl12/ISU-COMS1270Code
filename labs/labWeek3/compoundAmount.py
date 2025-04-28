#Riley Ahlrichs             2-3-2025
#Lab Week 3 - Use the values entered to calculate compound interest 

#CITATION - URL: https://www.investopedia.com/terms/c/compoundinterest.asp
#CITATION - Date Written/Posted: Updated February 28, 2024

print("Let's calculate your compound interest!")
principal = float(input("Enter your principal amount: "))
rate = float(input("Enter your interest rate: "))
number_compounds = float(input("Enter the number of times your ineterst compounds: "))
time = float(input("Enter time in years: "))
accrued_amount = principal * (1 + (rate/100) / number_compounds)**(number_compounds
* time)

print(f"Your compound interest is: {accrued_amount}")