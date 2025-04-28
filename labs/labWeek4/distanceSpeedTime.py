#Riley Ahlrichs             2-10-2025
#Lab Week 4 - Create a function called distanceSpeedTime that takes in 2 parameters and will return the distance
# calculation. The main function will gather the input from the user and use the values entered to calculate the distance traveled

def distanceSpeedTime(speedValue, timeValue):
    #CITATION - URL: https://www.geeksforgeeks.org/speed-time-distance/
    #CITATION - Date Written/Posted: Last Updated : 28 Oct, 2024 
    return speedValue * timeValue

def main():
    print("Let's calculate your distance traveled!")
    speed = float(input("Enter your speed value in m/s: "))
    time = float(input("Enter your time value in sec: "))
    answer = distanceSpeedTime(speed, time)
    print(f"The distance you traveled is: {answer}")

if __name__ == "__main__":
    main()