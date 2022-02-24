"""City skyline with colorfull skyscrapers, clouds, and the sun.

Breaking up a complex function: (ln. 67-94) Instead of using the window function for both the filled in box and the window pane, I added a
seperate function for the box that is called within the window function.
Try something fun!: (ln. 32-24) I used the randint function to randomize the heights and colors of the skyscrapers.
"""

__author__ = "730477365"

from turtle import Turtle, done, tracer, update
from random import randint

l: float = 50
MAX_SPEED: int = 0


def main() -> None:
    """Entry point of the skyline picture."""
    tracer(0, 0)
    nick: Turtle = Turtle()
    joe: Turtle = Turtle()
    carl: Turtle = Turtle()
    jeff: Turtle = Turtle()
    nick.speed(MAX_SPEED)
    joe.speed(MAX_SPEED)
    carl.speed(MAX_SPEED)
    jeff.speed(MAX_SPEED)
    sun(carl, 6 * l, 5.5 * l, 4 * l)
    cloud(jeff, 2 * l, 2 * l, l)
    cloud(jeff, -7.5 * l, 4 * l, l)
    i = 1
    building_x: float = l * -10.5
    while (i < 7):
        building_y: float = randint(0, 2) * 1.5 * l
        colors: list[str] = ["burlywood", "mediumpurple", "firebrick", "lemonchiffon", "salmon", "palevioletred"]
        building_color: str = colors[randint(0, 5)]
        building(nick, building_x, building_y, l * 3.5, building_y + 6 * l, building_color)
        alt_i: int = 0
        window_y: float = building_y - .5 * l
        while alt_i < (building_y + 6 * l) // (1.5 * l):
            window_x: float = building_x + .5 * l
            window(joe, window_x, window_y, l)
            window(joe, window_x + 1.5 * l, window_y, l)
            window_y = window_y - 1.5 * l
            alt_i += 1
        building_x += l * 3.5
        i += 1
    update()
    done()


def building(nick: Turtle, x: float, y: float, width: float, height: float, color: str) -> None:
    """Creates the skyskrapers that make up the skyline."""
    nick.penup()
    nick.goto(x, y)
    nick.setheading(0.0)
    nick.pendown()
    nick.pencolor("black")
    nick.fillcolor(color)
    nick.begin_fill()
    i: int = 0
    while (i < 2):
        nick.forward(width)
        nick.right(90)
        nick.forward(height)
        nick.right(90)
        i += 1
    nick.end_fill()


def box(joe: Turtle, x: float, y: float, width: float) -> None:
    """Creates the filled in box part of the windows."""
    joe.penup()
    joe.goto(x, y)
    joe.setheading(0.0)
    joe.pendown()
    joe.pencolor("dimgrey")
    joe.fillcolor("whitesmoke")
    joe.begin_fill()
    i: int = 0
    while (i < 4):
        joe.forward(width)
        joe.right(90)
        i += 1
    joe.end_fill()


def window(joe: Turtle, x: float, y: float, width: float) -> None:
    """Creates the windows on the skyscrapers."""
    box(joe, x, y, width)
    joe.penup()
    joe.goto(x, y - width * .5)
    joe.pendown()
    joe.forward(width)
    joe.penup()
    joe.goto(x + width * .5, y)
    joe.pendown()
    joe.right(90)
    joe.forward(width)
    

def sun(carl: Turtle, x: float, y: float, length: float) -> None:
    """Draws a sun."""
    carl.penup()
    carl.goto(x, y)
    carl.setheading(0.0)
    carl.pendown()
    carl.color("yellow")
    i: int = 0
    while (i < 20):
        carl.forward(length)
        carl.left(126)
        i += 1
    carl.penup()
    carl.goto(x + .5 * length, y)
    carl.setheading(0.0)
    carl.begin_fill()
    carl.pendown
    carl.color("orange")
    carl. circle(.25 * length)
    carl.end_fill()
    
    
def cloud(jeff: Turtle, x: float, y: float, radius: float) -> None:
    """Draws a cloud."""
    i: int = 0
    while (i < 3):
        jeff.penup()
        jeff.goto(x, y)
        jeff.pendown()
        jeff.color("grey")
        jeff.begin_fill()
        jeff.circle(radius)
        jeff.end_fill()
        x += radius
        i += 1


if __name__ == "__main__":
    main()