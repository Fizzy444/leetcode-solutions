class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        r = []
        while i < len(firstList) and j < len(secondList):
            m1 = max(firstList[i][0],secondList[j][0])
            m2 = min(firstList[i][1],secondList[j][1])

            if m1 <= m2:
                r.append([m1,m2])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return r