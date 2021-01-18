from turtle import Turtle

FONT = "Courier"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        style = (FONT, 12, 'italic')
        self.write(f'Score: {self.score}', font=style, align='center')

    def game_over(self):
        self.goto(0, 30)
        self.write("GAME OVER", font=FONT, align='center')

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
