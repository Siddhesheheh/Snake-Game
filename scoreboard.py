from turtle import Turtle

alignment = "center"
font = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("yellow")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=alignment, font=font)

    def game_over(self):
        self.penup()
        self.color("red")
        self.goto(0, 0)
        self.write("Game Over !", align=alignment, font=font)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()