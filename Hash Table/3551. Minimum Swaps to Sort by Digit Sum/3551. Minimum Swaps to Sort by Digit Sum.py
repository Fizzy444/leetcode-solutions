
class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def digit_sum(n):
            total = 0
            while n:
                total += n % 10
                n //= 10
            return total

        arr = sorted((digit_sum(n), n, i) for i, n in enumerate(nums))

        swaps = 0
        visited = [False] * len(nums)

        for i in range(len(nums)):
            if visited[i] or arr[i][2] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = arr[j][2]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps
