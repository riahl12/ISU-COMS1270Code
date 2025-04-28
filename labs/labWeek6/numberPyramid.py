# Riley Ahlrichs        2-23-2025
# Lab Week 6: This program prints a number pyramid based on user input.


def numberPyramid(num):
    for i in range(1, num + 1):
        # Print leading spaces to center the pyramid
        for j in range(num - i):
            print(" ", end="")  # Prints spaces without a newline
        
        # Print numbers for the current row
        for k in range(1, i + 1):
            print(k, end=" ")  # Prints numbers without a newline
        
        # Move to the next line after each row
        print()

def main():
    num = int(input("Enter an integer: "))
    numberPyramid(num)

if __name__ == "__main__":
    main()