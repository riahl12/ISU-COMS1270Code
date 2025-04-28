def annualPercentageRate(interest, fee, loan, days):
    #CITATION - URL: https://www.investopedia.com/terms/a/apr.asp
    #CITATION - Date Written/Posted: Updated June 03, 2024  
    return (((interest + fee) / loan) / days) * 100

def compoundAmount(principalValue, interestRate, compound, timeValue):
    #CITATION - URL: https://www.investopedia.com/terms/c/compoundinterest.asp
    #CITATION - Date Written/Posted: Updated February 28, 2024
    return principalValue * (1 + (interestRate/100) / compound)**(compound * timeValue)

