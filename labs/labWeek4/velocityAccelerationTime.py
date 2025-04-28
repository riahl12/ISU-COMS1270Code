#Riley Ahlrichs             2-10-2025
#Lab Week 4 - Create a function called velocityAccelerationTime that takes 3 parameters and will return
# the final velocity. The main function will gather those inputs and Use the values entered to calculate the final velocity

def velocityAccelerationTime(initial_velocityValue, accelerationValue, timeValue):
    #CITATION - URL: https://www.sciencing.com/final-velocity-object-5495923/
    #CITATION - Date Written/Posted: Mar 29, 2023
    #CITATION - Author: S. Hussain Ather
    return initial_velocityValue + (accelerationValue * timeValue)

def main():
    print("Let's calculate your final velocity!")
    initial_velocity = float(input("Enter your initial velocity in m/s: "))
    acceleration = float(input("Enter your acceleration in m/s^2: "))
    time = float(input("Enter your time value in sec: "))
    answer = velocityAccelerationTime(initial_velocity, acceleration, time)
    print(f"Your final velocity is: {answer}")

if __name__ == "__main__":
    main()