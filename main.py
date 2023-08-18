#Abdullah Mutaz Alshawa
#8/18/23

import turtle

#Set up the screen
screen = turtle.Screen()
screen.title("Turtle Graphical User Interface Application")
screen.bgcolor("white")

#Create a turtle
t = turtle.Turtle()
#Set the turtle's speed
t.speed(1)

#Draw a square
for _ in range(4):
    #Move the turtle forward by 100 units
    t.forward(100)
    #Turn the turtle 90 degrees to the right
    t.right(90)

#Draw a triangle
for _ in range(3):
    t.forward(100)
    t.left(120)
#Close the turtle graphics window when clicked
screen.exitonclick()