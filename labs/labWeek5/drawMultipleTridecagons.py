# Riley Ahlrichs            2-17-2025
# Lab Week 5 - create a new function which draws multiple tridecagons in a line - one after the other. It will do this
# by calling your original tridecagon-drawing function multiple times in a loop

import turtle

def tridecagonTurtle(s,x,y,t):
    t.penup()           # Picking the turtle up
    t.goto(x,y)         # The turtle will go to wherever the user enters for the x and y coordinates
    t.pendown()         # The turtle will be set down and the program will continue

    angle = 360 / 13        #Since each angle is exactly equal, you need to take the number of sides(13), divided by 360

    for i in range(13):         # Range is 13 since it is a 13-sided shape
        t.forward(s)
        t.left(angle)

def drawMultipleTridecagons(s,x,y,nr,sr,t):         # New function that calls the 1st function and loops depending on how many times you repeat
    for i in range(nr):
        tridecagonTurtle(s,x + i * sr,y,t)

def main():
    s = int(input("Enter the length of the sides of your shape: "))
    x = int(input("Enter the x-coordinate: "))
    y = int(input("Enter the y-coordinate: "))
    nr = int(input("How many times do you want to repeat?: "))
    sr = int(input("How much space between shapes?: "))

    window = turtle.Screen()
    window.bgcolor("lightblue")
    t = turtle.Turtle()
    t.pensize(3)

    drawMultipleTridecagons(s,x,y,nr,sr,t)       #Calling the function
    window.exitonclick()

if __name__ == "__main__":
    main()