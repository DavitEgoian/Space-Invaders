import turtle
import time

class Bullet:
    def __init__(self, speed: int, boundary_y: int, bullet_type: str = "player"):
        self.sprite = turtle.Turtle()
        if bullet_type == "player":
            self.sprite.color('yellow')
            self.sprite.shape('square')
            self.sprite.shapesize(0.2, 0.6)
        else:
            self.sprite.color('red')
            self.sprite.shape('square')
            self.sprite.shapesize(0.2, 0.6)
        self.sprite.penup()
        self.sprite.hideturtle()
        self.speed = speed
        self.boundary_y = boundary_y
        self.state = 'ready'
        self.bullet_type = bullet_type

    def fire(self, x: int, y: int):
        if self.state == 'ready':
            self.state = 'fire'
            if self.bullet_type == "player":
                self.sprite.goto(x, y + 10)
                self.sprite.setheading(90)
            else:
                self.sprite.goto(x, y - 10)
                self.sprite.setheading(270)
            self.sprite.showturtle()

    def move(self):
        if self.state == 'fire':
            new_y = self.sprite.ycor() + self.speed
            self.sprite.sety(new_y)
            if (self.speed > 0 and new_y > self.boundary_y) or (self.speed < 0 and new_y < self.boundary_y):
                self.reset()

    def reset(self):
        self.sprite.hideturtle()
        self.state = 'ready'
