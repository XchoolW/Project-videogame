# Space-Ghosts

### Project Overview

Space-Ghosts is a classic arcade-style video game where the player battles alien-ghosts. The game features progressively faster and more difficult levels, with an in-game score tracker and a high score leaderboard. This project was developed collaboratively to demonstrate core programming principles.

### Key Features

- **Dynamic Difficulty:** The game increases in speed and complexity with each level passed.
- **Score Management:** Tracks player scores and saves the top 5 records to a leaderboard, with all records stored in a `score.txt` file.
- **Space-Invaders Style Gameplay:** Simple and intuitive mechanics focused on shooting enemies.

### Technologies

- **Python:** The primary programming language used for the game logic.
- **Pygame:** A cross-platform set of Python modules designed for writing video games.

### Core Computer Science Concepts

This project was designed to showcase the implementation of fundamental software engineering principles:

- **Object-Oriented Programming (OOP):** The game's entities (player, enemies, bullets) are structured as classes, demonstrating the use of inheritance and encapsulation for a modular design.
- **File I/O:** Implemented functionality to read and write high scores from a text file, ensuring data persistence.
- **Game Loop:** Utilized a game loop to manage continuous user input, state updates, and rendering.

### Getting Started

#### Prerequisites

- Python 3.12.3

#### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/XchoolW/Project-videogame.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Project-videogame
    ```

3. Create and activate a virtual environment (recommended):

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

4. Install the required libraries from the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt

    ```

#### Running the Game

Navigate to the `src` folder and execute the main script:

```bash
cd src
python3 main.py
