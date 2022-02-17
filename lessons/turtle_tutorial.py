from turtle import Turtle, done
leo: Turtle = Turtle()
leo.speed(50)
leo.hideturtle()
leo.pencolor("pink")
leo.fillcolor("blue")

leo.penup()
leo.goto(0, 0)
leo.pendown()

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1  
leo.end_fill()


bob: Turtle = Turtle()
bob.pencolor("black")
bob.fillcolor("pink")

bob.penup()
bob.goto(0, 0)
bob.pendown()

i: int = 0
while (i < 3):
    bob.forward(300)
    bob.left(120)
    i += 1

side_length: float = 300

i: int = 0
while (i < 6):
    bob.forward(side_length)
    bob.left(150)
    i += 1
    

done()