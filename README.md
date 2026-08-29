# Games

A small collection of games, built and maintained by RedPandaGuy1234. This repo started as a single Python Battleship implementation and has grown into a home for multiple games — some playable in your terminal, some in your browser.

## Table of Contents
- [Games in This Repo](#games-in-this-repo)
  - [Battleship](#battleship)
  - [The Questions](#the-questions)
  - [Number Guesser](#number-guesser)
  - [Chess](#chess)
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
```
cd mainfile/Battleship
python3 Set_Up_Ships.py
```

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
```
cd mainfile/Questions
open The_Questions.html
```

### Number Guesser
A simple and fun guessing game where you try to guess a randomly selected number within a given range. Perfect for quick entertainment or learning the basics of game logic.

**Features**
- Simple number guessing mechanics
- Feedback on each guess (too high, too low, or correct)
- Adjustable difficulty levels
- Replay functionality

**Run it**
```
cd mainfile/NumberGuesser
python3 number_guesser.py
```

### Chess
A terminal-based chess game built on top of [python-chess](https://github.com/niklasf/python-chess), handling move legality, board state, and game rules.

**Features**
- Full standard chess rules via `python-chess` (legal move generation, check/checkmate detection, castling, en passant, promotion)
- Simple board setup and move-making interface
- Foundation for future features like a playable CLI loop or AI opponent

**Run it**
```
cd mainfile/chess
python3 board.py
```

## Requirements
- **Battleship:** Python 3 or newer, and a terminal
- **The Questions:** Any modern web browser
- **Number Guesser:** Python 3 or newer, and a terminal
- **Chess:** Python 3 or newer, and the `chess` package (see [Installation](#installation))

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/RedPandaGuy1234/Games
   ```
2. Enter the project directory:
   ```
   cd Games
   ```
3. Install dependencies (needed for Chess):
   ```
   pip install -r requirements.txt
   ```
4. Jump into whichever game you want to play — see [Games in This Repo](#games-in-this-repo) above for how to run each one.

## Contributing
Contributions are welcome, whether that's fixes or additions to an existing game or an entirely new game added to the collection. Suggested workflow:
1. Fork the repo
2. Commit changes to your fork
3. Open a pull request

Please include tests where applicable, follow the existing code style for whichever game you're touching, and keep each game's files self-contained within its own folder.

## License
This project is released under the GPL-3.0 License. See [LICENSE](LICENSE) for details. This license applies repo-wide unless a specific game's folder states otherwise.

## Contact
Maintainer: RedPandaGuy1234
GitHub: https://github.com/RedPandaGuy1234
