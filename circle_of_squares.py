import turtle

def draw_square(some_turtle, angle):
    count = 0;
    some_turtle.right(angle)
    while(count < 4):        
        some_turtle.forward(100)
        some_turtle.right(90)
        count += 1

def draw_art():        
    window = turtle.Screen()
    window.bgcolor("blue")

    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("white")
    brad.speed(5)
    angle = 0
    while (angle < 360):
        draw_square(brad, 10)
        angle += 10

    window.exitonclick()


draw_art()
