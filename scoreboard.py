from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Menlo", 24, "normal")

#Scoreboard of the game
class Scoreboard(Turtle):

    #Set the scorboard to the middle of the y axis
    #Made it yellow and used penup to get rid of excess lines

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("yellow")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    #updates the scoreboard
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    #prins "GAME OVER" in the middle of the screen
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    #Increase the scoreboard by 1 everytim the snake gets food
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
