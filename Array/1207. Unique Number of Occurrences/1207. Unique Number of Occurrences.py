class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        d = {}
        s = set()
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i,j in d.items():
            if j not in s:
                s.add(j)
            else:
                return False
        return True