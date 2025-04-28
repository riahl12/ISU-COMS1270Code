#Riley Ahlrichs             2-3-2025
#Lab Week 3 - Use the values entered to calculate the annual percentage ratee (APR) of a loan

#CITATION - URL: https://www.investopedia.com/terms/a/apr.asp
#CITATION - Date Written/Posted: Updated June 03, 2024

print("Let's calculate your APR!")
interest_charges = float(input("Enter your interest charges: "))
fees = float(input("Enter your fees: "))
loan_amount = float(input("Enter your loan amount: "))
days_in_term = float(input("Enter the number of days in the loan: "))
apr = (((interest_charges + fees) / loan_amount) / days_in_term) * 100

print(f"Your APR is: {apr}")