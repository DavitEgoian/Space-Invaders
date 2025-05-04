import turtle

class Player:
    def __init__(self, start_x: int, start_y: int, move_speed: int, boundary_x: int):
        self.sprite = turtle.Turtle()
        self.sprite.color('lime')
        self.sprite.shape('triangle')
        self.sprite.shapesize(1.5, 1.5)
        self.sprite.penup()
        self.sprite.setheading(90)
        self.sprite.goto(start_x, start_y)
        self.move_speed = move_speed
        self.boundary_x = boundary_x
        self.lives = 3

        self.base = turtle.Turtle()
        self.base.color('green')
        self.base.shape('square')
        self.base.shapesize(0.3, 1.5)
        self.base.penup()
        self.base.goto(start_x, start_y - 10)

    def move_left(self):
        x = max(self.sprite.xcor() - self.move_speed, -self.boundary_x)
        self.sprite.setx(x)
        self.base.setx(x)

    def move_right(self):
        x = min(self.sprite.xcor() + self.move_speed, self.boundary_x)
        self.sprite.setx(x)
        self.base.setx(x)

    def reset_position(self, x: int, y: int):
        self.sprite.goto(x, y)
        self.base.goto(x, y - 10)

    def hide(self):
        self.sprite.hideturtle()
        self.base.hideturtle()

    def show(self):
        self.sprite.showturtle()
        self.base.showturtle()
