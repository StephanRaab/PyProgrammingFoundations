import turtle

def draw_square(turtleName):
    for i in range (1,5):
        turtleName.forward(100)
        turtleName.right(90)

def draw_square_circle():
    window = turtle.Screen()
    window.bgcolor("black")

    chuck = turtle.Turtle()
    chuck.shape("circle")
    chuck.color("yellow")
    chuck.speed(30)
    chuck.width(4)

    for i in range(1,37):
        draw_square(chuck)
        chuck.right(10)

    window.exitonclick()

draw_square_circle()
