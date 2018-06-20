import turtle

#set up a counter
count = 0
while (count < 4):
    turtle.forward(100)
    turtle.left(90)
    count+=1

turtle.goto(25,25)
#reset counter
count = 0
while (count < 4):
    turtle.forward(100)
    turtle.left(90)
    count+=1

#keeps the turtle window open
turtle.exitonclick()