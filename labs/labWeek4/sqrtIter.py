# Riley Ahlrichs        #2-13-25
# Lab Week 4: Create a function that takes 2 parameters so that we can calculate the value we want to find the 
# square root of.

#CITATION - URL: https://www.cuemath.com/algebra/square-root-of-2/
#CITATION - Date Accessed: 2-13-2025
#CITATION - Author: CueMath


def sqrtIter(x, iterations):    # Function takes in 2 parameters
    y = (x + 1) / 2             # Stating the 'initial guess' for y, lab mentioned it would be 1
    for i in range(iterations):
        y = ((x / y ) + y) / 2      # You'll iterate to get the sqare root
    return y

def main():     # Gathering our 2 inputs and calling the sqrtIter function and printing the result
    x = int(input("Please enter the number you want to know the sqr. root of: "))
    iterations = int(input("Please enter the number of times you want to iterate: "))
    answer = sqrtIter(x, iterations)
    print(f"The answer is: {answer}")

if __name__ == "__main__":
    main()