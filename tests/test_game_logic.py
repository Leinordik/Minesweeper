import unittest
from src.game_logic import MinesweeperGame

class TestMinesweeperGame(unittest.TestCase):
    def test_initialization(self):
        game = MinesweeperGame(rows=5, cols=5, mines=5)
        self.assertEqual(game.rows, 5)
        self.assertEqual(game.cols, 5)
        self.assertEqual(game.mines, 5)
        mine_count = sum(cell == -1 for row in game.board for cell in row)
        self.assertEqual(mine_count, 5)

    def test_reveal_cell(self):
        game = MinesweeperGame(rows=3, cols=3, mines=1)
        # Find the mine location
        mine = None
        for r in range(3):
            for c in range(3):
                if game.board[r][c] == -1:
                    mine = (r, c)
                    break
            if mine:
                break
        # Reveal a safe cell
        safe_r, safe_c = (0, 0) if mine != (0, 0) else (1, 1)
        result = game.reveal_cell(safe_r, safe_c)
        self.assertTrue(result)
        self.assertTrue(game.revealed[safe_r][safe_c])

    def test_game_win(self):
        game = MinesweeperGame(rows=2, cols=2, mines=1)
        # Reveal all non-mine cells
        for r in range(2):
            for c in range(2):
                if game.board[r][c] != -1:
                    game.reveal_cell(r, c)
        self.assertTrue(game.is_won())

if __name__ == '__main__':
    unittest.main()
