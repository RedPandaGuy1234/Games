# Battleship

A classic Battleship game implemented in Python.

This repository contains a Python implementation of the Battleship board game. The game can be played locally (in your terminal) and includes AI and/or local multiplayer support.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Gameplay](#gameplay)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- Classic Battleship gameplay (place ships, call shots, sink enemy fleet)
- Single-player mode vs. computer AI
- Two-player local mode
- Clean interface with coordinate input (e.g., A5)

## Requirements
- Python 3 or newer
- A terminal

## Installation
1. Clone the repository
   git clone https://github.com/RedPandaGuy1234/Battleship.git
2. Enter the project directory
   cd Battleship

## Usage

Run the game:
python3 Set_Up_Ships.py

## Gameplay
- Board coordinates use letters for rows and numbers for columns (e.g., A1, B7).
- Ship placement:
  - Place ships manually or let the AI place them automatically.
  - Ship sizes: Carrier (5), Battleship (4), Cruiser (3), Submarine (3), Destroyer (3), and Patrol Boat (2).
- Taking a turn:
  - Enter the coordinate to fire at (e.g., E4).
  - The game reports Hit, Miss, or Sunk and updates the boards.
- Win condition: sink all opponent ships.

## Contributing
Contributions are welcome. Suggested workflow:
1. Fork the repo
2. Commit changes to fork
3. Open a pull request

Please include tests for new features or bug fixes and follow existing code style.

## License
This project is released under the GPL -3.0 License. See LICENSE for details.

## Contact
Maintainer: RedPandaGuy1234
GitHub: https://github.com/RedPandaGuy1234
