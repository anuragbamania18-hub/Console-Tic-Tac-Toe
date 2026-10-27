# Console-Tic-Tac-Toe
A lightweight, fully interactive Tic-Tac-Toe game playable directly in the terminal. Built entirely in Python, this project demonstrates fundamental programming concepts including game loops, robust input validation, and string-based state management.
Features
Interactive Game Loop: 
  Alternates turns between Player 1 (O) and Player 2 (X) with automatic win and draw detection.

Input Validation: 
  Actively rejects invalid inputs (non-1-3 numbers) and prevents players from overwriting previously claimed cells.
  Efficient State Management: Utilizes a single 9-character string to represent the 3x3 grid rather than a nested array structure.
  Dynamic ASCII Interface: Renders a clean, structured terminal grid that updates visually after every valid move.

How to Play
  Clone the repository to your local machine.
  Run the script in your terminal using python tictactoe.py (or your specific filename).
  Follow the prompts to enter a row number (1-3) and column number (1-3) to place your mark.
  The first player to align three matching marks horizontally, vertically, or diagonally wins the game.

Core Logic Highlights
  Coordinate Mapping: Transforms human-readable 2D coordinates into 1D string indices using the formula index = (row - 1) * 3 + (col - 1).

Optimized Win Checking:
  The script skips redundant condition checks during the early game, only evaluating the board for winning patterns from turn 5 onward (the   mathematical minimum for a win).
