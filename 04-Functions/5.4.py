import turtle
from figures import draw_rectangle, draw_square, draw_trangle

window = turtle.Screen()
window.bgcolor('lightgreen')
turtle.speed(5)

for position, draw in (((-250, 150), lambda: draw_square(80)),
                       ((-50, 150), lambda: draw_trangle(80)),
                       ((150, 150), lambda: draw_rectangle(100, 60)),
                       ((-250, -100), lambda: draw_square(80)),
                       ((-50, -100), lambda: draw_trangle(80)),
                       ((150, -100), lambda: draw_rectangle(100, 60))):
    turtle.penup()
    turtle.goto(*position)
    turtle.pendown()
    draw()

turtle.hideturtle()
window.mainloop()
