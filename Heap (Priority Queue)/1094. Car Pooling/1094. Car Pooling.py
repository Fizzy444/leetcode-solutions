class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        import heapq
        trips.sort(key = lambda x : x[1])
        l = []
        o = 0
        for p, s, e in trips:
            while l and l[0][0] <= s:
                end, pas = heapq.heappop(l)
                o -= pas
            o += p

            if o > capacity:
                return False
            heapq.heappush(l, [e, p])
        return True