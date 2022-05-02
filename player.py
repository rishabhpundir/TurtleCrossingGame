from turtle import Turtle


STEPS = 50
START = (0, -290)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(START)


    def move(self):
        self.forward(STEPS)


    def is_at_finish_line(self):
        if self.ycor() > 290:
            return True
        else:
            False

    def go_to_start(self):
        if self.is_at_finish_line():
            self.goto(START)



    

