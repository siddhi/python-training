import unittest
from .sudoku import Cell, Board, IllegalBoardStateException


class CellTest(unittest.TestCase):
    def test_setting_cell_value_should_clear_possibilities(self):
        cell = Cell((1, 1))
        cell.value = 5
        self.assertEqual([5], cell.possibilities)

    def test_elimination_should_remove_value_from_possibilities(self):
        cell = Cell((1, 1))
        cell.eliminate(1)
        self.assertEqual([2, 3, 4, 5, 6, 7, 8, 9], cell.possibilities)

    def test_eliminating_already_removed_item_does_not_give_error(self):
        cell = Cell((1, 1))
        cell.eliminate(1)
        cell.eliminate(1)
        self.assertEqual([2, 3, 4, 5, 6, 7, 8, 9], cell.possibilities)

    def test_cell_value_is_auto_set_if_all_possibilities_eliminated(self):
        cell = Cell((1, 1))
        for value in [2, 3, 4, 5, 6, 7, 8, 9]:
            cell.eliminate(value)
        self.assertEqual(1, cell.value)

    def test_cell_get_block(self):
        expected = [0, 0, 0, 1, 1, 1, 2, 2, 2,
                    0, 0, 0, 1, 1, 1, 2, 2, 2,
                    0, 0, 0, 1, 1, 1, 2, 2, 2,
                    3, 3, 3, 4, 4, 4, 5, 5, 5,
                    3, 3, 3, 4, 4, 4, 5, 5, 5,
                    3, 3, 3, 4, 4, 4, 5, 5, 5,
                    6, 6, 6, 7, 7, 7, 8, 8, 8,
                    6, 6, 6, 7, 7, 7, 8, 8, 8,
                    6, 6, 6, 7, 7, 7, 8, 8, 8]
        positions = [(row, col) for row in range(9) for col in range(9)]
        for value, position in zip(expected, positions):
            cell = Cell(position)
            self.assertEqual(value, cell.block())

    def test_is_same_row(self):
        cell_1 = Cell((1, 1))
        cell_2 = Cell((1, 5))
        cell_3 = Cell((2, 1))
        self.assertTrue(cell_1.is_same_row(cell_2))
        self.assertFalse(cell_1.is_same_row(cell_3))

    def test_is_same_col(self):
        cell_1 = Cell((1, 1))
        cell_2 = Cell((1, 5))
        cell_3 = Cell((2, 1))
        self.assertTrue(cell_1.is_same_col(cell_3))
        self.assertFalse(cell_1.is_same_col(cell_2))

    def test_is_same_block(self):
        cell_1 = Cell((1, 1))
        cell_2 = Cell((1, 5))
        cell_3 = Cell((2, 2))
        self.assertTrue(cell_1.is_same_block(cell_3))
        self.assertFalse(cell_1.is_same_block(cell_2))


class BoardTest(unittest.TestCase):
    simple_puzzle = """.781...2.1...62..35...9....8.....4.6.61.7..9..9....3.....5.42.76...8..3..5.7..9.."""
    simple_puzzle_answer = """378145629149862753526397148835921476261473895794658312983514267617289534452736981"""
    medium_puzzle = """...9.7..3.8..1..4.3...4..6.1...942...9..8..3...637...9.6..3...5.7..6..2.4..7.8..."""
    medium_puzzle_answer = """654927813789613542312845967137594286295186734846372159968231475571469328423758691"""
    hard_puzzle = """3.48.......5.2...8..7..6.....12..9..9.3...4.1..61938.....4..2..5...123....2..87.6"""
    almost_solved_puzzle = """1425763897963842515389126749742351682516987438637419254271538963894675126158.9437"""
    solved_puzzle = """142576389796384251538912674974235168251698743863741925427153896389467512615829437"""

    def test_a_new_board_is_not_complete(self):
        board = Board()
        self.assertFalse(board.is_complete())

    def test_a_complete_board(self):
        board = Board()
        board.load(self.solved_puzzle)
        self.assertTrue(board.is_complete())

    def test_set_a_value_on_the_board(self):
        board = Board()
        board.load(self.almost_solved_puzzle)
        board[(8, 4)] = 2
        self.assertTrue(board.is_complete())

    def test_get_related_cells(self):
        board = Board()
        board.load(self.solved_puzzle)
        expected = [(1, 0), (1, 1), (1, 2), (1, 4), (1, 5),
                    (1, 6), (1, 7), (1, 8), (0, 3), (2, 3),
                    (3, 3), (4, 3), (5, 3), (6, 3), (7, 3),
                    (8, 3), (0, 4), (0, 5), (2, 4), (2, 5)]
        cell = board[(1, 3)]
        self.assertEqual(sorted(expected), sorted(board.related_cells(cell)))

    def test_setting_a_value_eliminates_it_from_related_cells(self):
        board = Board()
        board[(0, 0)] = 1
        self.assertTrue(1 not in board[(0, 1)].possibilities)
        self.assertTrue(1 not in board[(1, 0)].possibilities)
        self.assertTrue(1 not in board[(1, 1)].possibilities)

    def set_cell_value(self, cell, states):
        """A helper method to set the value of cell to a particular value"""
        for num in range(1, 10):
            if num not in states:
                cell.eliminate(num)

    def test_a_cell_that_completes_during_propagation_should_also_trigger_propagation(self):
        board = Board()
        self.set_cell_value(board[(0, 1)], [1, 2])
        board[(0, 0)] = 1
        self.assertTrue(2 not in board[(0, 0)].possibilities)
        self.assertTrue(2 not in board[(0, 2)].possibilities)
        self.assertTrue(2 not in board[(1, 1)].possibilities)
        self.assertTrue(2 not in board[(1, 2)].possibilities)

    def test_exception_is_thrown_on_contradiction(self):
        board = Board()
        board[(0, 0)] = 1
        with self.assertRaises(IllegalBoardStateException):
            board[(0, 1)] = 1

    def test_exception_is_thrown_on_unsolvable_state(self):
        board = Board()
        board.load(self.medium_puzzle)
        board[(0, 0)] = 5
        with self.assertRaises(IllegalBoardStateException):
            board.solve()

    def test_solve_simple_puzzle(self):
        board = Board()
        board.load(self.simple_puzzle)
        answer = board.solve()
        self.assertEqual(self.simple_puzzle_answer, answer)

    def test_should_try_options_if_not_solved_by_constraints(self):
        board = Board()
        board.load(self.medium_puzzle)
        answer = board.solve()
        self.assertEqual(self.medium_puzzle_answer, answer)
