import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
pen = turtle.Turtle()
pen.color("black" , "White")
pen.pensize(10)

# Draw the letter 'S'

pen.circle(50, 180)
pen.penup()
pen.rt(180)
pen.circle(-50 , 180)
pen.pendown()
pen.circle(-50 , 60)
pen.rt(180)
pen.circle(50, 240)
pen.circle(-50, 240)

# Hide the turtle and display the window

turtle.done()
