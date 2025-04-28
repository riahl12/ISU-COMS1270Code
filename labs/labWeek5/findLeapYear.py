# Riley Ahlrichs        #2-17-25
# Lab Week 5: Get input from the user and create a function that will calculate whether the specified year is a leap year or not

def findLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True     #Is a leap year
            else:
                return False    #Not a leap year
        else:
            return True         #Is a leap year 
    else:
        return False            #Not a leap year

def main():
    year = int(input("Enter a year: "))
    answer = findLeapYear(year)

    if answer:
        print("Yes!")
    else:
        print("No!")

if __name__ == "__main__":
    main()