from turtle import Turtle, forward
import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

turtle.register_shape('pica.gif')
class Player(Turtle):
    
    def __init__(self):
        super().__init__()

        self.shape("pica.gif")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else: 
            return False