class Solution(object):
    def isValidSudoku(self, board):
        seen = set()
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num != ".":
                    if (num, r) in seen or (c, num) in seen or (r//3, c//3, num) in seen:
                        return False
                    seen.add((num, r))
                    seen.add((c, num))
                    seen.add((r//3, c//3, num))
        return True