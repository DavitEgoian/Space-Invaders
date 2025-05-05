import random
import turtle
import math
import time
import os
import winsound
from player import Player
from bullet import Bullet
from enemy import Enemy

class Game:
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 700
    NUM_ENEMIES_ROW = 5
    NUM_ENEMIES_COL = 4
    ENEMY_SPACING_X = 60
    ENEMY_SPACING_Y = 50
    ENEMY_START_Y = 250
    BARRIER_Y = -200
    NUM_BARRIERS = 4
    BARRIER_WIDTH = 60
    BARRIER_HEIGHT = 40

    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title('Space Invaders')
        self.screen.bgcolor('black')
        self.screen.setup(width=self.SCREEN_WIDTH, height=self.SCREEN_HEIGHT)
        self.screen.tracer(0)

        self.register_shapes()

        boundary_x = self.SCREEN_WIDTH//2 - 20

        self.score = 0
        self.level = 1
        self.lives = 3
        self.game_state = "start"
        self.enemy_speed = 2
        self.enemy_move_time = 0.02

        self.score_display = turtle.Turtle()
        self.score_display.hideturtle()
        self.score_display.color("white")
        self.score_display.penup()
        self.score_display.goto(-self.SCREEN_WIDTH/2 + 10, self.SCREEN_HEIGHT/2 - 30)

        self.lives_display = turtle.Turtle()
        self.lives_display.hideturtle()
        self.lives_display.color("white")
        self.lives_display.penup()
        self.lives_display.goto(self.SCREEN_WIDTH/2 - 100, self.SCREEN_HEIGHT/2 - 30)

        self.level_display = turtle.Turtle()
        self.level_display.hideturtle()
        self.level_display.color("white")
        self.level_display.penup()
        self.level_display.goto(0, self.SCREEN_HEIGHT/2 - 30)

        self.message_display = turtle.Turtle()
        self.message_display.hideturtle()
        self.message_display.color("white")
        self.message_display.penup()
        self.message_display.goto(0, 0)

        self.player = Player(0, -self.SCREEN_HEIGHT/2 + 50, 20, boundary_x)
        self.bullet = Bullet(40, self.SCREEN_HEIGHT/2)
        self.enemy_bullets = []
        self.enemies = []
        self.barriers = []
        self.ufo = None
        self.ufo_timer = 0

        self.create_barriers()

        self.create_enemies()

        self.screen.listen()
        self.screen.onkeypress(self.player.move_left, 'Left')
        self.screen.onkeypress(self.player.move_right, 'Right')
        self.screen.onkeypress(lambda: self.fire_bullet() if self.game_state == "playing" else self.start_game(), 'space')
        self.screen.onkeypress(self.quit_game, 'q')

        self.hide_all_game_elements()

        self.show_start_screen()

    def register_shapes(self):
        pass

    def hide_all_game_elements(self):
        self.player.hide()
        self.bullet.sprite.hideturtle()

        for bullet in self.enemy_bullets:
            bullet.sprite.hideturtle()

        for enemy in self.enemies:
            enemy.sprite.hideturtle()

        for barrier in self.barriers:
            barrier.hideturtle()

        if self.ufo:
            self.ufo.hideturtle()

        self.score_display.clear()
        self.lives_display.clear()
        self.level_display.clear()

    def show_all_game_elements(self):
        self.player.show()

        for enemy in self.enemies:
            enemy.sprite.showturtle()

        for barrier in self.barriers:
            barrier.showturtle()

        self.update_displays()

    def play_sound(self, sound_type):
        try:
            if sound_type == "shoot":
                winsound.Beep(1000, 50)
            elif sound_type == "explosion":
                winsound.Beep(200, 100)
            elif sound_type == "ufo":
                winsound.Beep(1500, 100)
            elif sound_type == "game_over":
                winsound.Beep(300, 500)
            elif sound_type == "level_up":
                winsound.Beep(800, 100)
                time.sleep(0.1)
                winsound.Beep(1000, 100)
                time.sleep(0.1)
                winsound.Beep(1200, 100)
        except:
            pass

    def create_barriers(self):
        barrier_spacing = self.SCREEN_WIDTH / (self.NUM_BARRIERS + 1)
        for i in range(self.NUM_BARRIERS):
            x_pos = -self.SCREEN_WIDTH/2 + barrier_spacing * (i + 1)

            for row in range(4):
                for col in range(6):
                    segment = turtle.Turtle()
                    segment.shape("square")
                    segment.color("green")
                    segment.shapesize(0.5, 0.5)
                    segment.penup()
                    segment.goto(x_pos - 15 + col * 5, self.BARRIER_Y + row * 5)
                    self.barriers.append(segment)

    def create_enemies(self):
        start_x = -((self.NUM_ENEMIES_ROW - 1) * self.ENEMY_SPACING_X) / 2

        for row in range(self.NUM_ENEMIES_COL):
            for col in range(self.NUM_ENEMIES_ROW):
                x = start_x + col * self.ENEMY_SPACING_X
                y = self.ENEMY_START_Y - row * self.ENEMY_SPACING_Y

                enemy_type = row % 3
                enemy = Enemy(self.SCREEN_WIDTH//2 - 20, (100, self.SCREEN_HEIGHT//2 - 100),
                             self.enemy_speed, 20, enemy_type)
                enemy.sprite.goto(x, y)
                self.enemies.append(enemy)

    def create_enemy_bullet(self):
        if len(self.enemies) > 0 and random.random() < 0.05:
            shooting_enemy = random.choice(self.enemies)
            bullet = Bullet(-20, -self.SCREEN_HEIGHT/2, "enemy")
            bullet.fire(shooting_enemy.sprite.xcor(), shooting_enemy.sprite.ycor())
            self.enemy_bullets.append(bullet)

    def create_ufo(self):
        if self.ufo is None and random.random() < 0.002:
            self.ufo = turtle.Turtle()
            self.ufo.shape("circle")
            self.ufo.color("purple")
            self.ufo.shapesize(1.5, 1.5)
            self.ufo.penup()

            start_side = random.choice([-1, 1])
            self.ufo.goto(start_side * (self.SCREEN_WIDTH/2 + 20), self.SCREEN_HEIGHT/2 - 80)
            self.ufo.dx = -start_side * 3

            self.play_sound("ufo")

    def move_ufo(self):
        if self.ufo:
            self.ufo.setx(self.ufo.xcor() + self.ufo.dx)

            if (self.ufo.dx > 0 and self.ufo.xcor() > self.SCREEN_WIDTH/2 + 20) or                (self.ufo.dx < 0 and self.ufo.xcor() < -self.SCREEN_WIDTH/2 - 20):
                self.ufo.hideturtle()
                self.ufo = None

    def fire_bullet(self):
        if self.bullet.state == 'ready':
            self.bullet.fire(self.player.sprite.xcor(), self.player.sprite.ycor())
            self.play_sound("shoot")

    def update_displays(self):
        self.score_display.clear()
        self.score_display.write(f"Score: {self.score}", font=("Arial", 14, "normal"))

        self.lives_display.clear()
        self.lives_display.write(f"Lives: {self.lives}", font=("Arial", 14, "normal"))

        self.level_display.clear()
        self.level_display.write(f"Level: {self.level}", font=("Arial", 14, "normal"))

    def show_start_screen(self):
        self.hide_all_game_elements()

        self.message_display.clear()
        self.message_display.write("SPACE INVADERS\n\nPress SPACE to start\nPress Q to quit",
                                  align="center", font=("Arial", 24, "normal"))

    def show_game_over_screen(self):
        self.hide_all_game_elements()

        self.message_display.clear()
        self.message_display.write(f"GAME OVER\n\nFinal Score: {self.score}\n\nPress SPACE to play again\nPress Q to quit",
                                  align="center", font=("Arial", 24, "normal"))

    def show_level_complete_screen(self):
        self.hide_all_game_elements()

        self.message_display.clear()
        self.message_display.write(f"LEVEL {self.level} COMPLETE!\n\nPress SPACE to continue",
                                  align="center", font=("Arial", 24, "normal"))

    def start_game(self):
        if self.game_state == "start" or self.game_state == "game_over" or self.game_state == "level_complete":
            if self.game_state == "start" or self.game_state == "game_over":
                self.score = 0
                self.lives = 3
                self.level = 1
                self.enemy_speed = 2
                self.enemy_move_time = 0.02

            for enemy in self.enemies:
                enemy.sprite.hideturtle()
            self.enemies.clear()

            for barrier in self.barriers:
                barrier.hideturtle()
            self.barriers.clear()

            for bullet in self.enemy_bullets:
                bullet.sprite.hideturtle()
            self.enemy_bullets.clear()

            if self.ufo:
                self.ufo.hideturtle()
                self.ufo = None

            self.player.reset_position(0, -self.SCREEN_HEIGHT/2 + 50)

            self.create_barriers()
            self.create_enemies()

            self.message_display.clear()

            self.show_all_game_elements()

            self.play_sound("level_up")

            self.game_state = "playing"

    def next_level(self):
        self.level += 1
        self.enemy_speed += 0.5
        self.enemy_move_time = max(0.005, self.enemy_move_time - 0.002)

        for enemy in self.enemies:
            enemy.sprite.hideturtle()
        self.enemies.clear()

        self.create_enemies()

        self.update_displays()

        self.game_state = "level_complete"
        self.show_level_complete_screen()

    def quit_game(self):
        turtle.bye()

    @staticmethod
    def collision(a, b, distance: int) -> bool:
        return math.hypot(a.xcor() - b.xcor(), a.ycor() - b.ycor()) < distance

    def run(self):
        last_time = time.time()
        while True:
            current_time = time.time()
            delta_time = current_time - last_time
            last_time = current_time

            self.screen.update()

            if self.game_state == "playing":
                self.bullet.move()

                self.create_enemy_bullet()
                for bullet in self.enemy_bullets[:]:
                    bullet.move()

                    if self.collision(bullet.sprite, self.player.sprite, 20):
                        bullet.reset()
                        self.enemy_bullets.remove(bullet)
                        self.lives -= 1
                        self.update_displays()
                        self.play_sound("explosion")

                        self.player.hide()
                        self.screen.update()
                        time.sleep(0.1)
                        self.player.show()

                        if self.lives <= 0:
                            self.game_state = "game_over"
                            self.show_game_over_screen()
                            self.play_sound("game_over")
                            break

                    for barrier in self.barriers[:]:
                        if self.collision(bullet.sprite, barrier, 10):
                            bullet.reset()
                            if bullet in self.enemy_bullets:
                                self.enemy_bullets.remove(bullet)
                            barrier.hideturtle()
                            self.barriers.remove(barrier)
                            break

                enemies_to_move_down = False
                for enemy in self.enemies[:]:
                    enemy.move()

                    if enemy.sprite.xcor() > self.SCREEN_WIDTH/2 - 20 or enemy.sprite.xcor() < -self.SCREEN_WIDTH/2 + 20:
                        enemies_to_move_down = True

                    if self.collision(enemy.sprite, self.player.sprite, 30):
                        self.game_state = "game_over"
                        self.show_game_over_screen()
                        break

                    if self.bullet.state == 'fire' and self.collision(self.bullet.sprite, enemy.sprite, 20):
                        self.bullet.reset()
                        enemy.sprite.hideturtle()
                        self.enemies.remove(enemy)
                        self.play_sound("explosion")

                        self.score += (3 - enemy.enemy_type) * 10
                        self.update_displays()

                    for barrier in self.barriers[:]:
                        if self.collision(enemy.sprite, barrier, 15):
                            barrier.hideturtle()
                            self.barriers.remove(barrier)

                if enemies_to_move_down:
                    for enemy in self.enemies:
                        enemy.shift_down()

                        if enemy.sprite.ycor() < -self.SCREEN_HEIGHT/2 + 100:
                            self.game_state = "game_over"
                            self.show_game_over_screen()
                            break

                self.create_ufo()
                self.move_ufo()

                if self.ufo and self.bullet.state == 'fire' and self.collision(self.bullet.sprite, self.ufo, 25):
                    self.bullet.reset()
                    self.ufo.hideturtle()
                    self.ufo = None
                    self.score += 100
                    self.update_displays()
                    self.play_sound("ufo")

                if len(self.enemies) == 0:
                    self.play_sound("level_up")
                    self.next_level()

            elif self.game_state == "level_complete":
                pass

            time.sleep(0.02)