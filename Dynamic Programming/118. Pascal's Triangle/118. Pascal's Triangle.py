class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        r = []
        for i in range(numRows):
            t = [1]*(i+1)
            for j in range(1,i):
                t[j] = r[i-1][j-1] + r[i-1][j]
            r.append(t)
        return r