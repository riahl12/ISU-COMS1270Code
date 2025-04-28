# Riley Ahlrichs        2-23-2025
# Lab Week 6: This program prints a number diamond pattern based on user input.

def numberDiamond(num):
    # Iterate for both the top and bottom parts of the diamond.
    for i in range(1, num * 2):
        # Determine whether we're in the top or bottom part of the diamond
        if i <= num:
            # Top half
            spaces = num - i
            count = i
        else:
            # Bottom half
            spaces = i - num
            count = (num * 2) - i
        
        # Print leading spaces for alignment
        print(" " * spaces, end="")
        
        # Print numbers for the current row
        print(" ".join(str(x) for x in range(1, count + 1)))

def main():
    num = int(input("Enter an integer: "))
    numberDiamond(num)

if __name__ == "__main__":
    main()