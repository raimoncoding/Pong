from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("lightgreen")
        self.penup()
        self.hideturtle()
        self.l_score = 0  # initialize left score to 0
        self.r_score = 0  # initialize right score to 0
        self.update_scoreboard()  # call update_scoreboard method to display initial scores

    def update_scoreboard(self):
        self.clear()  # clear previous scores
        self.goto(-100, 200)  # go to left score position
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))  # write left score
        self.goto(100, 200)  # go to right score position
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))  # write right score

    def l_point(self):
        self.l_score += 1  # increment left score by 1
        self.update_scoreboard()  # call update_scoreboard method to display updated scores

    def r_point(self):
        self.r_score += 1  # increment right score by 1
        self.update_scoreboard()  # call update_scoreboard method to display updated scores
