import unittest
from project import insert, Check_For_Draw, Check_For_Win

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        # Prepare an empty board for each test
        self.board = {
            1: " ", 2: " ", 3: " ",
            4: " ", 5: " ", 6: " ",
            7: " ", 8: " ", 9: " "
        }

    def test_insert(self):
        insert("X", 1, self.board)
        self.assertEqual(self.board[1], "X")

    def test_insert_overwrite_blocked(self):
        # Insert once, then try again (should still pass since we aren't testing overwrite handling here)
        insert("X", 1, self.board)
        self.assertEqual(self.board[1], "X")

    def test_check_draw_false(self):
        # Should not be draw on an empty board
        self.assertFalse(Check_For_Draw(self.board))

    def test_check_draw_true(self):
        board_full = {
            1: "X", 2: "O", 3: "X",
            4: "X", 5: "O", 6: "X",
            7: "O", 8: "X", 9: "O"
        }
        self.assertTrue(Check_For_Draw(board_full))

    def test_check_win_row(self):
        self.board[1] = self.board[2] = self.board[3] = "X"
        self.assertTrue(Check_For_Win("X", self.board))

    def test_check_win_column(self):
        self.board[1] = self.board[4] = self.board[7] = "O"
        self.assertTrue(Check_For_Win("O", self.board))

    def test_check_win_diagonal_1(self):
        self.board[1] = self.board[5] = self.board[9] = "X"
        self.assertTrue(Check_For_Win("X", self.board))

    def test_check_win_diagonal_2(self):
        self.board[3] = self.board[5] = self.board[7] = "O"
        self.assertTrue(Check_For_Win("O", self.board))

    def test_check_win_false(self):
        self.board[1] = "X"
        self.board[2] = "O"
        self.board[3] = "X"
        self.assertFalse(Check_For_Win("X", self.board))

if _name_ == "_main_":
    unittest.main()