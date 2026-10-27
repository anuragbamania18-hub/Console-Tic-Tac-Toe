import os

os.system("")  # Makes ANSI colours work on Windows terminals too (harmless elsewhere)

# ---------- Looks (colours + helpers) ----------
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[91m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"

def paint(cell):
    # Turns a board character into a coloured symbol. The board string itself is never changed.
    if cell == "X":
        return BOLD + RED + "X" + RESET
    if cell == "O":
        return BOLD + CYAN + "O" + RESET
    return DIM + "·" + RESET

def playerTag(player):
    # Because of values[turnCount % 2], Player 1 places O (cyan) and Player 2 places X (red)
    colour = CYAN if player == "1" else RED
    symbol = "O" if player == "1" else "X"
    return BOLD + colour + "Player " + player + " (" + symbol + ")" + RESET

def showBoard(board):
    print()
    print(DIM + "      1   2   3" + RESET)
    print("    ┏━━━┳━━━┳━━━┓")
    print(DIM + "  1 " + RESET + "┃ " + paint(board[0]) + " ┃ " + paint(board[1]) + " ┃ " + paint(board[2]) + " ┃")
    print("    ┣━━━╋━━━╋━━━┫")
    print(DIM + "  2 " + RESET + "┃ " + paint(board[3]) + " ┃ " + paint(board[4]) + " ┃ " + paint(board[5]) + " ┃")
    print("    ┣━━━╋━━━╋━━━┫")
    print(DIM + "  3 " + RESET + "┃ " + paint(board[6]) + " ┃ " + paint(board[7]) + " ┃ " + paint(board[8]) + " ┃")
    print("    ┗━━━┻━━━┻━━━┛")
    print()

def clearScreen():
    print("\033[H\033[J", end="")

def banner():
    print()
    print(BOLD + YELLOW + "  ╔═══════════════════════════╗" + RESET)
    print(BOLD + YELLOW + "  ║" + RESET + BOLD + "      TIC  ·  TAC  ·  TOE  " + RESET + BOLD + YELLOW + "    ║" + RESET)
    print(BOLD + YELLOW + "  ╚═══════════════════════════╝" + RESET)
    print(DIM + "   Player 1 = O    Player 2 = X" + RESET)

def warn(message):
    print()
    print(YELLOW + "  ! " + message + RESET)
    print()

# ---------- Game ----------

# Initialising the board for the start of a new game

board = "........."
turnCount = 1 # Keeps Track of how many turns of the game passes

clearScreen()
banner()
showBoard(board)

# Game Starts from Here
while True:

    validMove = False # Used to cross-check the validity of a move made
    values = "XO" # Possible Values that can be placed in the grid.

    if ( turnCount % 2 == 0 ):
        currentPlayer = "2" # Keeps Track of the player whose turn it is
    else:
        currentPlayer = "1"

    row = input(playerTag(currentPlayer) + " - enter row (1-3): ")

    while ( ( row != "1" ) and ( row != "2" ) and ( row != "3" ) ): # Checks if row entered is a valid row number
        warn("Please enter number between 1 and 3.")
        row = input(playerTag(currentPlayer) + " - enter row (1-3): ") # Prompts user to enter value again

    col = input(playerTag(currentPlayer) + " - enter column (1-3): ")

    while ( ( col != "1" ) and ( col != "2" ) and ( col != "3" ) ):
        warn("Please enter number between 1 and 3.")
        col = input(playerTag(currentPlayer) + " - enter column (1-3): ")

    while not validMove: # Repeats continually until the move is updated into a valid, empty cell

        validMove = True
        index = ( int(row) - 1 ) * 3 + ( int(col) - 1 ) # Any coordinate in the grid can be converted into an index of the string 'board' using this formula.

        if ( board[index] == "." ): # Condition if cell is empty
            board = board[:index] + values[ turnCount % 2] + board[index + 1:] # Uses String Splicing to rewrite the board
        else:
            warn("This cell is already taken")
            validMove = False

        if not validMove: #if cell was not empty, then prompts user to input new values of row and column

            row = input(playerTag(currentPlayer) + " - enter row (1-3): ")

            while ( ( row != "1" ) and ( row != "2" ) and ( row != "3" ) ):
                warn("Please enter number between 1 and 3.")
                row = input(playerTag(currentPlayer) + " - enter row (1-3): ")

            col = input(playerTag(currentPlayer) + " - enter column (1-3): ")

            while ( ( col != "1" ) and ( col != "2" ) and ( col != "3" ) ):
                warn("Please enter number between 1 and 3.")
                col = input(playerTag(currentPlayer) + " - enter column (1-3): ")

    clearScreen() # Wipes the old board so only the latest one is on screen
    banner()
    showBoard(board) # Prints the updated board after every valid move

    if ( turnCount >= 5 ): # we check the win condition only after 5 turns are complete as that is the minimum number of turns the game can take before someone wins

        if ((board[0] == board[1] == board[2] and board[0] != ".") or # Checks if all values of 1st row are matching
            (board[3] == board[4] == board[5] and board[3] != ".") or # Checks if all values of 2nd row are matching
            (board[6] == board[7] == board[8] and board[6] != ".") or # Checks if all values of 3rd row are matching
            (board[0] == board[3] == board[6] and board[0] != ".") or # Checks if all values of 1st column are matching
            (board[1] == board[4] == board[7] and board[1] != ".") or # Checks if all values of 2nd column are matching
            (board[2] == board[5] == board[8] and board[2] != ".") or # Checks if all values of 3rd column are matching
            (board[0] == board[4] == board[8] and board[0] != ".") or # Checks if all values of left-right diagonal match
            (board[2] == board[4] == board[6] and board[2] != ".")): # Checks if all values of right-left diagonal match

            print("  " + BOLD + GREEN + "🏆 Player " + RESET + paint(values[ turnCount % 2]) + BOLD + GREEN + " wins!" + RESET) # The turn count can be used to find the winner of game.
            print()
            break

    if ( turnCount == 9 ):  # If no winner is decided by turn 9, then the game is automatically drawn as max number of cells in a game is 9 and no more cells are available to be drawn in.
        print("  " + BOLD + YELLOW + "🤝 It's a Draw" + RESET)
        print()
        break

    turnCount = turnCount + 1
