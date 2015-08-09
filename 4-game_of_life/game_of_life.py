ROWS = 11
COLS = 11


def get_new_board():
    board = []
    for row in range(ROWS):
        board.append([False] * COLS)
    return board


def is_valid_position(row, col):
    return 0 <= row < ROWS and 0 <= col < COLS


def is_alive(board, row, col):
    return board[row][col]


def alive_neighbours_count(board, row, col):
    neighbours = [(row-1, col-1), (row-1, col), (row-1, col+1),
                  (row, col-1), (row, col+1),
                  (row+1, col-1), (row+1, col), (row+1, col+1)]
    count = 0
    for n_row, n_col in neighbours:
        if is_valid_position(n_row, n_col) and is_alive(board, n_row, n_col):
            count = count + 1
    return count


def evolve(board):
    new_board = get_new_board()
    for row in range(ROWS):
        for col in range(COLS):
            if is_alive(board, row, col) and alive_neighbours_count(board, row, col) in (2, 3):
                new_board[row][col] = True
            if not is_alive(board, row, col) and alive_neighbours_count(board, row, col) == 3:
                new_board[row][col] = True
    return new_board


def print_board(board):
    print()
    for row in range(ROWS):
        print(" ".join(["*" if is_alive(board, row, col) else "." for col in range(COLS)]))

import time
board = get_new_board()

#board[3][3], board[3][4], board[3][5] = [True] * 3
#board[4][4], board[5][3], board[5][4], board[5][5] = [True] * 4
board[0][1], board[1][2], board[2][0], board[2][1], board[2][2] = [True] * 5

while True:
    print_board(board)
    time.sleep(0.5)
    board = evolve(board)
