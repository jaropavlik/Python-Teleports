# Python-Teleports
Terminal-based board game in Python featuring configurable grid size, snake-like movement and randomized teleportation logic.

# 🎮 Game Overview

This project is a modern take on the classic "Snakes and Ladders" mechanics. Players start at the top-left corner and must reach the final goal tile. The board is navigated in a "snake-like" pattern, meaning the direction of movement alternates between left-to-right and right-to-left for each row.

# 🚀 Key Features
- Dynamic Grid System: Configurable board sizes ranging from 5x5 to 10x10.

  <img width="698" height="307" alt="eudq" src="https://github.com/user-attachments/assets/6c4cc9cd-f193-4e59-aead-0f1ced9055d1" />

- Intelligent Teleports:
    Positive (A, B, C...): Boost players forward to a higher tile.
    Negative (a, b, c...): Send players back to a previous tile.
    All teleports randomly generated to ensure a fair game.

  <img width="757" height="575" alt="Ly5h" src="https://github.com/user-attachments/assets/fffeb721-836e-4801-af64-06f1abac9012" />

- Exact Roll Mechanic
    To win, a player must land exactly on the final tile (*).
    Over-rolling keeps the player in their current position.
- Optimized Logic: Built using 1D-to-2D coordinate mapping for high performance and clean code.
<img width="665" height="394" alt="vnmd" src="https://github.com/user-attachments/assets/4ffc60a6-50b3-4e87-8761-0b9c0822fd33" />

# 🛠️ Technical Details
- Language: Python 3.x
- Architecture: The game logic separates the State (1D position of players) from the Visualization (2D console grid rendering), making the code easy to maintain and extend.

# 📋 How to play
  1. Run the script: python teleports.py
  2. Enter the desired board size.
  3. Enter the number of players.
  4. Players take turns automatically.
  5. Each round is printed into the terminal until a player wins.



All teleports are randomly generated with logical constraints to ensure a fair yet challenging game.

