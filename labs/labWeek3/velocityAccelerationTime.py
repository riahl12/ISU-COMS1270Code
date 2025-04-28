#Riley Ahlrichs             2-3-2025
#Lab Week 3 - Use the values entered to calculate the final velocity

#CITATION - URL: https://www.sciencing.com/final-velocity-object-5495923/
#CITATION - Date Written/Posted: Mar 29, 2023
#CITATION - Author: S. Hussain Ather

print("Let's calculate your final velocity!")
initial_velocity = float(input("Enter your initial velocity in m/s: "))
acceleration = float(input("Enter your acceleration in m/s^2: "))
time = float(input("Enter your time value in sec: "))
final_velocity = initial_velocity + (acceleration * time)

print(f"Your final velocity is: {final_velocity}")