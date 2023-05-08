from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")  # set the shape of the paddle to a square
        self.color("pink")  # set the color of the paddle to pink

        # set the size of the paddle using the stretch_wid and stretch_len parameters of the shapesize method
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()  # lift the pen up so that the turtle doesn't draw lines as it moves
        self.goto(position)  # set the starting position of the paddle

    def go_up(self):
        # calculate the new y-coordinate of the paddle by adding 20 to its current y-coordinate
        new_y = self.ycor() + 20

        self.goto(self.xcor(), new_y)  # move the paddle to its new position with the goto method

    def go_down(self):
        # calculate the new y-coordinate of the paddle by subtracting 20 from its current y-coordinate
        new_y = self.ycor() - 20

        self.goto(self.xcor(), new_y)  # move the paddle to its new position with the goto method
