import turtle
import random

turtle.colormode(255)
palette = [(5, 30, 62), (37, 30, 62), (69, 30, 62),
           (69, 30, 62), (133, 30, 62)]

window = turtle.Screen()
window.setup(width=800, height=800)
window.bgcolor("black")


def make_turtle(pos=(0, 0), speed=10, color="white", shape="turtle", width=2):
    turt = turtle.Turtle(shape)
    turt.pencolor(color)
    turt.pensize(width)
    turt.penup()
    turt.setpos(pos)
    turt.pendown()
    turt.speed(speed)
    return turt


def recaman(turt, head1=90, head2=270, max_range=200, scale=5, fill=False, divide=1):

    def random_circle():

        for i in range(1, divide + 1):
            color1 = random.choice(palette)
            color2 = random.choice(palette)
            if i % 2 == 0:
                turt.pencolor(color1)
                turt.fillcolor(color2)
            else:
                turt.pencolor(color2)
                turt.fillcolor(color1)
            if fill: turt.begin_fill()
            turt.circle(scale * step_size / 2, 180 / divide)
            if fill: turt.end_fill()

    current = 0
    seen = set()
    for step_size in range(1, max_range):
        back = current - step_size
        if back > 0 and back not in seen:
            turt.setheading(head1)
            random_circle()
            current = back
            seen.add(current)

        else:
            turt.setheading(head2)
            random_circle()
            current += step_size
            seen.add(current)


turtles = [make_turtle((-275, 200), speed=0, width=2),
           make_turtle((-275, -200), speed=0, width=2),
           make_turtle((-400, 0), speed=0, width=1),
           make_turtle((-400, 0), speed=0, width=3),
           make_turtle((-400, 0), speed=0, width=5)]

recaman(turtles[0], scale=5)
recaman(turtles[1], scale=5)

recaman(turtles[2], scale=10, fill=True, max_range=100)
recaman(turtles[3], scale=10, fill=True, max_range=100, divide=3)
recaman(turtles[4], scale=10, fill=False, max_range=100, divide=16)

turtle.done()
