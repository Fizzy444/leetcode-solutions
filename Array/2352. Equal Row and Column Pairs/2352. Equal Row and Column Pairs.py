class Solution(object):
    def equalPairs(self, grid):
        from collections import Counter
        rows = Counter(tuple(row) for row in grid)
        cols = Counter(tuple(col) for col in zip(*grid))
        return sum(rows[r] * cols[r] for r in rows)