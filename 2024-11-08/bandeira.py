import turtle

def bandeira_portugal(t, side, x, y):
    t.hideturtle()
    t.teleport(x, y)

    retangulo(t, 2 * side / 5, 2 * side / 3, 'green', 'green')

    t.teleport(x + 2 * side / 5, y)
    retangulo(t, 3 * side / 5, 2 * side / 3, 'red', 'red')

    t.teleport(x + 2 * side / 5, y + 2 * side / 3 / 2)
    t.pencolor('yellow')
    t.dot(side / 3)

def retangulo(t, base, altura, line, fill):
    t.setheading(0)
    t.pencolor(line)
    t.fillcolor(fill)
    t.begin_fill()
    for _ in range(2):
        t.forward(base)
        t.left(90)
        t.forward(altura)
        t.left(90)
    t.end_fill()

bandeira_portugal(turtle.Turtle(), 300, 200, -300)