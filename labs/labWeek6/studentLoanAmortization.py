# Riley Ahlrichs        #2-23-25
# Lab Week 6: you will program a Python script which calculates the monthly payment on a loan, repeatedly
# subtracts that monthly payment from the remaining balance, and which then prints out a table similar to the
# one at the bottom of the article

def studentLoanAmortization(principal, yearlyInterestRate, numberOfYears):
    monthlyInterestPayment = yearlyInterestRate / 12    # Get the monthly interest rate
    numberOfMonths = numberOfYears * 12     #Get the number of months to pay off loan

    #Monthly payment using Amortization formula
    monthlyPayment = principal * (monthlyInterestPayment * (1 + monthlyInterestPayment)**numberOfMonths) / ((1 + monthlyInterestPayment)**numberOfMonths - 1)

    print("Period | Total Payment Due  | Computed Interest Due| Principal Due |  Principal Balance")  #Column labels
    

    currentBalance = principal
    for period in range(1, numberOfMonths + 1):
        # Calculate interest for the current period
        interestDue = currentBalance * monthlyInterestPayment
        # Calculate the principal payment
        principalDue = monthlyPayment - interestDue
        # Update the remaining balance
        currentBalance -= principalDue

        print(f"{period:6} | {monthlyPayment:18.2f} | {interestDue:20.2f} | {principalDue:13.2f} | {currentBalance:17.2f}")
    
def main():
    principal = float(input("Enter the principal amount: "))
    yearlyInterestRate = float(input("Enter the yearly interest rate (as a decimal): "))
    numberOfYears = int(input("Enter the number of years: "))

    studentLoanAmortization(principal, yearlyInterestRate, numberOfYears)

if __name__ == "__main__":
    main()