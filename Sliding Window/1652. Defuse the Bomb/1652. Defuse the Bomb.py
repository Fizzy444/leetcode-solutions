class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)

        if k == 0:
            return [0] * n

        ans = [0] * n

        for i in range(n):
            s = 0

            if k > 0:
                idx = i + 1
                for _ in range(k):
                    if idx == n:
                        idx = 0
                    s += code[idx]
                    idx += 1
            else:
                idx = i - 1
                for _ in range(-k):
                    if idx < 0:
                        idx = n - 1
                    s += code[idx]
                    idx -= 1

            ans[i] = s

        return ans