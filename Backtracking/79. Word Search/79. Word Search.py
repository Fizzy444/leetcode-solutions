class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def solve(i, j, idx):
            if i < 0 or j < 0 or i >= r or j >= c or board[i][j] != word[idx] or board[i][j] == "#":
                return False
            
            if n == idx + 1:
                return True
            ch = board[i][j]
            board[i][j] = "#"
            if solve(i + 1, j, idx + 1):
                return True
            if solve(i - 1, j, idx + 1):
                return True
            if solve(i, j + 1, idx + 1):
                return True
            if solve(i, j - 1, idx + 1):
                return True
            
            board[i][j] = ch
            return False
        n = len(word)
        r = len(board)
        c = len(board[0])
        if r * c < n:
            return False
        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    if solve(i, j, 0):
                        return True
        return False