import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("blue")

    brad = turtle.Turtle()
    count = 0;
    while(count < 1000):        
        brad.forward(1)
        brad.right(0.36)
        count += 1

    window.exitonclick()


draw_square()
