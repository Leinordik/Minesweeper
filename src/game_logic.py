import random

class MinesweeperGame:
    def __init__(self, rows=10, cols=10, mines=10):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]
        self.place_mines()

    def place_mines(self):
        count = 0
        while count < self.mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            if self.board[r][c] == 0:
                self.board[r][c] = -1
                self.update_neighbors(r, c)
                count += 1

    def update_neighbors(self, r, c):
        for i in range(max(0, r-1), min(self.rows, r+2)):
            for j in range(max(0, c-1), min(self.cols, c+2)):
                if self.board[i][j] != -1:
                    self.board[i][j] += 1

    def reveal_cell(self, r, c):
        if self.board[r][c] == -1:
            return False  # Hit a mine
        self.revealed[r][c] = True
        if self.board[r][c] == 0:
            for i in range(max(0, r-1), min(self.rows, r+2)):
                for j in range(max(0, c-1), min(self.cols, c+2)):
                    if not self.revealed[i][j]:
                        self.reveal_cell(i, j)
        return True

    def is_won(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] != -1 and not self.revealed[r][c]:
                    return False
        return True

    def display_board(self):
        for row in self.board:
            print(" ".join(['X' if cell == -1 else str(cell) for cell in row]))
