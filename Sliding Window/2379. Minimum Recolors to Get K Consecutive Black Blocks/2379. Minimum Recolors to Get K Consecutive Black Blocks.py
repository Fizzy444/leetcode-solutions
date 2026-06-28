class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = 0
        for i in range(k):
            if blocks[i] == "W":
                white += 1
        ans = white
        for j in range(k, len(blocks)):
            if blocks[j-k] == "W":
                white -= 1
            if blocks[j] == "W":
                white += 1
            ans = min(ans, white)
        return ans