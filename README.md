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
A terminal-based chess game built from [python-chess](https://github.com/niklasf/python-chess) (A huge thanks to them), handling move legality, board state, and game rules. Includes an optional computer opponent, either a lightweight built-in bot or Stockfish, the open-source chess engine.

**Features**
- Full standard chess rules via `python-chess` (legal move generation, check/checkmate detection, castling, en passant, promotion)
- Simple board setup and move-making interface
- Play moves by typing the original square that the piece was on, and the square it is going to (E.g. e2e4). Castling is entered the same way — move your king two squares toward the rook (e.g. e1g1 for White kingside).
- Resign at any time by typing `resign`, or offer a draw by typing `draw`
- Optional bot opponent with three difficulty levels:
  - **Easy** — a lightweight built-in minimax bot (~600 elo), no Stockfish required
  - **Normal** — Stockfish, capped to roughly 1400 Elo
  - **Hard** — Stockfish, capped to roughly 2000 Elo
- Choose to play against the bot, pick its color (White, Black, or Random), and pick a difficulty level.

**Easy mode requires no extra setup** — it's a small built-in minimax bot with no external dependencies. **Normal and Hard modes require Stockfish to be installed separately** (it's a compiled chess engine, not a Python package — `pip install -r requirements.txt` won't get it for you). See [Installing Stockfish](#installing-stockfish) below. If Stockfish isn't found for Normal or Hard mode, the game falls back to human vs. human instead of crashing.

**Run it**

    cd mainfile/Chess
    python3 board.py

When you start the game, you'll be asked whether you want to play against the bot, which color it should play (or Random), and which difficulty level (Easy, Normal, or Hard).

#### Installing Stockfish

**macOS**

    brew install stockfish

**Windows**

    winget install Stockfish.Stockfish

Or download the executable from [stockfishchess.org/download](https://stockfishchess.org/download/) and either add it to your PATH or point `STOCKFISH_PATH` in `mainfile/Chess/board.py` at the full path to the `.exe`.

**Linux (Debian/Ubuntu)**

    sudo apt install stockfish

**Linux (Fedora)**

    sudo dnf install stockfish

**Linux (Arch)**

    sudo pacman -S stockfish

**Any OS, manual install**

Download a prebuilt binary from [stockfishchess.org/download](https://stockfishchess.org/download/), unzip it, and either add it to your PATH or set `STOCKFISH_PATH` in `mainfile/Chess/board.py` to the full path of the binary.

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
- **Chess:** Python 3 or newer, and the `chess` package (see [Installation](#installation)). The [Stockfish](https://stockfishchess.org/download/) engine is only needed for Normal/Hard bot difficulty (see [Installing Stockfish](#installing-stockfish)); Easy mode needs nothing extra.
- **Reaction Test:** Python 3 or newer, and a terminal

## Installation
1. Clone the repository:

       git clone https://github.com/RedPandaGuy1234/Games

2. Enter the project directory:

       cd Games

3. Install dependencies (needed for Chess):

       pip install -r requirements.txt

4. If you want to play Chess against the bot on Normal or Hard difficulty, also install the Stockfish engine — see [Installing Stockfish](#installing-stockfish). Easy mode works without it.

5. Regularly update it:

       git pull

6. Jump into whichever game you want to play — see [Games in This Repo](#games-in-this-repo) above for how to run each one.

## License
This project is released under the GPL-3.0 License. See [LICENSE](LICENSE) for details. This license applies repo-wide unless a specific game's folder states otherwise.

## Credits
This project is dependent on the python-chess library [python-chess](https://github.com/niklasf/python-chess), the [Stockfish](https://github.com/official-stockfish/Stockfish) chess engine, and black for formatting: [black](https://github.com/psf/black).

## Contact
Maintainer: RedPandaGuy1234
GitHub: https://github.com/RedPandaGuy1234
