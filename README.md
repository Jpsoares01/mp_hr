# Horse Racing Game
A terminal-based game where players bet on virtual horses and watch them race to the finish line.

## Features
- Bet virtual money on one of five randomly generated horses

- Unique horse stats affect race outcomes (stamina, speed, control, strength)

- Simulated race

- Supports multiple players

- Elimination when a player runs out of money

## Requirements
- Python 3.7+

- Runs in a terminal

## How to Run
1. Clone this repository

```bash
git clone https://github.com/Jpsoares01/mp_hr.git
cd mp_hr
```

2. Run the Game

```bash
python main.py
```
⚠️ On macOS/Linux, you may need to use `python3` instead of `python`.

## Project Structure

```text
mp_hr/
├── main.py            # Entry point and main game loop
├── logic/
│   ├── race.py        # Race logic & display
│   ├── betting.py     # Handles player betting
├── models/
│   ├── player.py      # Player class
│   ├── horse.py       # Horse class
├── README.md
```
