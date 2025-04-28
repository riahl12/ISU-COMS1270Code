#Riley Ahlrichs             2-10-2025
#Lab Week 4 - Create a function titled annualPercentageRate that takes 4 parameters
# and uses the values entered to calculate the annual percentage ratee (APR) of a loan in the main function

def annualPercentageRate(interest, fee, loan, days):
    #CITATION - URL: https://www.investopedia.com/terms/a/apr.asp
    #CITATION - Date Written/Posted: Updated June 03, 2024  
    return (((interest + fee) / loan) / days) * 100

def main():
    print("Lets' calculate your APR!")
    interest_charges = float(input("Enter your interest charges: "))
    fees = float(input("Enter your fees: "))
    loan_amount = float(input("Enter your loan amount: "))
    days_in_term = float(input("Enter the number of days in the loan: "))
    answer = annualPercentageRate(interest_charges, fees, loan_amount, days_in_term)
    print(f"Your APR is: {answer}")

if __name__ == "__main__":
    main()