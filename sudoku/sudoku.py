from copy import deepcopy


class IllegalBoardStateException(Exception):
    pass


class Cell:
    def __init__(self, position):
        self.position = position
        self.possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    @property
    def value(self):
        return self.possibilities[0] if len(self.possibilities) == 1 else 0

    @value.setter
    def value(self, number):
        self.possibilities = [number]

    def block(self):
        row, col = self.position
        return (row // 3) * 3 + col // 3

    def is_same_row(self, cell):
        return self.position[0] == cell.position[0]

    def is_same_col(self, cell):
        return self.position[1] == cell.position[1]

    def is_same_block(self, cell):
        return self.block() == cell.block()

    def eliminate(self, number):
        try:
            self.possibilities.remove(number)
        except ValueError:
            pass

    def is_solved(self):
        return len(self.possibilities) == 1

    def __str__(self):
        return str(self.value)


class Board:
    def __init__(self):
        self.board = {}
        for row in range(9):
            for col in range(9):
                self.board[(row, col)] = Cell((row, col))

    def __str__(self):
        return "".join([str(self[(row, col)]) for row in range(9) for col in range(9)])

    def __setitem__(self, position, value):
        cur_cell = self[position]
        cur_cell.value = value
        for pos in self.related_cells(cur_cell):
            cell = self[pos]
            if cell.is_solved() and cell.value == value:
                raise IllegalBoardStateException("Contradiction found")
            if not cell.is_solved():
                cell.eliminate(value)
                if cell.is_solved():
                    self[pos] = cell.value

    def __getitem__(self, position):
        return self.board[position]

    def cells(self):
        return (self.board[(row, col)] for row in range(9) for col in range(9))

    def related_cells(self, cur_cell):
        return [cell.position for cell in self.cells() if cell != cur_cell and (
            cell.is_same_row(cur_cell) or cell.is_same_col(cur_cell) or cell.is_same_block(cur_cell))]

    def load(self, puzzle):
        for position, cell in self.board.items():
            value = puzzle[position[0] * 9 + position[1]]
            if value != ".":
                self[position] = int(value)

    def is_complete(self):
        return all([cell.is_solved() for cell in self.board.values()])

    def solve(self):
        if self.is_complete():
            return str(self)
        unsolved_cells = [(position, cell) for position, cell in self.board.items() if not cell.is_solved()]
        position, cell = unsolved_cells[0]
        for possibility in cell.possibilities:
            try:
                new_board = deepcopy(self)
                new_board[position] = possibility
                return new_board.solve()
            except IllegalBoardStateException:
                pass
        raise IllegalBoardStateException("No possible solution")


if __name__ == "__main__":
    board = Board()
    board.load("5..941872..1...4.3.84.........6..1...7..8..4...5..2.......1.98.3...5....6....7...")
    print(board.solve())
