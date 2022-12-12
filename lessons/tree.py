import turtle as t


def tree(x: float, y: float) -> None:
    t.penup()
    t.goto(x, y)
    t.pendown()
    TRUNK = 100.0
    UP = 90.0
    branch(TRUNK, UP)
    # t.update()


def branch(length: float, angle: float) -> None:
    t.setheading(angle)
    t.forward(length)
    if length < 3.0:
        ...  # Do Nothing, this is the base case
    else:
        branch(length * 0.55, angle + 25.0)
        branch(length * 0.60, angle - 25.0)
    t.setheading(angle + 180.0)
    t.forward(length)


# t.tracer(0, 0)  # This only updates when you call t.update()
t.speed(0)
# t.getscreen().onclick(tree)
tree(0, 0)
t.done()