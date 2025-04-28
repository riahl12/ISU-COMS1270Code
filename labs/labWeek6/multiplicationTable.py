# Riley Ahlrichs        2-23-2025
# Lab Week 6: Create a function with 2 integer inputs that will use a nested loop to create a multiplication table.

def multiplicationTable(lowNum, highNum):
    for i in range(lowNum, highNum + 1):
        for j in range(lowNum, highNum + 1):
            print(f"{i * j}".rjust(4), end=" ")
        print()

def main():
    lowNum = int(input("Enter the low number: "))
    highNum = int(input("Enter the high number: "))

    multiplicationTable(lowNum,highNum)


if __name__ == "__main__":
    main()