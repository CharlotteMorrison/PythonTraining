import turtle


def fractal(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        fractal(length / 3, depth - 1)
        turtle.right(60)
        fractal(length / 3, depth - 1)
        turtle.left(120)
        fractal(length / 3, depth - 1)
        turtle.right(60)
        fractal(length / 3, depth - 1)


def koch(order, size):
    if order == 0:
        #base case is just a straight line
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
           koch(order-1, size/3)
           turtle.left(angle)


turtle.fillcolor('purple')
turtle.penup()
turtle.goto(-200,0)
turtle.pendown()

turtle.begin_fill()
fractal(400, 4)

turtle.penup()
turtle.goto(-200,0)
turtle.pendown()

koch(4, 400)
turtle.end_fill()
turtle.exitonclick()