# Console-Tic-Tac-Toe

# Tic-Tac-Toe (Terminal)

A two-player Tic-Tac-Toe game for the terminal, written in plain Python with no external libraries. Players take turns entering a row and a column, and the board redraws in color after every move.

```
  ╔═══════════════════════════╗
  ║      TIC  ·  TAC  ·  TOE  ║
  ╚═══════════════════════════╝
   Player 1 = O    Player 2 = X

      1   2   3
    ┏━━━┳━━━┳━━━┓
  1 ┃ O ┃ X ┃ X ┃
    ┣━━━╋━━━╋━━━┫
  2 ┃ · ┃ O ┃ · ┃
    ┣━━━╋━━━╋━━━┫
  3 ┃ · ┃ · ┃ O ┃
    ┗━━━┻━━━┻━━━┛

  🏆 Player O wins!
```

## Features

- Two players on one keyboard, taking alternate turns
- Colored board: O in cyan, X in red, empty cells shown as a dim `·`
- Screen clears after every move so only the current board is visible
- Input validation: rows and columns must be 1, 2 or 3
- Occupied cells are rejected, and the player is asked to choose again
- Detects wins (rows, columns, both diagonals) and draws

## Requirements

- Python 3.6 or newer
- A terminal that supports ANSI colors and Unicode box-drawing characters (most modern terminals do, including Windows Terminal, macOS Terminal, iTerm2, and Linux terminals)

Some IDE output panes do not render colors or the screen clear and will show raw escape codes instead. If that happens, run the game from a regular terminal.

## How to run

```bash
python3 tictactoe.py
```

On Windows you may need `python tictactoe.py` or `py tictactoe.py`.

## How to play

1. Player 1 (O) goes first, then Player 2 (X), alternating.
2. On your turn, type a **row** number (1-3), press Enter, then type a **column** number (1-3) and press Enter.
3. The first player to get three in a row, horizontally, vertically or diagonally, wins.
4. If all 9 cells are filled and nobody has won, the game is a draw.

Rows count from the top and columns from the left:

```
      col 1  col 2  col 3
row 1   (1,1)  (1,2)  (1,3)
row 2   (2,1)  (2,2)  (2,3)
row 3   (3,1)  (3,2)  (3,3)
```

## How it works

The board is stored as a single 9-character string, where `.` means an empty cell:

```python
board = "........."
```

A (row, column) pair is converted to a string index with:

```python
index = (row - 1) * 3 + (col - 1)
```

When a move is valid, the string is rebuilt using slicing:

```python
board = board[:index] + symbol + board[index + 1:]
```

Other details:

- `turnCount` tracks the turn number. Its parity decides whose turn it is and which symbol is placed.
- Win checks only start from turn 5, since that is the earliest a player can have three marks.
- If turn 9 is reached with no winner, the game is a draw.
- The board string always holds `.`, `X` and `O`. Colors and the `·` for empty cells are applied only when drawing.

## Customizing

**Make Player 1 use X instead of O.** The symbol is picked with `values[turnCount % 2]`, so Player 1 (odd turns) gets `values[1]`. Swap the string to flip it:

```python
values = "OX"   # Player 1 = X, Player 2 = O
```

Also swap the two labels in the `playerTag` function and the banner text so the on-screen names match.

**Change colors.** Edit the ANSI constants near the top of `tictactoe.py` (`RED`, `CYAN`, `GREEN`, `YELLOW`).

**Turn off screen clearing.** Remove or comment out the `clearScreen()` call after a valid move.

## Project structure

```
tictactoe.py   # the whole game
README.md      # this file
```

## Possible improvements

- Highlight the winning line
- Ask to play again after a game ends
- Add a single-player mode against the computer
- Keep a running score across rounds
