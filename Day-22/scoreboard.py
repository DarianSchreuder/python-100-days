from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"Score: {self.l_score}", align="center", font=("Arial", 24, "normal"))
        self.goto(100, 200)
        self.write(f"Score: {self.r_score}", align="center", font=("Arial", 24, "normal"))

    def l_score_inc(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_score_inc(self):
        self.r_score += 1
        self.update_scoreboard()
