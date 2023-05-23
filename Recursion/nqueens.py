"""
This module is for solving the famous n-Queens Problem, which states that for a board of n*n,
how many Queens can be placed such that following condition are satisfied:
Each row and column should contain 1 queen and no two queens should cross each other
"""
import copy


class Solution:
    """
    A class for solving the n-Queens problem
    """

    def is_possible(self, board, row, col, num):
        """
        A method to validate if it is safe to place a queen
        so that it shouldn't cross the other queen
        """
        row_idx, col_idx = row, col
        # check left column
        while col >= 0:
            if board[row][col] == 'Q':
                return False
            col -= 1
        col = col_idx
        # check upper diagonal
        while row >= 0 and col >= 0:
            if board[row][col] == 'Q':
                return False
            row, col = row-1, col-1
        row, col = row_idx, col_idx
        # check lower diagonal
        while row < num and col >= 0:
            if board[row][col] == 'Q':
                return False
            row, col = row+1, col-1
        return True

    def solve(self, ans, board, col, num):
        """
        A recursive method to check for all possibilities to place n queens
        """
        if col == num:
            return 1
        count = 0
        for row in range(num):
            if self.is_possible(board, row, col, num):
                board[row][col] = 'Q'
                count += self.solve(ans, copy.deepcopy(board), col+1, num)
                board[row][col] = '.'
        return count

    def solve_nqueens(self, num: int):
        """
        A method to initialize the parameters and solve the n-Queens problem
        """
        ans, board = [], []
        for _ in range(num):
            curr = []
            for _ in range(num):
                curr.append('.')
            board.append(curr)
        count = self.solve(ans, board, 0, num)
        print(count)
        result = []
        for solution in ans:
            board = []
            for row in solution:
                board.append("".join(row))
            result.append(board)
        return result


sol = Solution()
sol.solve_nqueens(5)
