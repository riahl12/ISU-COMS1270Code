#Riley Ahlrichs                        2-2-2025
#Lab Week 3 - Using the turtle module to draw a picture of my initials using 2 turtles

import turtle

window = turtle.Screen()
window.bgcolor("lightpink")

#Creating the first turtle for the letter 'R'
zippy = turtle.Turtle()
zippy.pencolor("red")
zippy.fillcolor("white")
zippy.pensize(5)

zippy.up()
zippy.backward(100)     #Moving the first letter 'over' to the left to make room
zippy.down()
zippy.begin_fill()
zippy.backward(100)
zippy.right(90)
zippy.forward(110)
zippy.left(180)
zippy.forward(200)
zippy.right(90)
zippy.forward(100)
zippy.right(90)
zippy.forward(90)
zippy.left(90)
zippy.backward(50)
zippy.right(50)
zippy.forward(140)
zippy.end_fill()

# Creating a second turtle for the letter 'A'
zappy = turtle.Turtle()
zappy.pencolor("purple")
zappy.fillcolor("blue")
zappy.pensize(5)

zappy.begin_fill()
zappy.right(100)
zappy.forward(110)
zappy.left(180)
zappy.forward(200)
zappy.right(145)
zappy.forward(210)
zappy.left(180)
zappy.forward(80)
zappy.left(70)
zappy.forward(75)
zappy.end_fill()

turtle.done()