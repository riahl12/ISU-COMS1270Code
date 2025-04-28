                                         #Riley Ahlrichs         2-10-2025
#Lab Week 4 - Create a function called randomProduct that takes 3 parameters and calculates the product of the random numbers in 
# a range and prints it out to the console

import random

def randomProduct(a, b, c):
    product = 1         # If initialized to 0, the answer would always be 0
    for i in range(a):
        num = random.randrange(b, c + 1)
        product *= num      # Multiplying to find the number between the random range of b and c + 1
    return product
    
def main():
    a = int(input("Give me an integer: "))
    b = int(input("Give me an integer: "))
    c = int(input("Give me an integer: "))
    answer = randomProduct(a,b,c)
    print(f"The answer is: {answer}")

if __name__ == "__main__":
    main()