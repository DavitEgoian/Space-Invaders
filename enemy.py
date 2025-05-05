import turtle
import random

class Enemy:
    SHAPES = ['triangle', 'circle', 'square']
    COLORS = ['red', 'orange', 'yellow']
    POINTS = [30, 20, 10]

    def __init__(self, boundary_x: int, boundary_y: tuple[int, int], speed: int, descent: int, enemy_type: int = 0):
        self.sprite = turtle.Turtle()
        self.enemy_type = enemy_type % 3
        self.sprite.color(self.COLORS[self.enemy_type])
        self.sprite.shape(self.SHAPES[self.enemy_type])
        self.sprite.penup()

        self.speed = speed
        self.descent = descent
        self.animation_frame = 0
        self.animation_delay = 10

        x = random.randint(-boundary_x + 50, boundary_x - 50)
        y = random.randint(boundary_y[0], boundary_y[1])
        self.sprite.goto(x, y)

    def move(self):
        self.sprite.setx(self.sprite.xcor() + self.speed)
        self.animation_frame += 1
        if self.animation_frame >= self.animation_delay:
            self.animation_frame = 0
            current_heading = self.sprite.heading()
            self.sprite.setheading((current_heading + 10) % 360)

    def shift_down(self):
        self.sprite.sety(self.sprite.ycor() - self.descent)
        self.speed *= -1
