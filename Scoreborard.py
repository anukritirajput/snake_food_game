from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as f:
            self.highscore=int(f.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_sb()

    def update_sb(self):
        self.clear()
        self.write(f"The Score is {self.score}  High Score:{self.highscore}", align="center", font=("Arial", 24, "normal"))
    def inc_score(self):
        self.score+=1

        self.update_sb()
    def reset(self):


        if self.score>self.highscore:
            self.highscore=self.score
            with open("data.txt",'w') as d:
                d.write(f'{self.highscore}')

        self.score=0
        self.update_sb()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('Game Over',align="center", font=("Arial", 24, "normal"))