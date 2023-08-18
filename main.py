import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Graphical User Interface Application")
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
# Set the turtle's speed
t.speed(10)

# Draw the base of the house (square)
for _ in range(4):
    t.forward(100)
    t.right(90)

# Draw the roof (triangle)
t.fillcolor("red")  # Set the fill color for the roof
t.begin_fill()      # Begin filling the shape
for _ in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()        # End filling the shape

# Draw a window
t.penup()           # Lift the pen to move to a new location
t.goto(40, 0)       # Move the turtle to the desired position for the window
t.pendown()         # Lower the pen to start drawing
t.fillcolor("blue") # Set the fill color for the window
t.begin_fill()      # Begin filling the shape
for _ in range(4):
    t.forward(20)
    t.right(90)
t.end_fill()        # End filling the shape

# Draw a door
t.penup()           # Lift the pen to move to a new location
t.goto(35, -30)    # Move the turtle to the desired position for the door
t.pendown()         # Lower the pen to start drawing
t.fillcolor("brown")# Set the fill color for the door
t.begin_fill()      # Begin filling the shape
for _ in range(2):
    t.forward(30)
    t.right(90)
    t.forward(70)
    t.right(90)
t.end_fill()        # End filling the shape

# Hide the turtle
t.hideturtle()

# Close the turtle graphics window when clicked
screen.exitonclick()
