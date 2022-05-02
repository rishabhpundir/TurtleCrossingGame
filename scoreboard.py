from turtle import Turtle
FONT = ('Courier', 24, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-290, 260)
        self.write(f"LEVEL : {self.level}", align='Left', font= FONT)

    def score_update(self):
        self.clear()
        self.write(f"LEVEL : {self.level}", align='Left', font= FONT)
    
    def score_up(self):
        self.level += 1
        self.score_update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align='Center', font=FONT)