from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("lightblue")  # Set ball color
        self.shape("circle")  # Set ball shape
        self.penup()  # Lift pen to prevent drawing a line
        self.x_move = 10  # Set horizontal movement amount
        self.y_move = 10  # Set vertical movement amount
        self.move_speed = 0.1  # Set initial movement speed

    def move(self):
        # Update ball position
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # Reverse vertical movement when ball hits top or bottom walls
        self.y_move *= -1

    def bounce_x(self):
        # Reverse horizontal movement when ball hits a paddle and increase speed
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        # Move ball to center of screen and reset speed
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()  # Randomize initial direction after reset
