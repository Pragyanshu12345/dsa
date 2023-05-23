class Solution:
    def ispossible(self, row, col, char, board):
        for i in range(9):
            if board[row][i] == char:
                return False
            if board[i][col] == char:
                return False
            if board[3*(row//3)+i//3][3*(col//3)+i % 3] == char:
                return False
        return True

    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for k in range(1, 10):
                        char = chr(k + ord('0'))
                        if self.ispossible(i, j, char, board) is True:
                            board[i][j] = char
                            if self.solve(board) is True:
                                return True
                            else:
                                board[i][j] = "."
                    return False
        return True

    def solveSudoku(self, board) -> None:
        self.solve(board)


sol = Solution()
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
sol.solveSudoku(board)
print(board)
