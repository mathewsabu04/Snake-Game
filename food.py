from turtle import Turtle
import random

#Made a class named Food

class Food(Turtle):

    #Attributes of the Food
    #Its a circle and its red
    #Set the length and width to 0.5
    #refreshes everytime its eaten
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    #This is the food refreshes
    #It refreshes randomly in the screen.
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
