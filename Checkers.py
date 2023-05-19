# Checkers

# Constants for the board size
ROWS = 8
COLS = 8

# Constants for the player symbols
PLAYER_X = 'X'
PLAYER_O = 'O'

# Function to initialize the board
def initialize_board():
    board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
    for row in range(ROWS):
        for col in range(COLS):
            if (row + col) % 2 == 1:
                if row < 3:
                    board[row][col] = PLAYER_X
                elif row > 4:
                    board[row][col] = PLAYER_O
    return board

# Function to print the board
def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

# Function to get all possible moves for a player
def get_possible_moves(board, player):
    moves = []
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == player:
                if player == PLAYER_X or player == 'XK':
                    if row > 0:
                        if col > 0 and board[row - 1][col - 1] == ' ':
                            moves.append(((row, col), (row - 1, col - 1)))
                        if col < COLS - 1 and board[row - 1][col + 1] == ' ':
                            moves.append(((row, col), (row - 1, col + 1)))
                    if board[row][col] == 'XK':
                        if row < ROWS - 1:
                            if col > 0 and board[row + 1][col - 1] == ' ':
                                moves.append(((row, col), (row + 1, col - 1)))
                            if col < COLS - 1 and board[row + 1][col + 1] == ' ':
                                moves.append(((row, col), (row + 1, col + 1)))
                if player == PLAYER_O or player == 'OK':
                    if row < ROWS - 1:
                        if col > 0 and board[row + 1][col - 1] == ' ':
                            moves.append(((row, col), (row + 1, col - 1)))
                        if col < COLS - 1 and board[row + 1][col + 1] == ' ':
                            moves.append(((row, col), (row + 1, col + 1)))
                    if board[row][col] == 'OK':
                        if row > 0:
                            if col > 0 and board[row - 1][col - 1] == ' ':
                                moves.append(((row, col), (row - 1, col - 1)))
                            if col < COLS - 1 and board[row - 1][col + 1] == ' ':
                                moves.append(((row, col), (row - 1, col + 1)))
    return moves

# Function to make a move on the board
def make_move(board, move):
    src, dest = move
    src_row, src_col = src
    dest_row, dest_col = dest
    player = board[src_row][src_col]
    board[src_row][src_col] = ' '
    board[dest_row][dest_col] = player
    if player == PLAYER_X and dest_row == 0:
        board[dest_row][dest_col] = 'XK'
    elif player == PLAYER_O and dest_row == ROWS - 1:
        board[dest_row][dest_col] = 'OK'
    elif abs(dest_row - src_row) == 2:
        captured_row = (src_row + dest_row) // 2
        captured_col = (src_col + dest_col) // 2
        board[captured_row][captured_col] = ' '
