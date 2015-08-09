from itertools import product

ROWS = 11
COLS = 11


def is_alive(board, row, col):
    return board[row][col]


def alive_neighbours_count(board, row, col):
    cells = product([row-1, row, row+1], [col-1, col, col+1])
    neighbours = [(r, c) for r, c in cells if not (r == row and c == col)]
    valid_neighbours = [(r, c) for r, c in neighbours if 0 <= r < ROWS and 0 <= c < COLS]
    alive_neighbours = [True for (r, c) in valid_neighbours if is_alive(board, r, c)]
    return len(alive_neighbours)


def get_new_cell_status(board, row, col):
    if is_alive(board, row, col) and alive_neighbours_count(board, row, col) in (2, 3):
        return True
    if not is_alive(board, row, col) and alive_neighbours_count(board, row, col) == 3:
        return True
    return False


def evolve(board):
    return [[get_new_cell_status(board, row, col) for col in range(COLS)] for row in range(ROWS)]


def print_board(board):
    print()
    for row in range(ROWS):
        print(" ".join(["*" if is_alive(board, row, col) else "." for col in range(COLS)]))

import time
board = [[False] * COLS for row in range(ROWS)]

#board[3][3], board[3][4], board[3][5] = [True] * 3
#board[4][4], board[5][3], board[5][4], board[5][5] = [True] * 4
board[0][1], board[1][2], board[2][0], board[2][1], board[2][2] = [True] * 5

while True:
    print_board(board)
    time.sleep(0.5)
    board = evolve(board)
