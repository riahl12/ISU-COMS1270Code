# Riley Ahlrichs        #2-13-25
# Lab Week 4: Create a function called tridecagonTurtle that takes 3 parameters and you will also pass in a turtle that is
# created outside the function and it will create a regular tridecagon shape at the coordinates the user gave.

#CITATION - URL: https://myedspace.co.uk/blog/post/what-size-exterior-and-interior-angle-regular-13-sided-polygon
#CITATION - Date Written/Posted: 1-28-2024
#CITATION - Author: MyEdSpace

import turtle

def tridecagonTurtle():
   # t.penup()           # Picking the turtle up
    #t.goto(x,y)         # The turtle will go to wherever the user enters for the x and y coordinates
    #t.pendown()         # The turtle will be set down and the program will continue

    angle = 360 / 13        #Since each angle is exactly equal, you need to take the number of sides(13), divided by 360

    for i in range(13):         # Range is 13 since it is a 13-sided shape
        turtle.forward(30)
        turtle.left(angle)

def main():
    s = int(input("Enter the length of the sides of your shape: "))
    x = int(input("Enter the x-coordinate: "))
    y = int(input("Enter the y-coordinate: "))

    window = turtle.Screen()
    window.bgcolor("lightblue")
    t = turtle.Turtle()
    t.pensize(3)

    tridecagonTurtle(s,x,y,t)       #Calling the function
    window.exitonclick()

if __name__ == "__main__":
    main()