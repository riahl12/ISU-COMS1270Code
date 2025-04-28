# Riley Ahlrichs        3-5-2025
# Lab Week 7: Taking the code from the textbook and implementing different rules to have it print out a different picture.
#CITATION - URL: https://runestone.academy/ns/books/published/iowastateuniversity_thinkcspy_spring25/Strings/TurtlesandStringsandLSystems.html?lastPosition=0
#CITATION - Last Updated: March 23, 2025
#CITATION - Author: Runestone Academy

import turtle
import random
from tridecagonTurtle import tridecagonTurtle

def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'F':
        newstr = 'F++F-F+T-H+P'   # Rule 1
    elif ch == 'T':  
        newstr = 'F-F++F-F+F'
    elif ch == 'H':
        newstr = 'H'  
    elif ch == 'P':
        newstr = 'P' 
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == 'H':
            tridecagonTurtle()
        elif cmd == 'P':
            # Move the turtle to a random position on the screen
            aTurtle.penup()
            aTurtle.goto(random.randint(-200, 200), random.randint(-200, 200))  # Random position
            aTurtle.pendown()

def main():
    inst = createLSystem(4, "F")   # create the string
    print(inst)
    t = turtle.Turtle()            # create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(9)
    drawLsystem(t, inst, 65, 5)   # draw the picture
                                  # angle 60, segment length 5
    wn.exitonclick()

if __name__ == "__main__":
    main()