# Riley Ahlrichs        2-23-2025
# Lab Week 6: Will print out a right triangle pattern with * based on the users input

def starRightTriangle(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

def main():
    num = int(input("Enter an integer: "))
    starRightTriangle(num)

if __name__ == "__main__":
    main()