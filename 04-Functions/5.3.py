import turtle
from figures import draw_square

window = turtle.Screen()
window.bgcolor('lightgreen')
turtle.speed(5)
draw_square(100)
turtle.hideturtle()
window.mainloop()
