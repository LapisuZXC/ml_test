from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # sudoku 0=9x9
        length = 9
        row_seen = set()
        column_seen = set()
        b_seen = set()
        for i in range(length):
            for j in range(length):
                if board[i][j] not in row_seen and board[i][j] != ".":
                    row_seen.add(board[i][j])
                else:
                    return False
                if board[j][i] not in column_seen and board[j][i] != ".":
                    column_seen.add(board[j][i])
                else:
                    return False
                boxI = 3 * (i // 3)
                boxJ = 3 * (i % 3)
                if board[boxI + j // 3][boxJ + j % 3] != ".":
                    if board[boxI + j // 3][boxJ + j % 3] in b_seen:
                        return False
                    b_seen.add(board[boxI + j // 3][boxJ + j % 3])

        return True
