from turtle import Turtle

start_pos = [(0, 0), (-20, 0), (-40, 0)]
move_dist = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
        for pos in start_pos:
            self.add_segment(pos)

    def add_segment(self, pos):
        segment = Turtle(shape="square")
        segment.pu()
        segment.color("white")
        segment.goto(pos)
        self.snake_parts.append(segment)

    def extend(self):
        self.add_segment(self.snake_parts[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[seg_num - 1].xcor()
            new_y = self.snake_parts[seg_num - 1].ycor()
            self.snake_parts[seg_num].goto(new_x, new_y)
        self.snake_parts[0].forward(move_dist)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
