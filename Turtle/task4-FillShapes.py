import turtle
#set the color to fill the shape
turtle.fillcolor('purple')

turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

#move the turtle
turtle.penup()
turtle.goto(100,0)
turtle.pendown()

#set a new fill color
turtle.fillcolor('yellow')

turtle.begin_fill()
count = 0
while (count < 4):
    turtle.forward(100)
    turtle.left(90)
    count+=1
turtle.end_fill()

#keeps the turtle window open
turtle.exitonclick()