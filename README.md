# Asteroids Game in Python

Welcome to the **Asteroids Game** project! This is a Python-based implementation of the classic Asteroids arcade game. The goal is to control a spaceship, destroy asteroids, and avoid collisions to survive as long as possible.

---

## Table of Contents
1. [Installation](#installation)
2. [How to Play](#how-to-play)
3. [Controls](##controls)
4. [Dependencies](#dependencies)

---

## Installation
To run this game on your local machine, follow these steps:

1. **Ensure Python 3.10+ is installed**:

   Check your Python version by running:
   ```bash
   python3 --version
   ```
   If Python 3.10 or later is not installed, download and install it from python.org.
2. Clone the repository:

   ```bash
   git clone https://github.com/gpavlov951/asteroids.git
   cd asteroids
   ```
3. Set up a virtual environment:

   Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   
   You should see (venv) at the beginning of your terminal prompt, for example:
   ```bash
   (venv) user@machine:~/asteroids$
   ```
4. Install dependencies:
   Install the required libraries using `pip`:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the game:
   Start the game using the following command:
   ```bash
   python3 -m pygame
   ```

---

## How to Play
* Your goal is to destroy all asteroids while avoiding collisions.
* Use the controls (see below) to move, rotate, and shoot.
* Larger asteroids break into smaller ones when shot.
* The game ends when your spaceship is hit by an asteroid.

---

## Controls
* W: Move forward.
* A: Rotate counterclockwise.
* D: Rotate clockwise.
* Spacebar: Shoot projectiles.

---

## Dependencies

This project uses the following Python libraries:
* `pygame`: For handling graphics, sound, and user input.
You can install all dependencies by running:
```bash
pip install -r requirements.txt
```
