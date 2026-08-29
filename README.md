# Games

A small collection of games, built by me. This repo started as a single Python Battleship implementation and has grown into a home for multiple games — some playable in your terminal, some in your browser.

## Table of Contents
- [Games in This Repo](#games-in-this-repo)
  - [Battleship](#battleship)
  - [The Questions](#the-questions)
  - [Number Guesser](#number-guesser)
  - [Chess](#chess)
  - [Reaction Test](#reaction-test)
- [Requirements](#requirements)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Games in This Repo

### Battleship
A classic Battleship implementation playable in your terminal, with a bot and local multiplayer support.

**Features**
- Classic Battleship gameplay (place ships, call shots, sink the enemy fleet)
- Single-player mode vs. computer AI
- Two-player local mode
- Coordinate-based input (e.g., A5) with input validation

**Run it**

    cd mainfile/Battleship
    python3 Set_Up_Ships.py

**Gameplay basics**
- Board coordinates use letters for rows and numbers for columns (e.g., A1, B7).
- Ship sizes: Carrier (5), Battleship (4), Cruiser (3), Submarine (3), Destroyer (3), and Patrol Boat (2).
- Enter a coordinate to fire at (e.g., E4); the game reports Hit, Miss, or Sunk.
- Win by sinking every ship in the opposing fleet.

### The Questions
A browser-based trivia game for 1–5 players (or solo against a computer opponent), inspired by classic wedge-collecting trivia board games. Runs entirely in a single HTML file — no install required.

**Features**
- A 36-space board with six trivia categories: Geography, History, Science, Entertainment, Sports, and Arts & Words
- Roll a die, choose a direction, and answer whatever category you land on
- Open-answer, multiple-choice, and true/false question formats
- A "deciding question" mechanic — once you've collected all six wedges, the other players choose your final category
- 1–5 player support, including a solo mode against a computer opponent
- Optional Hard Mode: missing a question in a category you've already won costs you that wedge

**Play it**

    cd mainfile/Questions
    open The_Questions.html

### Number Guesser
A simple and fun guessing game where you try to guess a randomly selected number within a given range. Perfect for quick entertainment or learning the basics of game logic.

**Features**
- Simple number guessing mechanics
- Feedback on each guess (too high, too low, or correct)
- Adjustable difficulty levels
- Replay functionality

**Run it**

    cd mainfile/NumberGuesser
    python3 number_guesser.py

### Chess
A terminal-based chess game built from [python-chess](https://github.com/niklasf/python-chess) (A huge thanks to them), handling move legality, board state, and game rules.

**Features**
- Full standard chess rules via `python-chess` (legal move generation, check/checkmate detection, castling, en passant, promotion)
- Simple board setup and move-making interface
- Play moves by typing the original square that the piece was on, and the square it is going to (E.g. e2e4).

**Run it**

    cd mainfile/chess
    python3 board.py

### Reaction Test
A quick terminal game that measures how fast your reflexes are. It waits a random amount of time between 1 and 60 seconds, tells you to go, then reports how long it took you to press Enter.

**Features**
- Random wait time before the "NOW!" prompt appears
- Measures and reports your reaction time in seconds
- Simple, single-run terminal gameplay

**Run it**

    cd mainfile/Reactiontest
    python3 Reaction_test

## Requirements
- **Battleship:** Python 3 or newer, and a terminal
- **The Questions:** Any modern web browser
- **Number Guesser:** Python 3 or newer, and a terminal
- **Chess:** Python 3 or newer, and the `chess` package (see [Installation](#installation))
- **Reaction Test:** Python 3 or newer, and a terminal

## Installation
1. Clone the repository:

       git clone https://github.com/RedPandaGuy1234/Games

2. Enter the project directory:

       cd Games

3. Install dependencies (needed for Chess):

       pip install -r requirements.txt

4. Regularly update it:

       git pull

5. Jump into whichever game you want to play — see [Games in This Repo](#games-in-this-repo) above for how to run each one.

## License
This project is released under the GPL-3.0 License. See [LICENSE](LICENSE) for details. This license applies repo-wide unless a specific game's folder states otherwise.

## Credits
This project is dependent on the python-chess library [python-chess](https://github.com/niklasf/python-chess) and black for formatting: [black](https://github.com/psf/black).

## Contact
Maintainer: RedPandaGuy1234
GitHub: https://github.com/RedPandaGuy1234
