import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("black")
    
    simon = turtle.Turtle()
    simon.shape("turtle")
    simon.color("limegreen")
    simon.speed(1)
    simon.width(5)

    for i in range (1,5):
        simon.forward(100)
        simon.right(90)
        
def draw_circle():
    albert = turtle.Turtle()
    albert.shape("turtle")
    albert.color("purple")
    albert.speed(1)
    albert.width(5)

    albert.circle(100)
    
def draw_triangle():
    bob = turtle.Turtle()
    bob.shape("turtle")
    bob.color("orange")
    bob.speed(1)
    bob.width(4)

    bob.right(60)
    bob.forward(100)
    bob.right(120)
    bob.forward(100)
    bob.right(120)
    bob.forward(100)

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("black")
    
    draw_square()
    draw_circle()
    draw_triangle()

    window.exitonclick()

#draw_shapes()

def draw_deathly_hallows():
    window = turtle.Screen()
    window.bgcolor("darkblue")

    harry = turtle.Turtle()
    harry.shape("circle")
    harry.width(5)
    harry.color("gold")
    harry.speed(1)

    harry.right(60)
    harry.forward(150)
    harry.right(120)
    harry.forward(150)
    harry.right(120)
    harry.forward(150)

    harry.right(150)
    harry.forward(130)
    
    harry.left(90)
    harry.forward(75)
    harry.left(120)
    harry.forward(75)
    
    harry.circle(42)

    window.exitonclick()

draw_deathly_hallows()
