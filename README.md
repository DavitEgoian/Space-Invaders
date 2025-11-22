# Space Invaders 🚀👾

A recreation of the classic arcade game where you defend Earth from waves of descending alien ships, built using Python and the Turtle graphics library.

## 🎮 Gameplay Overview

Take command of your ship and stop the alien invasion!

1. **Defend:** Destroy rows of aliens (Yellow, Orange, and Red) before they reach the bottom.
2. **Survive:** Dodge enemy fire and hide behind destructible green barriers.
3. **Score:** Earn points for every hit. Catch the random UFO for a massive bonus.
4. **Progress:** Clear waves to advance levels. Enemies become faster with every new level.

## ✨ Features

* **Classic Mechanics**: Authentic fleet movement, destructible covers, and increasing difficulty.
* **Enemy Variety**:
  * **Yellow Aliens** (Top): 30 points
  * **Orange Aliens** (Middle): 20 points
  * **Red Aliens** (Bottom): 10 points
  * **UFO**: Random spawn for **100 bonus points**.
* **Leveling System**: Infinite progression where enemies gain speed after every cleared wave.
* **Retro Audio**: Sound effects for shooting, explosions, and game events (Windows only).

## 💻 Prerequisites

* Python 3.x
* Standard libraries (included with Python): `turtle`, `math`, `random`, `time`

### ⚠️ Platform Compatibility
**Audio**: This game uses the `winsound` module for sound effects, which is standard on **Windows**.
* On **macOS/Linux**, the game will run perfectly, but without sound effects.

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/DavitEgoian/Space-Invaders.git
   cd Space-Invaders
   ```

2. **Run the game:**
   ```bash
   python main.py
   ```

## 🕹️ Controls

| Key | Action |
| :--- | :--- |
| **← Left Arrow** | Move Ship Left |
| **→ Right Arrow** | Move Ship Right |
| **Spacebar** | Fire Bullet / Start Game |
| **Q** | Quit Game |

## 📂 Project Structure

* `main.py`: Entry point; initializes the game window.
* `game.py`: Core logic, game loop, and state management.
* `player.py`: Player ship movement and rendering.
* `enemy.py`: Alien behavior, movement patterns, and types.
* `bullet.py`: Projectile logic for both player and enemies.

## ⚙️ Customization

You can tweak the game difficulty and layout by modifying the constants in `game.py`:

```python
SCREEN_WIDTH = 600      # Window width
NUM_ENEMIES_ROW = 5     # Aliens per row
enemy_speed = 2         # Base movement speed
UFO_SPAWN_CHANCE = 0.002 # Frequency of bonus ship
```

---
*Built with Python Turtle. Contributions are welcome!*
