# Space Invaders 🚀👾

The classic arcade game where you shoot down alien ships.

1. **Launch** the game window with Turtle.
2. **Control** your player ship (3 lives) with arrow keys.
3. **Shoot** yellow bullets to destroy rows of red, orange, and yellow enemies.
4. **Hide** behind destructible green barriers.
5. **Dodge** enemy fire and prevent aliens from reaching the bottom.
6. **Beat** each wave to level up—enemies speed up over time.
7. **Catch** the occasional UFO bonus for 100 points.
8. **See** your score, level, and lives displayed on-screen.
9. **Enjoy** retro sound effects (shoot, explosion, level-up, UFO).

---

## 🛠️ Features

* **Classic Gameplay**
  Implements the core mechanics of Space Invaders: fleet movement, barrier destruction, and level progression.

* **Multiple Enemy Types**

  * **Yellow Aliens** (top row): 30 points
  * **Orange Aliens** (middle row): 20 points
  * **Red Aliens** (bottom row): 10 points

* **UFO Bonus Enemy**
  Randomly spawns across the top for an extra **100 points**.

* **Protective Barriers**
  Four green barriers you can duck behind—and destroy with bullets.

* **Lives & Scoring System**
  Start with 3 lives; lose one on an enemy bullet hit or collision.

* **Level Progression**
  Each cleared wave increases enemy speed and descent rate.

* **Sound Effects**
  Built-in beeps for shooting, explosions, UFO, level-ups, and game-over.

* **Start & Game-Over Screens**
  Friendly prompts to start a new game or retry after defeat.

---

## 📂 Repository Structure

```
.
├── main.py           # Entry point that instantiates and runs Game
├── game.py           # Game logic and main loop
├── player.py         # Player class (movement, rendering)
├── enemy.py          # Enemy class (behavior, animation)
├── bullet.py         # Bullet class (player & enemy projectiles)
```

---

## 🚀 Usage

1. **Run the game**

   ```bash
   python main.py
   ```

2. **Controls**

   * **Left Arrow**: Move left
   * **Right Arrow**: Move right
   * **Space**: Fire bullet / Start game
   * **Q**: Quit game

3. **Objective**
   Destroy all enemies to advance levels, avoid enemy fire, and protect your barriers. Rack up points and aim for a high score!

---

## ⚙️ Configuration

You can tweak gameplay parameters in `game.py`:

```python
# in Game class
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
NUM_ENEMIES_ROW = 5
NUM_ENEMIES_COL = 4
ENEMY_SPACING_X = 60
ENEMY_SPACING_Y = 50
ENEMY_START_Y = 250
enemy_speed = 2           # initial speed of enemies
enemy_move_time = 0.02    # time between moves
BARRIER_Y = -200
NUM_BARRIERS = 4
UFO_SPAWN_CHANCE = 0.002  # probability per frame
```

Adjust these values to change difficulty, formation layout, and overall pacing.

---

## 📝 Notes

* This game uses **Turtle** for graphics—performance may vary by system.
* Sound effects utilize **winsound.Beep** on Windows. Other platforms will run silently.
* You can replace shapes or add images by registering custom Turtle shapes in `register_shapes()`.
* Contributions and bug reports are welcome—feel free to open an issue or pull request!

---