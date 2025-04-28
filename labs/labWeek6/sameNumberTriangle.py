# Riley Ahlrichs        2-23-2025
# Lab Week 6: This program prints a triangle pattern with the same number repeated in each row based on user input.

def sameNumberTriangle(num):
    for i in range(1, num + 1):
        print(f"{i} " * i)

def main():
    num = int(input("Enter an integer: "))
    sameNumberTriangle(num)

if __name__ == "__main__":
    main()