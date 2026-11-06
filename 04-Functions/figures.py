import turtle


def draw_square(length):
    for _ in range(4):
        turtle.forward(length)
        turtle.right(90)


def draw_trangle(length):
    for _ in range(3):
        turtle.forward(length)
        turtle.left(120)


def draw_rectangle(length_a, length_b):
    for _ in range(2):
        turtle.forward(length_a)
        turtle.right(90)
        turtle.forward(length_b)
        turtle.right(90)
